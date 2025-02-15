
from typing import Annotated
from fastapi import FastAPI, Response,status
from fastapi.params import Depends, Query
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from fastapi.exceptions import HTTPException
from Model import Manage, UserInfo, UpdateInfo


app = FastAPI()
security = HTTPBasic()
USER_NAME = "admin"
PASS_WORD = "test"
manage = Manage()

def authen(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if credentials.username == USER_NAME and credentials.password == PASS_WORD:
        return True
    return False

@app.get("/get_user_by_username/")
def get_user(username: str, isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"Message": "Access Denied"}
    return manage.search_by_user_name(username)

@app.get("/get_user_by_name/")
def get_user(name: str, isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"Message": "Access Denied"}
    return manage.search_by_name(name)

@app.get("/get_user_by_gender_and_age/")
def get_user(gender: bool, age: int, isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"Message": "Access Denied"}
    return manage.search_by_gender_and_age(gender, age)

@app.delete("/del_user/{user_name}")
def del_user(user_name: str, isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"Message": "Access Denied"}
    return {"data": manage.del_user(user_name)}

@app.get("/get_full_user/")
def get_full_user(isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"message": "Access Denied"}
    return {"data": manage.get_all_users()}

@app.post("/create_user/", status_code=status.HTTP_201_CREATED)
def create_user(user_info: UserInfo, isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"message": "Access Denied"}
    return manage.add_user(user_info)

@app.put("/update_user/{user_name}")
def update_user(user_name: str, new_info: UpdateInfo, isCorrect: Annotated[bool, Depends(authen)]):
    if not isCorrect:
        return {"message": "Access Denied"}
    return manage.update_user(user_name, new_info)

