
from shop.apple import Apple
from shop.potato import Potato
from shop.order import generate_order

def run_homework():
    # green_apple = Apple(species_name='Green', size='M', price=3.5, amount=20)
    # red_apple = Apple(species_name='Red', size='S', price=2.8, amount=15)
    # old_potato = Potato(species_name='Old', size='L', price=4, amount=30)
    # print(green_apple.species_name, green_apple)
    # print(red_apple.species_name, red_apple)
    # print(red_apple.total_price())
    # print(old_potato.species_name, old_potato.total_price())
    first_order = generate_order()
    first_order.print_order()
    second_order = generate_order()
    second_order.print_order()

if __name__ == '__main__':
    run_homework()