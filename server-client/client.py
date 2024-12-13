# Para este ejemplo nuestro cliente será la consola de comandos de Python
# en un proyecto real se debe tener un cliente que se comunique con el servidor
# por ejemplo un cliente web o una aplicación de escritorio

from server import Server

class Client:

    def __init__(self):
        self.server = Server()

    def show_menu(self):
        print("1. Crear producto")
        print("2. Editar producto")
        print("3. Ver productos")
        print("4. Ver precios")
        print("5. Ver precio de un producto")
        print("6. Eliminar producto")
        print("7. Salir")
        input_option = input("Seleccione una opción: ")
        return input_option
    
    def create_product(self):
        product = input("Ingrese el nombre del producto: ")
        price = int(input("Ingrese el precio del producto: "))
        self.server.create_product(product, price)
        print("Producto creado")

    def update_product(self):
        self.show_products()
        product = input("Ingrese el producto a editar: ")
        db_products = self.server.get_products()
        if product not in db_products:
            print("Producto no encontrado")
            return
        new_name = input("Ingrese el nuevo nombre: ")
        price = int(input("Ingrese el nuevo precio: "))
        self.server.update(product, new_name, price)
        print("Producto actualizado")

    def delete_product(self):
        self.show_products()
        product = input("Ingrese el producto a eliminar: ")
        db_products = self.server.get_products()
        if product not in db_products:
            print("Producto no encontrado")
            return
        self.server.delete(product)
        print("Producto eliminado")
    
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