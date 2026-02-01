from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from api.app.database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False, unique=True)
    port = Column(Integer, nullable=False)
    update_interval = Column(Float, nullable=False, default=1.0)
    strategy = Column(String, nullable=False, default="random")
    description = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to registers
    registers = relationship(
        "Register",
        back_populates="device",
        cascade="all, delete-orphan"
    )
