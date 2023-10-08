
class OrderElement:
    def __init__(self, product, amount):
        self.amount = amount
        self.product = product
        self.total_price = self.calculate_price()

    def __str__(self):
        return f'{self.product} | Ilość: {self.amount} szt | Kwota: {self.total_price} PLN'
        # product = self.product
        # product = print(product)
        # ilość = print(f'Zamówiona liczba sztuk: {self.amount}')
        # cena = print(f'Cena danej pozycji wynosi {self.total_price()} PLN \n')
        # order_element = ''
        # order_element += str(product)
        # order_element += str(ilość)
        # order_element += str(cena)
        # return order_element


    # def print_order_element(self):
    #     product = self.product
    #     product.print_product()
    #     print('\t', end="")
    #     print(f'Zamówiona liczba sztuk: {self.amount}')
    #     print('\t', end="")
    #     print(f'Cena danej pozycji wynosi {self.total_price()} PLN \n')

    def calculate_price(self):
        total_price = self.product.unit_price * self.amount
        return total_price

    # def order_element_data(self):
    #     return self.product, self.amount

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.product == other.product and
                self.amount == other.amount)


