from fastapi import FastAPI
import asyncio

from app.api.routers.devices import router as devices_router
from app.api.routers.registers import router as registers_router
from app.api.routers.telemetry import router as telemetry_router
from app.simulator.strategy_factory import strategy_factory
from app.models.device import Device
from sqlalchemy import select
from app.models.register import Register
from app.database import AsyncSessionLocal

# Import your simulator
from app.simulator.modbus_server import ModbusServer, ModbusDeviceSimulator

app = FastAPI(title="Modbus Simulator API")

# Global reference so your /api routes can access the server
modbus_server: ModbusServer | None = None


@app.on_event("startup")
async def startup_event():
    global modbus_server

    # Create the Modbus server using the port of the FIRST device
    # (or you can support multiple servers later)
    async with AsyncSessionLocal() as session:
        devices = await session.execute(select(Device))
        devices = devices.scalars().all()

        if not devices:
            print("No devices found in DB")
            return

        # For now: one Modbus server per application
        port = devices[0].port
        modbus_server = ModbusServer(port=port)

        for device in devices:
            # Build strategy instance
            strategy = strategy_factory(device.strategy)

            # Load registers for this device
            regs = await session.execute(
                select(Register).where(Register.device_id == device.id)
            )
            regs = regs.scalars().all()

            # For now: assume one register per device
            # (you can extend this to multi-register devices later)
            if not regs:
                continue

            register = regs[0].address

            modbus_server.add_device(
                device.name,
                ModbusDeviceSimulator(
                    strategy=strategy,
                    register=register,
                    interval=device.update_interval,
                )
            )

    asyncio.create_task(modbus_server.start())



# Register routers
app.include_router(devices_router, prefix="/devices", tags=["Devices"])
app.include_router(registers_router, prefix="/registers", tags=["Registers"])
app.include_router(telemetry_router, prefix="/telemetry", tags=["Telemetry"])


@app.get("/")
async def root():
    return {"status": "ok", "message": "Modbus Simulator API running"}
