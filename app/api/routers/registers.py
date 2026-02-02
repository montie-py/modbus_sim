from fastapi import APIRouter

from app.api.schemas.register import (
    RegisterCreate,
    RegisterUpdate,
    RegisterRead,
    RegisterValueUpdate
)

# When ORM is added:
# from app.models.register import Register
# from app.database import get_db

router = APIRouter(
    prefix="/registers",
    tags=["registers"]
)


# ---------------------------------------------------------
# Create a register
# ---------------------------------------------------------
@router.post("/", response_model=RegisterRead)
def create_register(
    payload: RegisterCreate,
    # db: Session = Depends(get_db)
):
    # TODO: Replace with ORM logic
    # Example:
    # register = Register(**payload.dict())
    # db.add(register)
    # db.commit()
    # db.refresh(register)
    # return register

    return RegisterRead(
        id=1,
        device_id=payload.device_id,
        address=payload.address,
        type=payload.type,
        value=payload.value,
        description=payload.description,
        created_at=None
    )


# ---------------------------------------------------------
# List registers (optionally filtered by device_id)
# ---------------------------------------------------------
@router.get("/", response_model=list[RegisterRead])
def list_registers(
    device_id: int | None = None,
    # db: Session = Depends(get_db)
):
    # TODO: ORM query
    # query = db.query(Register)
    # if device_id:
    #     query = query.filter(Register.device_id == device_id)
    # return query.all()

    return []


# ---------------------------------------------------------
# Get a single register
# ---------------------------------------------------------
@router.get("/{register_id}", response_model=RegisterRead)
def get_register(
    register_id: int,
    # db: Session = Depends(get_db)
):
    # TODO: ORM lookup
    # register = db.query(Register).filter(Register.id == register_id).first()
    # if not register:
    #     raise HTTPException(404, "Register not found")
    # return register

    return RegisterRead(
        id=register_id,
        device_id=1,
        address=100,
        type="holding",
        value=42.0,
        description="Example register",
        created_at=None
    )


# ---------------------------------------------------------
# Update a register (partial update)
# ---------------------------------------------------------
@router.put("/{register_id}", response_model=RegisterRead)
def update_register(
    register_id: int,
    payload: RegisterUpdate,
    # db: Session = Depends(get_db)
):
    # TODO: ORM update logic
    # register = db.query(Register).filter(Register.id == register_id).first()
    # if not register:
    #     raise HTTPException(404, "Register not found")
    #
    # for key, value in payload.dict(exclude_unset=True).items():
    #     setattr(register, key, value)
    #
    # db.commit()
    # db.refresh(register)
    # return register

    return RegisterRead(
        id=register_id,
        device_id=1,
        address=payload.address or 100,
        type=payload.type or "holding",
        value=payload.value or 42.0,
        description=payload.description or "Updated register",
        created_at=None
    )


# ---------------------------------------------------------
# Write a new value to a register
# ---------------------------------------------------------
@router.post("/{register_id}/write", response_model=RegisterRead)
def write_register_value(
    register_id: int,
    payload: RegisterValueUpdate,
    # db: Session = Depends(get_db)
):
    # TODO: ORM update for value only
    # register = db.query(Register).filter(Register.id == register_id).first()
    # if not register:
    #     raise HTTPException(404, "Register not found")
    #
    # register.value = payload.value
    # db.commit()
    # db.refresh(register)
    # return register

    return RegisterRead(
        id=register_id,
        device_id=1,
        address=100,
        type="holding",
        value=payload.value,
        description="Updated via write endpoint",
        created_at=None
    )


# ---------------------------------------------------------
# Delete a register
# ---------------------------------------------------------
@router.delete("/{register_id}")
def delete_register(
    register_id: int,
    # db: Session = Depends(get_db)
):
    # TODO: ORM delete
    # register = db.query(Register).filter(Register.id == register_id).first()
    # if not register:
    #     raise HTTPException(404, "Register not found")
    #
    # db.delete(register)
    # db.commit()

    return {"message": f"Register {register_id} deleted"}
