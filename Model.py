
class User:
    def __init__(self, user_name: str, pass_word: str):
        self.user_name = user_name
        self.pass_word = pass_word
      #  self.phone_number = phone_number

    def __str__(self):
        return f"{self.user_name};{self.pass_word}"

class Manage:
    def __init__(self, list_users: list):
        self.list_users = list_users
    def add_user(self, user: User):
        self.list_users.append(user)
    def del_user(self, user_name: str):
        pass
    def get_all_users(self):
        result = ""
        for user in self.list_users:
            result = result + str(user)
            result = result + "|"
        return result
