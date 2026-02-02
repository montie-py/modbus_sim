from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ---------------------------------------------------------
# Shared fields
# ---------------------------------------------------------


class RegisterBase(BaseModel):
    device_id: int = Field(..., description="ID of the parent device")
    address: int = Field(..., ge=0, description="Register address")
    type: str = Field(
        ...,
        example="holding",
        description="Register type: holding | input | coil | discrete",
    )
    value: float = Field(..., description="Current register value")
    description: Optional[str] = Field(
        None,
        example="Pump pressure reading",
        description="Optional human-readable description",
    )


# ---------------------------------------------------------
# Create
# ---------------------------------------------------------


class RegisterCreate(RegisterBase):
    pass


# ---------------------------------------------------------
# Update (partial)
# ---------------------------------------------------------


class RegisterUpdate(BaseModel):
    address: Optional[int] = None
    type: Optional[str] = None
    value: Optional[float] = None
    description: Optional[str] = None


# ---------------------------------------------------------
# Read (returned to client)
# ---------------------------------------------------------


class RegisterRead(RegisterBase):
    id: int
    created_at: datetime | None = None

    class Config:
        orm_mode = True


# ---------------------------------------------------------
# Value update endpoint (optional)
# ---------------------------------------------------------


class RegisterValueUpdate(BaseModel):
    value: float = Field(..., description="New value to write to the register")


# ---------------------------------------------------------
# Optional: runtime status (if you add simulation state)
# ---------------------------------------------------------


class RegisterStatus(BaseModel):
    register_id: int
    value: float
    last_update: Optional[datetime]
    status: str = Field(..., example="active", description="active | stale | error")
