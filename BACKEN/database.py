# Autor: Diego Galviz
# Fecha: 19/07/2021
# Version: v1
# Descripcion: Conexion a la base de datos

# importacion de librerias

from motor.motor_asyncio import AsyncIOMotorClient
from models import Task
from bson import ObjectId

# conexion
client = AsyncIOMotorClient('mongodb://localhost:27017')
# creacion de la base de datos
database = client.taskdatabese
# creacion de la coleccion
collections = database.tasks


# funciones de la base de datos

async def get_one_task_id(id):
    task = await collections.find_one({'_id': ObjectId(id)})
    return task


async def get_one_task(title):
    task = await collections.find_one({'title': title})
    return task


async def get_tasks():
    task = []
    cursor = collections.find({})
    async for documento in cursor:
        task.append(Task(**documento))

    return task


async def create_task(task):
    new_task = await collections.insert_one(task)
    created_task = await collections.find_one({'_id': new_task.inserted_id})
    return created_task


async def update_task(id: str, data):
    task = {k: v for k, v in data.dict().items() if v is not None}
    print(task)
    await collections.update_one({'_id': ObjectId(id)}, {'$set': task})
    document = await collections.find_one({'_id': ObjectId(id)})
    return document


async def delete_task(id: str):
    await collections.delete_one({'_id': ObjectId(id)})
    document = await collections.find_one({'_id': id})
    return True
