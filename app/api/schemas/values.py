from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ---------------------------------------------------------
# Read a single register value
# ---------------------------------------------------------


class RegisterValue(BaseModel):
    register_id: int = Field(..., description="ID of the register")
    device_id: int = Field(..., description="ID of the parent device")
    value: float = Field(..., description="Current value of the register")
    timestamp: datetime = Field(..., description="Timestamp when the value was read")


# ---------------------------------------------------------
# Write/update a single register value
# ---------------------------------------------------------


class RegisterValueWrite(BaseModel):
    value: float = Field(..., description="New value to write to the register")


# ---------------------------------------------------------
# Batch read response
# ---------------------------------------------------------


class RegisterValueBatch(BaseModel):
    values: List[RegisterValue] = Field(..., description="List of register values")
    count: int = Field(..., description="Number of values returned")


# ---------------------------------------------------------
# Batch write request
# ---------------------------------------------------------


class RegisterValueWriteItem(BaseModel):
    register_id: int = Field(..., description="Register to update")
    value: float = Field(..., description="New value to write")


class RegisterValueWriteBatch(BaseModel):
    writes: List[RegisterValueWriteItem] = Field(
        ..., description="List of register updates"
    )


# ---------------------------------------------------------
# Optional: value metadata (for diagnostics)
# ---------------------------------------------------------


class RegisterValueMeta(BaseModel):
    register_id: int
    device_id: int
    last_update: Optional[datetime] = None
    status: str = Field(..., example="ok", description="ok | stale | error")
