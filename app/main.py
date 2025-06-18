from fastapi import FastAPI, Path
from schemas.tasks_schema import TaskCreate as NewTask
from datetime import datetime
from typing import Annotated
app = FastAPI()

tasks = {}

@app.get("/")
async def root():
    return {"message": "Welcome Home:)"}

@app.get("/tasks/{task_id}")
async def read_task(task_id: int):  # 
    if tasks[task_id] is not None:
        return tasks[task_id]
    return {"message": "Task Not Found:("}

@app.post("/tasks/")
async def create_task(task: NewTask):
    new_task_id: int = len(tasks) + 1
    new_task = {
        "id": new_task_id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority": task.priority,
        "category": task.category,
        "due_date": task.due_date,
        "created_at": datetime.now().isoformat(),  # Example date
        "completed_at": None,  # Initially None
        "assigned_to": task.assigned_to
    }
    tasks[new_task_id] = new_task
    return {"message": "Task Successfully Created:)", "task_id": new_task_id, "task": new_task}

# TODO: implement update task, delete task, and get all tasks
# TODO: when delete, update or get task, check if task exists
# TODO: write tests for each crud operation in the tasks category
# TODO: implement a router for tasks

# TODO: