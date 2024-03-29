from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from routes.route import router

app = FastAPI()
app.include_router(router)

uri = "mongodb+srv://admin:test1234@cluster0.4bp93an.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)