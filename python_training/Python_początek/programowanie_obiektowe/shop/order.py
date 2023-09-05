import random
from shop.product import Product
from shop.order_element import OrderElement


class Order:
    def __init__(self, client_first_name, client_last_name, order_elements=None):
        self.client_last_name = client_last_name
        self.client_first_name = client_first_name

        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements

    def total_order_price(self):
        total_order_price = 0
        for order_element in self.order_elements:
            total_order_price += order_element.total_price()
        return total_order_price


    def print_order(self):
        print('=' * 20)
        print(f'Zamówienie złożone przez {self.client_first_name} {self.client_last_name}')
        print(f'Łączna wartość zamówienia wynosi {self.total_order_price()} PLN')
        print('Zamówione produkty: \n')
        for product in self.order_elements:
            print('\t', end="")
            product.print_order_element()
        print('=' * 20)
        print()

def generate_order():
    number_of_product = random.randint(1, 10)
    products = []
    for product_number in range(number_of_product):
        product_name = f'Produkt-{product_number}'
        category_name = "Inne"
        unit_price = random.randint(1, 30)
        amount = random.randint(1,50)
        product = Product(product_name, category_name, unit_price)
        order_element = OrderElement(product, amount)
        products.append(order_element)
    order = Order(client_first_name='Mikołaj', client_last_name='Lewandowski', order_elements=products)
    return order