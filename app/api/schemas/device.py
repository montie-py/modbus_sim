from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# -----------------------------
# Base shared fields
# -----------------------------


class DeviceBase(BaseModel):
    name: str = Field(..., example="Boiler Pump Simulator")
    port: int = Field(..., example=5020, description="Modbus/TCP port")
    update_interval: float = Field(
        example=1.0, description="Seconds between register updates"
    )
    strategy: str = Field(
        ..., example="random", description="Update strategy: random | sine | ramp"
    )


# -----------------------------
# Create
# -----------------------------


class DeviceCreate(DeviceBase):
    enabled: bool = Field(
        default=False, description="Whether the simulator should start immediately"
    )


# -----------------------------
# Update (partial)
# -----------------------------


class DeviceUpdate(BaseModel):
    name: Optional[str] = None
    port: Optional[int] = None
    update_interval: Optional[float] = None
    strategy: Optional[str] = None
    enabled: Optional[bool] = None


# -----------------------------
# Read (returned to client)
# -----------------------------


class DeviceRead(DeviceBase):
    id: int
    enabled: bool
    created_at: datetime

    class Config:
        orm_mode = True


# -----------------------------
# Status endpoint
# -----------------------------


class DeviceStatus(BaseModel):
    device_id: int
    enabled: bool
    last_update: Optional[datetime]
    register_count: int
    status: str = Field(..., example="running", description="running | stopped | error")
