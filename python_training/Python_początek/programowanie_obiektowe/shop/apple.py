class Apple:
    def __init__(self, species_name, size, price, amount):
        self.amount = amount
        self.price = price
        self.size = size
        self.species_name = species_name

    def total_price(self):
        amount = self.amount
        price = self.price
        total_price = amount * price
        return total_price

