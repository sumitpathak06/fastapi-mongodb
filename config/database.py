from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:test1234@cluster0.4bp93an.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]


