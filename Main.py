from fastapi import FastAPI, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBasic
from pydantic import BaseModel
from Model import User, Manage, Item

app = FastAPI()
manage = Manage([])
@app.get("/get_user/{user_name}")
async def get_user(user_name:str):
    for user in manage.list_users:
        if user.user_name == user_name:
            return user
    return f"Not Found {user_name}"

@app.delete("/del_user/{user_name}")
async def del_user(user_name: str):
   return manage.del_user(user_name)

@app.get("/get_full_user/")
async def get_full_user():
    return manage.get_all_users()

@app.post("/create_user/")
async def create_us(user_info: Item):
    new_user = User(user_info.user_name, user_info.pass_word, user_info.phone_number, user_info.full_name)
    manage.add_user(new_user)
    return user_info