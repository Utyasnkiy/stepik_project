from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.config import load_config
from app.logger import logger
from app.models import User, FeedBack


config = load_config()

app = FastAPI()

if config.debug:
    app.debug = True
else:
    app.debug = False

fake_db = [
    {"username": "vasya", "user_info": "любит колбасу"},
    {"username": "katya", "user_info": "любит петь"}
]


@app.get('/user/{username}')
async def get_user(username: str):
    for user in  fake_db:
        if user['username'] == username:
            return user
    return {"Erorr":"User not found"}


@app.get('/users')
async def get_users(limit: int = 10):
    return fake_db[:limit]


@app.post('/user_add')
async def add_user(user: User):
    try:
        fake_db.append(user)
        return {"status": "Ok"}
    except:
        return {"massage": "user not add"} 
    
feedback_data = []
@app.post('/add_feedback')
async def add_feedback(feedback: FeedBack):
    feedback_data.append(feedback)
    return {"status": f'Thx {feedback.name}'}


@app.get('/feedback')
async def get_feedback():
    return feedback_data