from fastapi import APIRouter
from models.todos import Todo
from schema.schemas import list_serial
from bson import ObjectId
from config.database import collection_name


router = APIRouter()

#!GET REQUEST METHOD
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


#!POST REQUEST 
@router.post("/")
async def post_todos(todo:Todo):
    collection_name.insert_one(dict(todo))
    

#!PUT REQUEST
@router.put("/{id}")
async def put_todo(id:str, todo:Todo):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})

#!DELETE REQUEST
@router.delete("/{id}")
async def delete_todo(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})