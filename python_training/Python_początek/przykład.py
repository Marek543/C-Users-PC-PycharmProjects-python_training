import random

def say_hello():
    print('Hello World')

def say_good_bye():
    print('Good bye')

def randomize_func(first_func, second_func):
    number = random.randint(1,2)
    if number == 1:
        return first_func
    return second_func
def say_hello_name(name):
    print(f'Hello {name}')

def calculate_something(some_value, other_value):
    return some_value + other_value

def run_example():
    # hello_name = say_hello_name
    # hello_name('Mikołaj')
    # calculation = calculate_something
    # result = calculation(10, 30)
    # print(result)
    hello_or_good_bye = randomize_func(say_hello, say_good_bye)
    hello_or_good_bye()


if __name__ == '__main__':
    run_example()