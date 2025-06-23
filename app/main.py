from fastapi import FastAPI, Path, HTTPException
from schemas.tasks_schema import BaseTask, Status
from datetime import datetime
from typing import Annotated
from json import loads
from uuid import uuid4, UUID

app = FastAPI()

tasks = {}

@app.get("/")
async def root():
    raise HTTPException(
        status_code=200,
        detail="Welcome home:)"
    ) 

@app.get("/tasks/{task_id}")
async def read_task(task_id: UUID):
    if task_id not in tasks:
        raise HTTPException(
        status_code=404,
        detail=f"Task with ID {task_id} Not Found"
        )
    raise HTTPException(
        status_code=200,
        detail={"task": tasks[task_id]}
    ) 
   

@app.post("/tasks/")
async def create_task(task: BaseTask):
    new_task_id = uuid4()
    new_task = {
        "task_id": new_task_id,
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
    raise HTTPException(
        status_code=200,
        detail={"message": "Task Successfully Created:)", "task": new_task}
    )

@app.put("/tasks/{task_id}")
async def update_task(task_id: UUID, task: BaseTask):
    if task_id not in tasks:
        raise HTTPException(
        status_code=404,
        detail=f"Task with ID {task_id} Not Found"
        )
    task_values = loads(tasks[task_id])
    if task.status == Status.DONE: # Handle complete task status update
        updated_task = {
            "task_id": task_values["task_id"],
            "title": task.title or task_values["title"],
            "description": task.description or task_values["description"],            
            "status": task.status or task_values["status"],            
            "priority": task.priority or task_values["priority"],            
            "category": task.category or task_values["category"],                 
            "due_date": task.due_date or task_values["due_date"],
            "created_at": task_values["created_at"],
            "completed_at": datetime.now().date(),                           
            "partner_id": task.partner_id or task_values["partner_id"]            
        }
    else:
        updated_task = {
            "task_id": task_values["task_id"],
            "title": task.title or task_values["title"],
            "description": task.description or task_values["description"],            
            "status": task.status or task_values["status"],            
            "priority": task.priority or task_values["priority"],            
            "category": task.category or task_values["category"],                 
            "due_date": task.due_date or task_values["due_date"],
            "created_at": task_values["created_at"],
            "completed_at": None,                           
            "partner_id": task.partner_id or task_values["partner_id"]
        }
    tasks[task_id] = updated_task
    raise HTTPException(
        status_code=200,
        detail= {"message": "Successfully updated task {task_id}", "new_task": updated_task}
    )

@app.get('/tasks/')
async def get_tasks():
    raise HTTPException(
        status_code=200,
        detail=tasks
    )

@app.delete('/tasks/{task_id}')
async def delete_task(task_id: UUID):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail=f"Unable to delete task with ID {task_id}, task not exist"
        )
    del tasks[task_id]
    raise HTTPException(
        status_code=200,
        detail={"message": f"Successfully delete task {task_id}"}
    )
    
# TODO: write tests for each crud operation in the tasks category
# TODO: implement a router for tasks
# TODO: move tasks creation, deletion, update etc to db folder, using db function (even if the db is a dict right now)
