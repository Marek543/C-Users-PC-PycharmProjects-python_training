import random
def calculate_sum_via_list(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def calculate_sum_via_args(*args):
    # print(type(args))
    result = 0
    for number in args:
        result += number
    return result

def add_two_numbers(first, second):
    return first + second

def run_example():
    numbers = [1,2,3,4,5,6]
    # result = calculate_sum_via_list(numbers)
    result = calculate_sum_via_args(*numbers)
    print(result)

    two_numbers = [10,30]
    result = add_two_numbers(*two_numbers)
    print(result)

    combined_numbers = [*numbers, *two_numbers]
    print(combined_numbers)

    # result = calculate_sum_via_args(5,6)
    # print(result)

def print_grades(**kwargs):
    for subject,grade in kwargs.items():
        print(f'Z przedmiotu: {subject} wystawiono: {grade}')


def example():
    grades = {
        'matematyka': 4,
        'fizyka': 4,
        'chemia': 5,
    }
    print_grades(**grades)

    more_grades = {
        'polski': 4,
        'biologia': 4,
        'geografia': 3
    }
    all_grades = {**grades, **more_grades}
    print(all_grades)
    # print_grades(
    #     matematyka=4,
    #     fizyka=4,
    #     chemia=5,
    #     polski=4,
    #     biologia=4,
    #     geografia=3
    # )

def add_up_words(*args):
    napis = ''
    # for word in args:
    #     napis +=str(word)
    #     if not word is args[-1]:
    #         napis += '-'
    # return napis
    return '-'.join(args)

def print_call_str(**kwargs):
    # for item,value in kwargs.items():
    #     print(f'{item}={value}')
    call_str = 'print_call_str('
    for argument_name, argument_value in kwargs.items():
        call_str += f'{argument_name}={argument_value},'
    call_str += ')'
    print(call_str)

def generate_random_lists():
    lista_1 = []
    while len(lista_1) < random.randint(1, 10):
        lista_1.append(random.randint(1, 10))
    print(lista_1)
    lista_2 = []
    while len(lista_2) < random.randint(1, 10):
        lista_2.append(random.randint(1, 10))
    print(lista_2)
    combined_lists = [*lista_1, *lista_2]
    print(combined_lists)

def dictionaries():
    słownik1 = {
        'jajka': 1,
        'chleb': 2
    }
    słownik2 = {
        'czekolada': 3,
        'herbata': 4
    }
    wszystkie_słowniki = {**słownik1, **słownik2}
    print(wszystkie_słowniki)
    print_call_str(**wszystkie_słowniki)

def przykład():
    lista = ['mąka', 'jajka', 'chleb', '2', '7']
    # print(add_up_words(*lista))
    print_call_str(argument='i jego wartość', a_to_inny='wartość też inna')
    # arguments = {
    #     'first_name': 'Mikołaj',
    #     'age': 134,
    # }
    # write_arguments(**arguments)

def generate_random_numbers():
    result = []
    for _ in range(random.randint(5, 10)):
        result.append(random.randint(1, 100))
    return result

def run_homerowk():
    random_numbers = generate_random_numbers()
    other_numbers = generate_random_numbers()
    print(random_numbers)
    print(other_numbers)
    all_numbers = [*random_numbers, *other_numbers]
    print(all_numbers)


if __name__ == '__main__':
    dictionaries()