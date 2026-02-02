from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)

    device_id = Column(Integer, ForeignKey("devices.id", ondelete="CASCADE"), nullable=False)
    register_id = Column(Integer, ForeignKey("registers.id", ondelete="CASCADE"), nullable=False)

    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)

    # ORM relationships
    device = relationship("Device", back_populates="telemetry")
    register = relationship("Register", back_populates="telemetry")
