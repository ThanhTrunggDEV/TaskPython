from pydantic import BaseModel


class Item(BaseModel):
    user_name: str
    pass_word: str
    phone_number: str | None = None
    full_name: str


class User:
    def __init__(self, user_name: str, pass_word: str, phone_number: str , full_name: str):
        self.user_name = user_name
        self.pass_word = pass_word
        self.full_name = full_name
        self.phone_number = phone_number

    def __str__(self):
        item = Item
        item.user_name = self.user_name
        item.pass_word = self.pass_word
        item.phone_number = self.phone_number
        item.full_name = self.full_name
        return item

class Manage:
    def __init__(self, list_users: list):
        self.list_users = list_users
    def add_user(self, user: User):
        self.list_users.append(user)
    def del_user(self, user_name: str):
        for user in self.list_users:
            if user_name == user.user_name:
                self.list_users.remove(user)
                return True
        return False
    def get_all_users(self):
        result = list()
        for user in self.list_users:
            result.append(user)
        return result
