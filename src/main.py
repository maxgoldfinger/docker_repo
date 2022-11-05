from fastapi import FastAPI
from pydantic import BaseModel
from .mongo_manager import MongoManager, Photo
import datetime

app = FastAPI()

class Msg(BaseModel):
    msg: str

mongo_manager = MongoManager()


@app.get("/")
async def root():
    return {"message": "API home page!"}


@app.get("/time")
async def function_demo_get():
    return {
        "message": f"It's {datetime.datetime.now().time()}"
    }


@app.get("/get_photo")
async def function_demo_get():
    return mongo_manager.get()

@app.get("/load_photo")
async def function_demo_get():
    return mongo_manager.add(Photo(url="https://some_photo_url"))