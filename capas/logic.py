class User:
    def __init__(self, name, cc, telephone, id_user):
        self.name = name
        self.cc = cc
        self.telephone = telephone
        self.id_user = id_user

    def __str__(self):
        return f"ID: {self.id_user}, Nombre: {self.name}, CC: {self.cc}, Teléfono: {self.telephone}"

class UserService:
    def __init__(self, user_data):
        self.user_data = user_data

    def create_User(self, name, cc, telephone):
        id_user = self.user_data.generar_id()
        user = User(name, cc, telephone, id_user)
        self.user_data.add_User(user)
        return user
    
    def list_User(self):
        return self.user_data.obtain_User()