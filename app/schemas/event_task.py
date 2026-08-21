from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.event_task import TaskStatus, TaskPriority

class EventTaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: Optional[datetime] = None
    assignee_id: Optional[int] = None

class EventTaskCreate(EventTaskBase):
    pass

class EventTaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None
    assignee_id: Optional[int] = None

class EventTaskResponse(EventTaskBase):
    id: int
    event_id: int
    created_at: datetime

    model_config = {"from_attributes": True}
