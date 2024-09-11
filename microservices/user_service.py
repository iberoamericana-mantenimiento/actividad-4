# Class for User Service
class UserService:
    def __init__(self):
        self.users = list()

    def get(self, user_id):
        result = None
        for user in self.users:
            if user.id == user_id:
                result = user
                break
        return result
    
    def create(self, user):
        self.users.append(user)

    def update(self, user_id, user):
        for i, user in enumerate(self.users):
            if user.id == user_id:
                self.users[i] = user
                break
    
    def delete(self, user_id):
        for i, user in enumerate(self.users):
            if user.id == user_id:
                self.users.pop(i)
                break
