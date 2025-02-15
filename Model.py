from pydantic import BaseModel
from fastapi.exceptions import HTTPException
class UserInfo(BaseModel):
    user_name: str
    gender: bool
    phone_number: str | None = None
    full_name: str
    age: int

class UpdateInfo(BaseModel):
    new_user_name: str | None = None
    new_gender: bool | None = None
    new_phone_number: str | None = None
    new_full_name: str | None = None
    new_age: int | None = None
class User:
    def __init__(self, user_name: str, gender: bool, phone_number: str , full_name: str, age: int):
        self.user_name = user_name
        self.gender = gender
        self.full_name = full_name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        item = UserInfo
        item.user_name = self.user_name
        item.gender = self.gender
        item.phone_number = self.phone_number
        item.full_name = self.full_name
        item.age = self.age
        return item

class Manage:
    def __init__(self):
        self.list_users = list()
        self.existed = dict()

    def add_user(self, user_info: UserInfo):
        if self.existed.get(user_info.user_name):
            raise HTTPException(status_code=200, detail=f"username {user_info.user_name} is existed")
        new_user = User(user_info.user_name, user_info.gender, user_info.phone_number, user_info.full_name, user_info.age)
        self.list_users.append(new_user)
        self.existed[new_user.user_name] = True
        return {"message": f"added user {new_user.user_name}"}

    def del_user(self, user_name: str):
        for user in self.list_users:
            if user_name == user.user_name:
                self.list_users.remove(user)
                self.existed.pop(user_name)
                return {"message": f"deleted user {user_name}"}
        raise HTTPException(status_code=404, detail="Not Found")

    def update_user(self, user_name, new_info: UpdateInfo):
        for user in self.list_users:
            if user_name == user.user_name:
                if new_info.new_user_name:
                    user.user_name = new_info.new_user_name
                    self.existed.pop(user_name)
                    self.existed[new_info.new_user_name] = True
                if new_info.new_full_name:
                    user.full_name = new_info.new_full_name
                if new_info.new_phone_number:
                    user.phone_number = new_info.new_phone_number
                if new_info.new_age:
                    user.age = new_info.new_age
                return {"message": "Updated"}
        raise HTTPException(status_code=404, detail=f"Not found user name {user_name}")

    def get_all_users(self):
        result = list()
        for user in self.list_users:
            result.append(user)
        return result

    def search_by_user_name(self, user_name: str):
        result = list()
        for user in self.list_users:
            if user_name in user.user_name:
                result.append(user)
        if len(result) == 0:
            raise HTTPException(status_code=404, detail="Not found")
        return result

    def search_by_name(self, name: str):
        result = list()
        for user in self.list_users:
            if name in user.full_name:
                result.append(user)
        if len(result) == 0:
            raise HTTPException(status_code=404, detail="Not found")
        return result

    def search_by_gender_and_age(self, gender, age):
        result = list()
        for user in self.list_users:
            if user.age == age and user.gender == gender:
                result.append(user)
        if len(result) == 0:
            raise HTTPException(status_code=404, detail="Not found")
        return result