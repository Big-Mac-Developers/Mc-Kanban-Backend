from pydantic import BaseModel
from enum import Enum
from datetime import datetime

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
    id: int
    completion_date: datetime

class Subtask(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    main_task_id: int
    assigned_date: datetime
    due_date: datetime
    completed_date: datetime
