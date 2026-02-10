import asyncio
from typing import Dict

from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
)

from .strategies import BaseStrategy


class ModbusDeviceSimulator:
    def __init__(self, strategy: BaseStrategy, register: int, interval: float = 1.0):
        self.strategy = strategy
        self.register = register
        self.interval = interval

    async def run(self, context: ModbusServerContext):
        while True:
            slave = context[0x00]

            # Read current holding register (function code 3)
            current = slave["hr"].getValues(self.register, count=1)[0]

            # Compute next value
            new_value = self.strategy.next_value(current)

            # Write new value
            slave["hr"].setValues(self.register, [int(new_value)])

            await asyncio.sleep(self.interval)


class ModbusServer:
    def __init__(self, host: str = "0.0.0.0", port: int = 502):
        self.host = host
        self.port = port
        self.devices: Dict[str, ModbusDeviceSimulator] = {}

        # Create datastore with 100 holding registers
        self.context = ModbusServerContext(
            slaves={
                0x00: {
                    "hr": ModbusSequentialDataBlock(0, [0] * 100),
                    "ir": ModbusSequentialDataBlock(0, [0] * 100),
                    "co": ModbusSequentialDataBlock(0, [0] * 100),
                    "di": ModbusSequentialDataBlock(0, [0] * 100),
                }
            }
        )

    def add_device(self, name: str, device: ModbusDeviceSimulator):
        self.devices[name] = device

    async def start(self):
        # Start device update tasks
        for device in self.devices.values():
            asyncio.create_task(device.run(self.context))

        # Start Modbus TCP server
        await StartAsyncTcpServer(
            context=self.context,
            address=(self.host, self.port),
        )
