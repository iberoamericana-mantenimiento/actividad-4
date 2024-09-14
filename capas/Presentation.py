class UserVist:
    def __init__(self, user_service):
        self.user_service = user_service

    def mostrar_menu(self):
        while True:
            print("\n1. Crear un Nuevo usuario")
            print("2. Listar usuarios")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.create_User()
            elif opcion == "2":
                self.list_User()
            elif opcion == "3":
                break
            else:
                print("Opción no válida")

    def create_User(self):
        name = input("Ingrese el Nombre del Usuario: ")
        cc = input("Ingrese el Número de Cédula del Usuario: ")
        telephone = input("Ingrese el Número de Teléfono del Usuario: ")
        user = self.user_service.create_User(name, cc, telephone)
        print(f"Usuario creado correctamente: {user}")
    
    def list_User(self):
        users = self.user_service.list_User()
        if users:
            for user in users:
                print(user)
        else:
            print("No hay usuarios registrados.")