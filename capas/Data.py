class UserData:
    def __init__(self):
        self.users = []
        self.counter = 1
    
    def add_User(self, user):
        self.users.append(user)
    
    def obtain_User(self):
        return self.users
    
    def generar_id(self):
        id_actual = self.counter
        self.counter += 1
        return id_actual