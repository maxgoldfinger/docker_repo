from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI()


class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to the API home page!"}


@app.get("/time")
async def function_demo_get():
    return {
        "message": f"It's {datetime.datetime.now().time()}"
    }

# !uvicorn main:app --reload