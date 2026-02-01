from fastapi import APIRouter
from datetime import datetime
import psutil

from api.api.app.schemas.system import (
    HealthStatus,
    SystemMetrics,
    SimulationStatus,
    SystemOverview
)

router = APIRouter(
    prefix="/system",
    tags=["system"]
)


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------
@router.get("/health", response_model=HealthStatus)
def get_health_status():
    return HealthStatus(
        status="ok",
        timestamp=datetime.utcnow(),
        database="connected",       # TODO: replace with real DB check
        simulator="running"         # TODO: replace with real simulation engine state
    )


# ---------------------------------------------------------
# System metrics
# ---------------------------------------------------------
@router.get("/metrics", response_model=SystemMetrics)
def get_system_metrics():
    return SystemMetrics(
        uptime_seconds=psutil.boot_time(),   # TODO: replace with app uptime if needed
        cpu_percent=psutil.cpu_percent(interval=0.1),
        memory_percent=psutil.virtual_memory().percent,
        active_devices=0,                    # TODO: query DB
        active_registers=0                   # TODO: query DB
    )


# ---------------------------------------------------------
# Simulation engine status
# ---------------------------------------------------------
@router.get("/simulation", response_model=SimulationStatus)
def get_simulation_status():
    return SimulationStatus(
        running=True,                        # TODO: real engine state
        last_tick=None,                      # TODO: track simulation ticks
        tick_interval=1.0,                   # TODO: load from config
        strategy_count=0                     # TODO: count active strategies
    )


# ---------------------------------------------------------
# Combined system overview
# ---------------------------------------------------------
@router.get("/overview", response_model=SystemOverview)
def get_system_overview():
    health = HealthStatus(
        status="ok",
        timestamp=datetime.utcnow(),
        database="connected",
        simulator="running"
    )

    metrics = SystemMetrics(
        uptime_seconds=psutil.boot_time(),
        cpu_percent=psutil.cpu_percent(interval=0.1),
        memory_percent=psutil.virtual_memory().percent,
        active_devices=0,
        active_registers=0
    )

    simulation = SimulationStatus(
        running=True,
        last_tick=None,
        tick_interval=1.0,
        strategy_count=0
    )

    return SystemOverview(
        health=health,
        metrics=metrics,
        simulation=simulation
    )
