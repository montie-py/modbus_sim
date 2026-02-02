from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Register(Base):
    __tablename__ = "registers"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id", ondelete="CASCADE"), nullable=False)

    address = Column(Integer, nullable=False, index=True)
    type = Column(String, nullable=False)  # holding | input | coil | discrete
    value = Column(Float, nullable=False)
    description = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Device
    device = relationship("Device", back_populates="registers")
