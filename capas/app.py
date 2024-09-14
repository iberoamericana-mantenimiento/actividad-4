#Ejecución de capas para creación de usuarios con nombre, cedula, telefono para una base.

from data import UserData
from logic import UserService
from presentation import UserView

if __name__ == "__main__":
    data = UserData()
    logic = UserService(data)
    presentation = UserView(logic) 
    presentation.show_menu()

