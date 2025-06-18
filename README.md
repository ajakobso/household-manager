# household-manager

to install dependencies for this project please run:
```poetry install --no-root```  
to run the webserver run the following commands:
```cd app```  
```uvicorn main:app --reload```  

now you can access the server at http://127.0.0.1:8000/


current available operations are:
[get task](http://127.0.0.1:8000/tasks/{task_id})  
create task using post request to [create task](http://127.0.0.1:8000/tasks/) with the following example json:
```
{
    "title": "do the dishes",
    "description": "wash the beshari dishes left in the sink",
    "status": "Pending",
    "priority": null,
    "due_date": null,
    "assigned_to": null
}
```