from client import Client

client = Client()

while True:
    option = client.show_menu()
    if option == "1":
        client.show_products()
    elif option == "2":
        client.show_prices()
    elif option == "3":
        client.show_price()
    elif option == "4":
        break
    else:
        print("Opción inválida")