#
# name = 'Ala'
# if 'ł' in name:
#     print('W imieniu jest ł')
# else:
#     print('Nie ma ł')

# favourite_sports = ['bieganie', 'jazda na rowerze', 'pływanie',]
#
# if 'koszykówka' in favourite_sports:
#     print('Zagramy w kosza?')
# else:
#     print('hmm')
# print(favourite_sports[-1])

# person = {
#     'first name': 'Mikołaj',
#     'last name': 'Lewandowski',
# }
# if 'first name' in person:
#     print(person['first name'])
#
# if 'car' in person:
#     print(person['car'])

# if 'koszykówka' not in favourite_sports:
#     print('Nie lubisz koszykówki')
# else:
#     print('hmm')

# age = 45

# if age:
#     print('if age')
# if age == True: # age ma  wartość 45 co jest inne niż True
#     print('age == True')
# if age is True:
#     print('if age is True')
# true_value = True
# if true_value is True:
#     print('if True_value is true')
# nothing = None
# if not nothing:
#     print('if not nothing')

# zero = 0
# if not zero:
#     print('if not zero')
#
# if zero is None:
#     print('if zero is None')
# if nothing is None:
#     print('if nothing is none')
# if zero is not None:
#     print('if zero is not None')
# if nothing is not None:
#     print('if nothing is not None')

lista = input('Wypisz liste zakupów ')
shoppin_list = lista.split(',')
print(shoppin_list)
if 'chleb'in shoppin_list or 'bułki' in shoppin_list:
    print('Mmm pieczywo')
else:
    print('Bez pieczywa?')

number = (input('Jaki jest twój numer telefonu? '))
if '0' in number:
    print("Cyfra zero")
else:
    print('Bez zera')

value = 'Bigos'

if value is True:
    print('True')
elif value is False:
    print('False')
elif value is None:
    print('None')
elif value is not True and value is not False and value is not None:
    print('Coś innego')