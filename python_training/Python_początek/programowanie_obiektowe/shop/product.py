class Product:
    def __init__(self, name, category_name, unit_price):
        self.unit_price = unit_price
        self.category_name = category_name
        self.name =name

def print_product(product):
    print(f'Nazwa: {product.name} | Kategoria: {product.category_name} | Cena: {product.unit_price} /szt')
