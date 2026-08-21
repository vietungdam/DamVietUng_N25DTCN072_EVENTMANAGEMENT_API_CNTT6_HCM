import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.database import Base
from enum import Enum

class StaffRole(str, Enum):
    OWNER = "OWNER"
    MEMBER = "MEMBER"

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    owner = relationship("User", back_populates="events_owned")
    staff = relationship("EventStaff", back_populates="event", cascade="all, delete-orphan")
    tasks = relationship("EventTask", back_populates="event", cascade="all, delete-orphan")

class EventStaff(Base):
    __tablename__ = "event_staff"

    event_id = Column(Integer, ForeignKey("events.id"), primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    role = Column(String(50), nullable=False)  # OWNER / MEMBER
    joined_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    event = relationship("Event", back_populates="staff")
    user = relationship("User", back_populates="staff_roles")

    __table_args__ = (UniqueConstraint('event_id', 'user_id', name='uq_event_user'),)