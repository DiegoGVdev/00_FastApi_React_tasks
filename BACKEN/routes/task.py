from fastapi import APIRouter, HTTPException
from database import get_tasks, create_task, update_task, delete_task, get_one_task_id, get_one_task
from models import Task, UpdateTask

task = APIRouter()


@task.get('/api/tasks')
async def all_tasks():
    tasks = await get_tasks()
    return tasks


@task.post('/api/tasks', response_model=Task)
async def new_task(task: Task):
    taskFound = await get_one_task(task.title)
    if taskFound:
        raise HTTPException(400, 'Task already exist')
    response = await create_task(task.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong')


@task.get('/api/tasks/{id}', response_model=Task)
async def get_task(id: str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f'Task not found with id {id}')


@task.put('/api/tasks/{id}', response_model=Task)
async def put_tasks(id: str, task: UpdateTask):
    response = await update_task(id, task)
    if response:
        return response
    return HTTPException(404, f'Task not found with id {id}')


@task.delete('/api/tasks/{id}')
async def remove_tasks(id: str):
    task = await get_one_task_id(id)
    if task:
        responese = await delete_task(id)
        if responese:
            return "task deleted successfully"
    raise HTTPException(404, f'Task not found with id {id}')
