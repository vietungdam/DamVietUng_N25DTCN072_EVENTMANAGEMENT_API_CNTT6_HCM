from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from app.models.event import StaffRole

class EventBase(BaseModel):
    name: str
    description: Optional[str] = None

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class EventResponse(EventBase):
    id: int
    owner_id: int
    created_at: datetime

    model_config = {"from_attributes": True}

class EventStaffBase(BaseModel):
    user_id: int
    role: StaffRole

class EventStaffCreate(EventStaffBase):
    pass

class EventStaffResponse(EventStaffBase):
    event_id: int
    joined_at: datetime

    model_config = {"from_attributes": True}
