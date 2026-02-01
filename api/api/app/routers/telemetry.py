from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from api.api.app.schemas.telemetry import (
    TelemetrySample,
    TelemetryBatch,
    TelemetryQuery,
    TelemetryStats,
    TelemetryLive
)

# When ORM is added:
# from app.models.telemetry import Telemetry
# from app.database import get_db

router = APIRouter(
    prefix="/telemetry",
    tags=["telemetry"]
)


# ---------------------------------------------------------
# Query telemetry history
# ---------------------------------------------------------
@router.get("/", response_model=TelemetryBatch)
def get_telemetry(
    query: TelemetryQuery = Depends(),
    # db: Session = Depends(get_db)
):
    # TODO: Replace with ORM query
    # Example:
    # q = db.query(Telemetry)
    # if query.device_id:
    #     q = q.filter(Telemetry.device_id == query.device_id)
    # if query.register_id:
    #     q = q.filter(Telemetry.register_id == query.register_id)
    # if query.start_time:
    #     q = q.filter(Telemetry.timestamp >= query.start_time)
    # if query.end_time:
    #     q = q.filter(Telemetry.timestamp <= query.end_time)
    # samples = q.order_by(Telemetry.timestamp.desc()).limit(query.limit).all()

    samples = [
        TelemetrySample(
            register_id=query.register_id or 1,
            device_id=query.device_id or 1,
            value=42.0,
            timestamp=datetime.utcnow()
        )
    ]

    return TelemetryBatch(samples=samples, count=len(samples))


# ---------------------------------------------------------
# Get latest telemetry for a register
# ---------------------------------------------------------
@router.get("/{register_id}", response_model=TelemetrySample)
def get_latest_telemetry(
    register_id: int,
    # db: Session = Depends(get_db)
):
    # TODO: ORM lookup for latest sample
    # sample = (
    #     db.query(Telemetry)
    #     .filter(Telemetry.register_id == register_id)
    #     .order_by(Telemetry.timestamp.desc())
    #     .first()
    # )
    # if not sample:
    #     raise HTTPException(404, "No telemetry found")

    return TelemetrySample(
        register_id=register_id,
        device_id=1,
        value=55.3,
        timestamp=datetime.utcnow()
    )


# ---------------------------------------------------------
# Telemetry statistics (optional analytics)
# ---------------------------------------------------------
@router.get("/stats", response_model=TelemetryStats)
def get_telemetry_stats(
    query: TelemetryQuery = Depends(),
    # db: Session = Depends(get_db)
):
    # TODO: ORM aggregation
    # Example:
    # q = db.query(...)
    # compute min/max/avg/count

    now = datetime.utcnow()

    return TelemetryStats(
        register_id=query.register_id or 1,
        device_id=query.device_id or 1,
        min_value=10.0,
        max_value=90.0,
        avg_value=42.5,
        sample_count=100,
        start_time=query.start_time or now,
        end_time=query.end_time or now
    )


# ---------------------------------------------------------
# Live telemetry placeholder (WebSocket/SSE)
# ---------------------------------------------------------
@router.get("/live/{register_id}", response_model=TelemetryLive)
def get_live_telemetry(
    register_id: int,
    # db: Session = Depends(get_db)
):
    # TODO: Replace with real streaming or live engine state
    return TelemetryLive(
        register_id=register_id,
        device_id=1,
        value=48.7,
        timestamp=datetime.utcnow(),
        status="ok"
    )
