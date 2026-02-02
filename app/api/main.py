from fastapi import FastAPI
from routers import devices

app = FastAPI()
app.include_router(devices.router)

@app.get("/health")
def health():
    return {"status": "ok"}