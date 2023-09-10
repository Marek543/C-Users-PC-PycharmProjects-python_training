class Product:
    def __init__(self, name, category_name, unit_price):
        self.unit_price = unit_price
        self.category_name = category_name
        self.name =name

    def __str__(self):
        return f'Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price} PLN/szt'

    # def print_product(self):
        # print(f'Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price} PLN/szt')

    # def product_data(self):
    #     return self.name, self.category_name, self.unit_price

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category_name == other.category_name and
                self.unit_price == other.unit_price)




