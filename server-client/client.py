# Para este ejemplo nuestro cliente será la consola de comandos de Python
# en un proyecto real se debe tener un cliente que se comunique con el servidor
# por ejemplo un cliente web o una aplicación de escritorio

from server import Server

class Client:

    def __init__(self):
        self.server = Server()

    def show_menu(self):
        print("1. Ver productos")
        print("2. Ver precios")
        print("3. Ver precio de un producto")
        print("4. Salir")
        input_option = input("Seleccione una opción: ")
        return input_option
    
    def show_products(self):
        products = self.server.get_products()
        for product in products:
            print(product)

    def show_prices(self):
        prices = self.server.get_prices()
        for product, price in prices.items():
            print(f"{product}: {price}")

    def show_price(self):
        product = input("Ingrese el producto: ")
        price = self.server.get_price(product)
        print(price)