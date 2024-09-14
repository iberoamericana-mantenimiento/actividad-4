#Ejecución de capas para creación de usuarios con nombre, cedula, telefono para una base.

from Data import UserData
from logic import UserService
from Presentation import UserVist

if __name__ == "__main__":
    Data = UserData()
    logic = UserService(Data)
    Presentation = UserVist(logic) 
    Presentation.mostrar_menu()

