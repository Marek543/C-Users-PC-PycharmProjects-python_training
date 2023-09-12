
from shop.apple import Apple
from shop.potato import Potato
from shop.order import Order
from shop.product import Product
from shop.order_element import OrderElement
from shop.order import Order
from shop.tax_calculator import TaxCalculator

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


if __name__ == '__main__':
    run_homework()