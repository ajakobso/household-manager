from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str  # e.g., 'pending', 'in_progress', 'completed'
    priority: int | None  # e.g., 1 for high, 2 for medium, 3 for low
    category: str | None # e.g 'routine maintenance', 'long-term improvements', 'urgent maintenance' etc
    due_date: str | None # ISO format date string, e.g., '2023-10-01'
    created_at: str  # ISO format date string, e.g., '2023-10-01T12:00:00Z'
    completed_at: str | None  # ISO format date string, e.g., '2023-10-01T12:00:00Z' or None if not completed
    assigned_to: int | None  # ID of the user the task is assigned to

class TaskCreate(BaseModel):
    title: str
    description: str
    status: str  # e.g., 'pending', 'in_progress', 'completed'
    priority: int | None  # e.g., 1 for high, 2 for medium, 3 for low
    category: str | None  # e.g 'routine maintenance', 'long-term improvements', 'urgent maintenance' etc
    due_date: str | None  # ISO format date string, e.g., '2023-10-01'
    assigned_to: int | None  # ID of the user the task is assigned to