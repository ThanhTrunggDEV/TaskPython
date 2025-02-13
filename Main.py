from typing import Annotated
from fastapi import FastAPI, Response,status
from fastapi.params import Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from Model import Manage, UserInfo, UpdateInfo


app = FastAPI()
security = HTTPBasic()
USERNAME = "admin"
PASSWORD = "test"
manage = Manage()

def authen(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if credentials.username == USERNAME and credentials.password == PASSWORD:
        return True
    return False

@app.get("/get_user/{user_name}")
def get_user(user_name:str, isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"Message": "Access Denied"}
    for user in manage.list_users:
        if user.user_name == user_name:
            return user
    return {"message" : f"Not Found {user_name}"}

@app.delete("/del_user/{user_name}")
def del_user(user_name: str, isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"Message": "Access Denied"}
    return manage.del_user(user_name)

@app.get("/get_full_user/")
def get_full_user(isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"message": "Access Denied"}
    return manage.get_all_users()

@app.post("/create_user/")
def create_user(user_info: UserInfo, isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"message": "Access Denied"}
    return manage.add_user(user_info)

@app.put("/update_user/{user_name}")
def update_user(user_name: str, new_info: UpdateInfo, isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"message": "Access Denied"}
    return manage.update_user(user_name, new_info)

