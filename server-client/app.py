import os
from client import Client

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

client = Client()

while True:
    clear_console()
    option = client.show_menu()
    if option == "1":
        clear_console()
        client.create_product()
    elif option == "2":
        clear_console()
        client.update_product()
    elif option == "3":
        clear_console()
        client.show_products()
    elif option == "4":
        clear_console()
        client.show_prices()
    elif option == "5":
        clear_console()
        client.show_price()
    elif option == "6":
        clear_console()
        client.delete_product()
    elif option == "7":
        break
    else:
        print("Opción inválida")
    input("Presiona Enter para continuar...")