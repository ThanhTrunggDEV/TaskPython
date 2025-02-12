from pydantic import BaseModel

class UserInfo(BaseModel):
    user_name: str
    pass_word: str
    phone_number: str | None = None
    full_name: str
    age: int
class SearchInfo(BaseModel):
    user_name: str | None = None
    full_name: str | None = None

class UpdateInfo(BaseModel):
    new_user_name: str | None = None
    new_pass_word: str | None = None
    new_phone_number: str | None = None
    new_full_name: str | None = None

class User:
    def __init__(self, user_name: str, pass_word: str, phone_number: str , full_name: str, age: int):
        self.user_name = user_name
        self.pass_word = pass_word
        self.full_name = full_name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        item = UserInfo
        item.user_name = self.user_name
        item.pass_word = self.pass_word
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
            return {"message": f"username {user_info.user_name} is existed"}
        new_user = User(user_info.user_name, user_info.pass_word, user_info.phone_number, user_info.full_name, user_info.age)
        self.list_users.append(new_user)
        self.existed[new_user.user_name] = True
        return {"message": f"added user {new_user.user_name}"}
    def del_user(self, user_name: str):
        for user in self.list_users:
            if user_name == user.user_name:
                self.list_users.remove(user)
                self.existed.pop(user_name)
                return {"message": f"deleted user {user_name}"}
        return {"message": f"Not Found user {user_name}"}
    def update_user(self, user_name, new_info: UpdateInfo):
        for user in self.list_users:
            if user_name == user.user_name:
                if new_info.new_user_name:
                    user.user_name = new_info.new_user_name
                    self.existed.pop(user_name)
                    self.existed[new_info.new_user_name] = True
                if new_info.new_pass_word:
                    user.pass_word = new_info.new_pass_word
                if new_info.new_full_name:
                    user.full_name = new_info.new_full_name
                if new_info.new_phone_number:
                    user.phone_number = new_info.new_phone_number
                return {"message": "Updated"}
        return {"message": f"Not Found user {user_name}"}

    def get_all_users(self):
        result = list()
        for user in self.list_users:
            result.append(user)
        return result
    def search(self):
        pass