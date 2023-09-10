class Potato:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

    def total_price(self, amount):
        price = self.price
        total_price = amount * price
        return total_price

    def __repr__(self):
        return f'species_name = {self.species_name}, size = {self.size}, price = {self.price}'
