from fastapi import FastAPI, HTTPException
from database import get_tasks, create_task, update_task, delete_task, get_one_task_id
from models import Task

app = FastAPI()


@app.get("/")
def welcome():
    return {"message": "Welcome to FastAPI"}


@app.get('/api/tasks')
async def all_tasks():
    tasks = await get_tasks()
    return tasks


@app.post('/api/tasks', response_model=Task)
async def new_task(task: Task):
    response = await create_task(task.dict())
    if response:
        return response

    raise HTTPException(400, 'Something went wrong')



@app.get('/api/tasks/{id}')
async def get_task():
    return 'single task'


@app.put('/api/tasks/{id}')
async def update_tasks():
    return 'task updated'


@app.delete('/api/tasks/{id}')
async def delete_tasks():
    return 'task deleted'
