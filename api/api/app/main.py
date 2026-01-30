from fastapi import FastAPI
from routers import devices, registers, system, telemetry, values

app = FastAPI()
app.include_router(devices.router)

@app.get("/health")
def health():
    return {"status": "ok"}