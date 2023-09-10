import random
from shop.product import Product
from shop.order_element import OrderElement


class Order:
    def __init__(self, client_first_name, client_last_name, order_elements=None):
        self.client_last_name = client_last_name
        self.client_first_name = client_first_name

        if order_elements is None:
            order_elements = []
        self._order_elements = order_elements
        self.total_price = self._total_order_price()

    def _total_order_price(self):
        total_order_price = 0
        for order_element in self._order_elements:
            total_order_price += order_element.total_price
        return total_order_price

    def add_product_to_the_order(self, product, amount):
        new_order_element = OrderElement(product, amount)
        self._order_elements.append(new_order_element)
        self.total_price = self._total_order_price()



    # def print_order(self):
    #     mark_line = '=' * 20
    #     order_details = f'Zamówienie złożone przez {self.client_first_name} {self.client_last_name}'
    #     value_details = f'Łączna wartość zamówienia wynosi {self.total_order_price()} PLN'
    #     product_details = 'Zamówione produkty:\n'
    #     for element in self.order_elements:
    #         product_details += f'\t{element}\n'
    #     result = '\n'.join([mark_line, order_details, value_details, product_details, mark_line])
    #     return result

    def __str__(self):
        mark_line = '=' * 20
        order_details = f'Zamówienie złożone przez {self.client_first_name} {self.client_last_name}'
        value_details = f'Łączna wartość zamówienia wynosi {self._total_order_price()} PLN'
        product_details = 'Zamówione produkty:\n'
        for element in self._order_elements:
            product_details += f'\t{element}\n'
        result = '\n'.join([mark_line, order_details, value_details, product_details, mark_line])
        return result

    def __len__(self):
        return len(self._order_elements)

    # def order_data(self):
    #     return self.client_first_name, self.client_last_name, self.order_elements

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if len(self._order_elements) != len(other.order_elements):
            return False
        if self.client_first_name != other.client_first_name or self.client_last_name != other.client_last_name:
            return False
        for order_element in self._order_elements:
            if order_element not in other.order_elements:
                return False
        return True


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