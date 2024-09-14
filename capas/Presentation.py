class UserView:
    def __init__(self, user_service):
        self.user_service = user_service

    def show_menu(self):
        while True:
            print("\n1. Crear un Nuevo usuario")
            print("2. Listar usuarios")
            print("3. Salir")
            option = input("Seleccione una opción: ")

            if option == "1":
                self.create_user()
            elif option == "2":
                self.list_users()
            elif option == "3":
                break
            else:
                print("Opción no válida")

    def create_user(self):
        name = input("Ingrese el Nombre del Usuario: ")
        document = input("Ingrese el Número de Cédula del Usuario: ")
        phone = input("Ingrese el Número de Teléfono del Usuario: ")
        user = self.user_service.create_user(name, document, phone)
        print(f"Usuario creado correctamente: {user}")
    
    def list_users(self):
        users = self.user_service.list_users()
        if users:
            for user in users:
                print(user)
        else:
            print("No hay usuarios registrados.")