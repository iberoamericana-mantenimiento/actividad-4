class User:
    # Constructor
    def __init__(self, name, document, phone, user_id):
        self.name = name
        self.document = document
        self.phone = phone
        self.user_id = user_id

    # Método para mostrar los datos de un usuario
    def __str__(self):
        return f"ID: {self.user_id}, Nombre: {self.name}, Documento: {self.document}, Teléfono: {self.phone}"

class UserService:
    # Constructor
    def __init__(self, user_data):
        self.user_data = user_data

    def create_user(self, name, document, phone):
        user_id = self.user_data.generate_user_id()
        user = User(name, document, phone, user_id)
        self.user_data.add_user(user)
        return user
    
    def list_users(self):
        return self.user_data.get_users()