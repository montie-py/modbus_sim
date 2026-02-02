from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ---------------------------------------------------------
# Single telemetry sample
# ---------------------------------------------------------


class TelemetrySample(BaseModel):
    register_id: int = Field(
        ..., description="ID of the register producing the telemetry"
    )
    device_id: int = Field(..., description="ID of the parent device")
    value: float = Field(..., description="Measured or simulated value")
    timestamp: datetime = Field(..., description="Timestamp of the telemetry sample")


# ---------------------------------------------------------
# Batch of telemetry samples
# ---------------------------------------------------------


class TelemetryBatch(BaseModel):
    samples: List[TelemetrySample] = Field(..., description="List of telemetry samples")
    count: int = Field(..., description="Number of samples returned")


# ---------------------------------------------------------
# Query parameters for telemetry history
# ---------------------------------------------------------


class TelemetryQuery(BaseModel):
    device_id: Optional[int] = Field(None, description="Filter by device ID")
    register_id: Optional[int] = Field(None, description="Filter by register ID")
    start_time: Optional[datetime] = Field(None, description="Start of time range")
    end_time: Optional[datetime] = Field(None, description="End of time range")
    limit: int = Field(100, description="Maximum number of samples to return")


# ---------------------------------------------------------
# Telemetry statistics (optional analytics)
# ---------------------------------------------------------


class TelemetryStats(BaseModel):
    register_id: int
    device_id: int
    min_value: float
    max_value: float
    avg_value: float
    sample_count: int
    start_time: datetime
    end_time: datetime


# ---------------------------------------------------------
# Live telemetry payload (for WebSocket/SSE)
# ---------------------------------------------------------


class TelemetryLive(BaseModel):
    register_id: int
    device_id: int
    value: float
    timestamp: datetime
    status: str = Field(..., example="ok", description="ok | stale | error")
