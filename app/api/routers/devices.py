from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.schemas.device import DeviceCreate, DeviceUpdate, DeviceRead, DeviceStatus
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime

from app.database import get_db
from app.models.device import Device
from app.models.register import Register

# These will exist once you create your schemas and models
# from app.schemas.device import DeviceCreate, DeviceUpdate, DeviceRead
# from app.models.device import Device
# from app.db import get_db

router = APIRouter(prefix="/devices", tags=["devices"])

# -----------------------------
# Device CRUD
# -----------------------------



@router.post("/", response_model=DeviceRead, summary="Create a new device")
async def create_device(payload: DeviceCreate, db: AsyncSession = Depends(get_db)):
    # Check if device name already exists
    existing = await db.execute(select(Device).where(Device.name == payload.name))
    if existing.scalars().first():
        raise HTTPException(400, detail="Device with this name already exists")

    # Create device row
    device = Device(
        name=payload.name,
        port=payload.port,
        update_interval=payload.update_interval,
        strategy=payload.strategy,
        description=None,
        created_at=datetime.utcnow(),
    )
    db.add(device)
    await db.flush()  # ensures device.id is available

    # Create a default register for the device (optional)
    # You can remove this if you want registers created separately
    default_register = Register(
        device_id=device.id,
        address=0,
        type="holding",
        value=0.0,
        description="Auto-created default register",
    )
    db.add(default_register)

    await db.commit()
    await db.refresh(device)

    return device



@router.get("/", response_model=List[DeviceRead], summary="Get all devices")
def list_devices(
    # db = Depends(get_db)
):
    """
    Return all configured devices.
    """
    # TODO: query DB
    return {"devices": []}


@router.get("/{device_id}", response_model=DeviceRead, summary="Get device details")
def get_device(
    device_id: int,
    # db = Depends(get_db)
):
    """
    Return full configuration for a single device.
    """
    # TODO: query DB
    return DeviceRead(
        id=device_id,
        name="Example Device",
        port=5020,
        update_interval=1.0,
        strategy="random",
        enabled=True,
        created_at=datetime.utcnow(),
    )


@router.put(
    "/{device_id}", response_model=DeviceRead, summary="Update device configuration"
)
def update_device(
    device_id: int,
    payload: DeviceUpdate,
    # db = Depends(get_db)
):
    """
    Update configuration for a device.
    """
    # TODO: update DB
    return DeviceRead(
        id=device_id,
        name=payload.name,
        port=payload.port or 5020,
        update_interval=payload.update_interval or 1.0,
        strategy=payload.strategy or "random",
        enabled=payload.enabled if payload.enabled is not None else True,
        created_at=datetime.utcnow(),
    )


@router.delete("/{device_id}", summary="Delete a device")
def delete_device(
    device_id: int,
    # db = Depends(get_db)
):
    """
    Delete or deactivate a device.
    """
    # TODO: delete from DB
    return {"message": f"Device {device_id} deleted (placeholder)"}


# -----------------------------
# Simulation control
# -----------------------------


@router.post("/{device_id}/start", summary="Start simulation for a device")
def start_device(
    device_id: int,
    # db = Depends(get_db)
):
    """
    Enable simulation for this device.
    """
    # TODO: update DB state or send signal to simulator
    return {"message": f"Device {device_id} simulation started (placeholder)"}


@router.post("/{device_id}/stop", summary="Stop simulation for a device")
def stop_device(
    device_id: int,
    # db = Depends(get_db)
):
    """
    Disable simulation for this device.
    """
    # TODO: update DB state or send signal to simulator
    return {"message": f"Device {device_id} simulation stopped (placeholder)"}


# -----------------------------
# Device status
# -----------------------------


@router.get(
    "/{device_id}/status",
    response_model=DeviceStatus,
    summary="Get device runtime status",
)
def device_status(
    device_id: int,
    # db = Depends(get_db)
):
    """
    Return runtime status for a device.
    """
    # TODO: query DB or simulator
    return DeviceStatus(
        device_id=device_id,
        enabled=True,
        last_update=datetime.utcnow(),
        register_count=5,
        status="running",
    )
