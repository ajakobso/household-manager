from fastapi import FastAPI, Path
from schemas.tasks_schema import BaseTask
from datetime import datetime
from typing import Annotated
app = FastAPI()

tasks = {}

@app.get("/")
async def root():
    return {"message": "Welcome Home:)"}

@app.get("/tasks/{task_id}")
async def read_task(task_id: int):  # 
    if task_id in tasks:
        return tasks[task_id]
    return {"message": "Task Not Found:("}

@app.post("/tasks/")
async def create_task(task: BaseTask):
    new_task_id: int = len(tasks) + 1
    new_task = {
        "id": new_task_id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority": task.priority,
        "category": task.category,
        "due_date": task.due_date,
        "created_at": datetime.now().date(),  # Example date
        "completed_at": None,  # Initially None
        "partner_id": task.partner_id
    }
    tasks[new_task_id] = new_task
    return {"message": "Task Successfully Created:)", "task_id": new_task_id, "task": new_task}

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: BaseTask):
    if task_id in tasks:
        updated_task = {

        }
    return {"message": "Unable to update non-existing task"}
    
# TODO: implement update task, delete task, and get all tasks
# TODO: when delete, update or get task, check if task exists
# TODO: write tests for each crud operation in the tasks category
# TODO: implement a router for tasks
