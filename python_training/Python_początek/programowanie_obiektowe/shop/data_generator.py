import random
from shop.product import Product
from shop.order_element import OrderElement
from shop.order import Order

MIN_NUMBER_OF_ORDER_ELEMENTS = 1

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30
MIN_AMOUNT = 1
MAX_AMOUNT = 50

def generate_order_elements(number_of_order_elements=None):
    if number_of_order_elements is None:
        number_of_order_elements = random.randint(MIN_NUMBER_OF_ORDER_ELEMENTS, Order.MAX_NUMBER_OF_ORDER_ELEMENTS)
    products = []
    for product_number in range(number_of_order_elements):
        product_name = f'Produkt-{product_number}'
        category_name = "Inne"
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        amount = random.randint(MIN_AMOUNT, MAX_AMOUNT)
        product = Product(product_name, category_name, unit_price)
        order_element = OrderElement(product, amount)
        products.append(order_element)
    return products
