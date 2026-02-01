from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ---------------------------------------------------------
# System health / readiness
# ---------------------------------------------------------

class HealthStatus(BaseModel):
    status: str = Field(..., example="ok", description="Overall system health")
    timestamp: datetime = Field(..., description="Time of health check")
    database: str = Field(..., example="connected", description="Database connection status")
    simulator: str = Field(..., example="running", description="Simulation engine status")


# ---------------------------------------------------------
# System metrics (CPU, memory, uptime)
# ---------------------------------------------------------

class SystemMetrics(BaseModel):
    uptime_seconds: float = Field(..., description="System uptime in seconds")
    cpu_percent: float = Field(..., description="CPU usage percentage")
    memory_percent: float = Field(..., description="Memory usage percentage")
    active_devices: int = Field(..., description="Number of active simulated devices")
    active_registers: int = Field(..., description="Number of active registers")


# ---------------------------------------------------------
# Simulation engine status
# ---------------------------------------------------------

class SimulationStatus(BaseModel):
    running: bool = Field(..., description="Whether the simulation engine is active")
    last_tick: Optional[datetime] = Field(None, description="Last simulation update timestamp")
    tick_interval: float = Field(..., description="Simulation update interval in seconds")
    strategy_count: int = Field(..., description="Number of active update strategies")


# ---------------------------------------------------------
# Combined system overview
# ---------------------------------------------------------

class SystemOverview(BaseModel):
    health: HealthStatus
    metrics: SystemMetrics
    simulation: SimulationStatus


# ---------------------------------------------------------
# Optional: system configuration schema
# ---------------------------------------------------------

class SystemConfig(BaseModel):
    simulation_interval: float = Field(..., description="Global simulation tick interval")
    max_devices: int = Field(..., description="Maximum allowed devices")
    max_registers: int = Field(..., description="Maximum allowed registers")
    telemetry_logging: bool = Field(..., description="Enable or disable telemetry logging")
