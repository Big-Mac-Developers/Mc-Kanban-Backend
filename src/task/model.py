from typing import Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from uuid import UUID

class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class Maintask_initial(BaseModel):
    title: str
    description: str
    status: TaskStatus
    due_date: datetime
    board_id: int

class Maintask(Maintask_initial):
    id: UUID
    completion_date: datetime

class Subtask_initial(BaseModel):
    title: str
    description: str
    status: TaskStatus
    main_task_id: UUID
class Subtask(Subtask_initial):
    id: UUID
    assignee: str
    assigned_date: datetime
    completed_date: datetime
