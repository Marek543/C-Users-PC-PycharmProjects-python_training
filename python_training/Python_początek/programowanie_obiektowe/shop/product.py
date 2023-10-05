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

class ExpandedProduct(Product):
    def __init__(self, name, category_name, unit_price, expiration_date, year_of_creation):
        super().__init__(name, category_name, unit_price)
        self.year_of_creation = year_of_creation
        self.expiration_date = expiration_date
        self.time_before_spoiling = expiration_date - year_of_creation

    def __str__(self):
        return (f'Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price} PLN/szt \n'
                f'Data ważności do spożycia: {self.expiration_date}\n'
                f'Rok produkcji: {self.year_of_creation}\n'
                f'Liczba lat przed zepsuciem: {self.time_before_spoiling}')

    def does_expire(self, current_year):
        if (current_year - self.year_of_creation) <= self.time_before_spoiling:
            return 'Produkt dobry do spożycia'
        else:
            return 'Produkt przeterminowany'

class ExpiringProduct(Product):
    def __init__(self, name, category_name, unit_price, production_year, validity_years):
        super().__init__(name,category_name, unit_price)
        self.production_year = production_year
        self.validity_years = validity_years

    def does_expire(self, current_year):
        return current_year > self.production_year + self.validity_years

