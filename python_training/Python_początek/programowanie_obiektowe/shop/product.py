class Product:
    def __init__(self, name, category_name, unit_price):
        self.unit_price = unit_price
        self.category_name = category_name
        self.name =name

    def print_product(self):
        print(f'Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price} PLN/szt')
