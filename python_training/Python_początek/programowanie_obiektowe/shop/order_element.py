
class OrderElement:
    def __init__(self, product, amount):
        self.amount = amount
        self.product = product


    def print_order_element(self):
        product = self.product
        product.print_product()
        print('\t', end="")
        print(f'Zamówiona liczba sztuk: {self.amount}')
        print('\t', end="")
        print(f'Cena danej pozycji wynosi {self.total_price()} PLN \n')

    def total_price(self):
        product = self.product
        unit_price = product.unit_price
        amount = self.amount
        total_price = unit_price * amount
        return total_price



