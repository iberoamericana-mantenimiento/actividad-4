class UserData:

    # Constructor de la clase
    def __init__(self):
        self.users = []
        self.counter = 1
    
    def add_user(self, user):
        self.users.append(user)
    
    def get_users(self):
        return self.users
    
    def generate_user_id(self):
        id_actual = self.counter
        self.counter += 1
        return id_actual