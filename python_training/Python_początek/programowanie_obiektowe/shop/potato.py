class Potato:
    def __init__(self, species_name, size, price, amount):
        self.amount = amount
        self.species_name = species_name
        self.size = size
        self.price = price

    def total_price(self):
        amount = self.amount
        price = self.price
        total_price = amount * price
        return total_price
