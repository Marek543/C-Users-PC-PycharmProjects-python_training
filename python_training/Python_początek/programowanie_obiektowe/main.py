
from shop.apple import Apple
from shop.order import print_order, generate_order

def run_homework():
    green_apple = Apple(species_name='Green', size='M', price=3.5)
    red_apple = Apple(species_name='Red', size='S', price=2.8)
    print(green_apple.species_name, green_apple)
    print(red_apple.species_name, red_apple)
    first_order = generate_order()
    print_order(first_order)
    second_order = generate_order()
    print_order(second_order)

if __name__ == '__main__':
    run_homework()