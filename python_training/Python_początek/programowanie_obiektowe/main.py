import random
from shop.apple import Apple
from shop.potato import Potato
from shop.order import Order
from shop.product import Product
from shop.order_element import OrderElement
from shop.order import Order, ExpressOrder
from shop.tax_calculator import TaxCalculator
from shop.discount import Discount
from shop import data_generator
from shop.product import ExpandedProduct, ExpiringProduct
from shop.express_order import ExpresssssOrder

def compare_lists(first,second):
    for order in first:
        if order not in second:
            return False
    return True

def run_homework():
    # green_apple = Apple(species_name='Green', size='M', price=3.5)
    # red_apple = Apple(species_name='Red', size='S', price=2.8)
    # old_potato = Potato(species_name='Old', size='L', price=4)
    # print(green_apple.species_name, green_apple)
    # print(red_apple.species_name, red_apple)
    # print(red_apple.total_price())
    # print(old_potato.species_name, old_potato.total_price())
    first_order = Order.generate_order(2)
    # print(first_order)
    # second_order = generate_order()
    # print(second_order)

    # print(green_apple)
    # print(red_apple)
    # print(old_potato)
    # print(f'Liczba elemntów w zamówieniu: {len(first_order)}')
    # print(compare_lists(first_order, second_order))
    cookie = Product(name='Ciastko', category_name='Jedzenie', unit_price=4)
    tomato = Product(name='Pomidor', category_name='Owoce i warzywa', unit_price=5)
    first_order.add_product_to_the_order(cookie, 3)
    first_order.add_product_to_the_order(tomato, 6)
    print(first_order)
    TaxCalculator.calculate_tax(first_order)

    # other_cookie = Product(name='Inne ciastko', category_name='Jedzenie', unit_price=4)
    # juice = Product(name='Sok', category_name='Napoje', unit_price=3)
    # first_order_elements = [
    #     # OrderElement(product=cookie, amount=3),
    #     OrderElement(product=other_cookie, amount=3),
    #     OrderElement(product=juice, amount=4)
    # ]
    # second_order_elements = [
    #     OrderElement(product=juice, amount=4),
    #     OrderElement(product=cookie, amount=3)
    # ]
    #
    # first_order = Order(client_first_name='Kuba', client_last_name='Kowalski', order_elements=first_order_elements)
    # second_order = Order(client_first_name='Kuba', client_last_name='Kowalski', order_elements=second_order_elements)
    # # second_order.client_last_name = 'Lewandowski'
    #
    # if first_order == second_order:
    #     print('Te zamówienia są takie same')
    # else:
    #     print('Te zamówienia są różne')



def generate_multiple_orders():
    number_of_orders = 5
    order_list = []
    for order in range(number_of_orders):
        order_list.append(Order.generate_order())
    # order_list.sort(key=sort_by_total_price)
    order_list.sort(key=lambda order: order.calculate_price)
    for order in order_list:
        print(order)

def sort_by_total_price(order):
    return order.calculate_price

def generate_order_elements_():
    number_of_products = 5
    products = []
    for product_number in range(number_of_products):
        product_name = f'Produkt-{product_number}'
        category_name = "Inne"
        unit_price = random.randint(1, 30)
        amount = random.randint(1, 50)
        product = Product(product_name, category_name, unit_price)
        order_element = OrderElement(product, amount)
        products.append(order_element)
    return products

def ex_3():
    first_name = "Mikołaj"
    last_name = 'Lewandowski'
    order_elements = data_generator.generate_order_elements()
    normal_order = Order(client_first_name=first_name, client_last_name=last_name, order_elements=order_elements)
    loyal_customer_order = Order(client_first_name=first_name, client_last_name=last_name, order_elements=order_elements, discount_policy=Discount.regular_customer_discount)
    christmas_order = Order(client_first_name=first_name, client_last_name=last_name, order_elements=order_elements, discount_policy=Discount.holiday_special_discount)

    # print(normal_order)
    for order_element in normal_order.order_elements:
        print(order_element)
    # print(loyal_customer_order)
    # print(christmas_order)

def ex_4():
    first_name = "Mikołaj"
    last_name = 'Lewandowski'
    date_of_delivery = '21.10.2023'
    order_elements = data_generator.generate_order_elements()
    order = Order(first_name, last_name, order_elements)
    print(order)
    hastened_order = ExpressOrder(first_name, last_name, date_of_delivery, order_elements)
    print(hastened_order)
    quick_order = ExpresssssOrder(
        date_of_delivery,
        first_name,
        last_name,
        order_elements)
    print(quick_order)
    # new_order_elements = data_generator.generate_order_elements(12)
    # order.order_elements = new_order_elements
    # print(order)
    # print(order.total_price)

def ex_5():
    apple = ExpandedProduct(name='jabłko', category_name='owoc', unit_price= 5, expiration_date=2024, year_of_creation=2022)
    apple_number_2 = ExpiringProduct(name='jabłko', category_name='owoc', unit_price= 5, production_year=2022, validity_years=2)
    print(apple.does_expire(2025))
    print(apple_number_2.does_expire(2025))


if __name__ == '__main__':
    ex_4()