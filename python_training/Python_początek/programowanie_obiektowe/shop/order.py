import random
from shop.product import Product
from shop.order_element import OrderElement
from shop.discount import Discount


class Order:

    MAX_NUMBER_OF_ORDER_ELEMENTS = 10
    def __init__(self, client_first_name, client_last_name, order_elements=None, discount_policy=None):
        self.client_last_name = client_last_name
        self.client_first_name = client_first_name

        if order_elements is None:
            order_elements = []
        if len(order_elements) > Order.MAX_NUMBER_OF_ORDER_ELEMENTS:
            order_elements = order_elements[:Order.MAX_NUMBER_OF_ORDER_ELEMENTS]

        if discount_policy is None:
            discount_policy = Discount.no_discount
        self.discount_policy = discount_policy

        self._order_elements = order_elements
        # self.total_price = self._total_order_price()

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, value):
        if len(value) < Order.MAX_NUMBER_OF_ORDER_ELEMENTS:
            self._order_elements = value
        else:
            print('Osiągnięto maksymalną liczbę pozycji  w zamówieniu')
            self._order_elements = value[:Order.MAX_NUMBER_OF_ORDER_ELEMENTS]
        # self.total_price = self._total_order_price()

    @property
    def total_price(self):
        return self._total_order_price()

    def _total_order_price(self):
        total_order_price = 0
        for order_element in self._order_elements:
            total_order_price += order_element.calculate_price()
        return self.discount_policy(total_order_price)

    def add_product_to_the_order(self, product, amount):
        new_order_element = OrderElement(product, amount)
        if len(self._order_elements) >= Order.MAX_NUMBER_OF_ORDER_ELEMENTS:
            print('Nie ma już miejsca w zamówieniu')
        else:
            self._order_elements.append(new_order_element)
            # self.total_price = self._total_order_price()



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
        value_details = f'Łączna wartość zamówienia wynosi {self.total_price} PLN'
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

    # def calculate_discount(self, discount_policy=None):
    #     if discount_policy is None:
    #         discount_policy = Discount.no_discount
    #     self.total_price = discount_policy



    @classmethod
    def generate_order(cls):
        number_of_products = random.randint(1, Order.MAX_NUMBER_OF_ORDER_ELEMENTS)
        products = []
        for product_number in range(number_of_products):
            product_name = f'Produkt-{product_number}'
            category_name = "Inne"
            unit_price = random.randint(1, 30)
            amount = random.randint(1,50)
            product = Product(product_name, category_name, unit_price)
            order_element = OrderElement(product, amount)
            products.append(order_element)
        order = Order(client_first_name='Mikołaj', client_last_name='Lewandowski', order_elements=products)
        return order

# return f'Wygenerowano {number_of_orders} losowych zamówień'

class ExpressOrder(Order):
    def __init__(self, client_first_name, client_last_name, date_of_delivery, order_elements=None, discount_policy=None):
        super().__init__(client_first_name,client_last_name,order_elements,discount_policy)
        self.date_of_delivery = date_of_delivery

    @property
    def total_payment(self):
        extra_payment = 20
        return self._total_order_price() + extra_payment


    def __str__(self):
        mark_line = '=' * 20
        order_details = f'Zamówienie złożone przez {self.client_first_name} {self.client_last_name}'
        date_of_delivery = f'Data dostawy: {self.date_of_delivery}'
        value_details = f'Łączna wartość zamówienia wynosi {self.total_payment} PLN'
        product_details = 'Zamówione produkty:\n'
        for element in self._order_elements:
            product_details += f'\t{element}\n'
        result = '\n'.join([mark_line, order_details, date_of_delivery, value_details, product_details, mark_line])
        return result