from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from api.api.app.schemas.values import (
    RegisterValue,
    RegisterValueWrite,
    RegisterValueBatch,
    RegisterValueWriteBatch,
    RegisterValueWriteItem
)

# When ORM is added:
# from app.models.register import Register
# from app.database import get_db

router = APIRouter(
    prefix="/values",
    tags=["values"]
)

# ---------------------------------------------------------
# Read a single register value
# ---------------------------------------------------------
@router.get("/{register_id}", response_model=RegisterValue)
def read_register_value(
    register_id: int,
    # db: Session = Depends(get_db)
):
    # TODO: ORM lookup
    # register = db.query(Register).filter(Register.id == register_id).first()
    # if not register:
    #     raise HTTPException(404, "Register not found")

    return RegisterValue(
        register_id=register_id,
        device_id=1,
        value=42.0,
        timestamp=datetime.utcnow()
    )


# ---------------------------------------------------------
# Write a single register value
# ---------------------------------------------------------
@router.post("/{register_id}", response_model=RegisterValue)
def write_register_value(
    register_id: int,
    payload: RegisterValueWrite,
    # db: Session = Depends(get_db)
):
    # TODO: ORM update
    # register = db.query(Register).filter(Register.id == register_id).first()
    # if not register:
    #     raise HTTPException(404, "Register not found")
    #
    # register.value = payload.value
    # db.commit()
    # db.refresh(register)

    return RegisterValue(
        register_id=register_id,
        device_id=1,
        value=payload.value,
        timestamp=datetime.utcnow()
    )


# ---------------------------------------------------------
# Batch read values
# ---------------------------------------------------------
@router.get("/", response_model=RegisterValueBatch)
def read_values_batch(
    device_id: int | None = None,
    # db: Session = Depends(get_db)
):
    # TODO: ORM query
    # q = db.query(Register)
    # if device_id:
    #     q = q.filter(Register.device_id == device_id)
    # registers = q.all()

    values = [
        RegisterValue(
            register_id=1,
            device_id=device_id or 1,
            value=55.0,
            timestamp=datetime.utcnow()
        )
    ]

    return RegisterValueBatch(values=values, count=len(values))


# ---------------------------------------------------------
# Batch write values
# ---------------------------------------------------------
@router.post("/batch", response_model=RegisterValueBatch)
def write_values_batch(
    payload: RegisterValueWriteBatch,
    # db: Session = Depends(get_db)
):
    # TODO: ORM batch update
    # updated = []
    # for item in payload.writes:
    #     register = db.query(Register).filter(Register.id == item.register_id).first()
    #     if not register:
    #         continue
    #     register.value = item.value
    #     updated.append(register)
    # db.commit()

    updated_values = [
        RegisterValue(
            register_id=item.register_id,
            device_id=1,
            value=item.value,
            timestamp=datetime.utcnow()
        )
        for item in payload.writes
    ]

    return RegisterValueBatch(values=updated_values, count=len(updated_values))
