from fastapi import FastAPI

# Import your routers
from app.api.routers.devices import router as devices_router
from app.api.routers.registers import router as registers_router
from app.api.routers.telemetry import router as telemetry_router

# If you want to start the simulator on startup:
# from app.simulator.engine import SimulatorEngine

app = FastAPI(title="Modbus Simulator API")

# Register routers
app.include_router(devices_router, prefix="/devices", tags=["Devices"])
app.include_router(registers_router, prefix="/registers", tags=["Registers"])
app.include_router(telemetry_router, prefix="/telemetry", tags=["Telemetry"])

# Optional: startup event
# @app.on_event("startup")
# async def startup_event():
#     simulator = SimulatorEngine()
#     await simulator.start()


@app.get("/")
async def root():
    return {"status": "ok", "message": "Modbus Simulator API running"}
