from email.policy import default
from typing import Annotated
from fastapi import FastAPI, Response,status
from fastapi.params import Header, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from Model import User, Manage, UserInfo, UpdateInfo

app = FastAPI()
security = HTTPBasic()
USERNAME = "admin"
PASSWORD = "test"
manage = Manage([])

def authen(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if credentials.username == USERNAME and credentials.password == PASSWORD:
        return True
    return False

@app.get("/get_user/{user_name}")
async def get_user(user_name:str, Authen: Annotated[None, Depends(authen)]):
    if not Authen:
        return {"Message": "Access Denied"}
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
async def create_us(user_info: UserInfo):
    new_user = User(user_info.user_name, user_info.pass_word, user_info.phone_number, user_info.full_name)
    manage.add_user(new_user)
    return user_info

@app.put("/update_user/{user_name}")
async def update_user(user_name: str, new_info: UpdateInfo):
    return manage.update_user(user_name, new_info)

