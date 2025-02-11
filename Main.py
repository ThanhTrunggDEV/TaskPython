from fastapi import FastAPI
from fastapi.security import HTTPAuthorizationCredentials
from pydantic import BaseModel
from Model import User, Manage

app = FastAPI()
manage = Manage([])
@app.get("/get_user/{user_name}")
async def get_user(user_name:str):
    for user in manage.list_users:
        if user.user_name == user_name :
            return f"{user.user_name} | {user.pass_word}"
    return f"Not Found {user_name}"

@app.get("/get_full_user/")
async def get_full_user():
    return f"{manage.get_all_users()}"

@app.put("/create_user/{user_name};{pass_word}")
async def create_us(user_name: str, pass_word: str):
    new_user = User(user_name, pass_word)
    manage.add_user(new_user)