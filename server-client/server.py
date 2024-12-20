# Emulate prices data
prices = {
    "manzana": 1000,
    "pera": 2000,
    "naranja": 3000,
    "piña": 4000,
    "sandia": 5000,
    "melon": 6000,
    "banano": 1000,
    "lulo": 2000,
    "uva": 3000,
    "mango": 4000
}

class Server:
    def __init__(self):
        print("Server se ha inicializado en el puerto 5000")

    def create_product(self, product, price):
        prices[product] = price

    def update(self, product, new_name, price):
        prices[new_name] = prices.pop(product)
        prices[new_name] = price

    def delete(self, product):
        prices.pop(product)

    def get_price(self, product):
        if product not in prices:
            return "Producto no encontrado"
        
        return prices[product]
    
    def get_products(self):
        return list(prices.keys())
    
    def get_prices(self):
        return prices
