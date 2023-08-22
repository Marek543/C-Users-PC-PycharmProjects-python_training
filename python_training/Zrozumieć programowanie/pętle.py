
# grades = []
# subjects = ['matematyka', 'fizyka', 'chemia', 'biologia']
# for subject in subjects:
#     ocena = int(input(f'Jaka jest twoja ocena z przedmiotu {subject}? '))
#     grades.append(ocena)
#
# for grade in grades:
#     if grade == 1:
#         print('Niestety')
#         break
# else:
#     print('Zdałeś')

# ocena = (input('Wprowadź następną ocenę: '))
# while ocena != 'X':
#     grades.append(int(ocena))
#     if ocena == '1':
#         print('Należy powtórzyć klasę')
#         break
#     ocena = (input('Wprowadź następną ocenę, wpisz "X" aby zakończyć: '))
# else:
#     print('Zdałeś do następnej klasy')

# print('Kalkulator budżetu miesięcznego')
# expenditures = {}
#
#
# while True:
#     category_name = input('Podaj kategorię wydatków lub zakończ wpisując "X": ')
#     if category_name == 'X':
#         break
#     expenditures[category_name] = []
#     while True:
#         expenditure = input(f'Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpsiując "X": ')
#         if expenditure == 'X':
#             break
#         expenditure_value = float(expenditure)
#         expenditures[category_name].append(expenditure_value)
#
#
# print(expenditures)
#
# total_expenditures = 0
#
# for category_expenditures in expenditures.values():
#     for expenditure_value in category_expenditures:
#         total_expenditures += expenditure_value
#
# expenditures_percentage = {}
# for category_name,category_expenditures in expenditures.items():
#     total_category_expenditures = 0
#     for expenditure_value in category_expenditures:
#         total_category_expenditures += expenditure_value
#     expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures
# print(expenditures_percentage)
#
# most_important_category = None
# most_important_category_percentage = 0
# for category, percentage in expenditures_percentage.items():
#     if percentage > most_important_category_percentage:
#         most_important_category_percentage = percentage
#         most_important_category = category
#
# if most_important_category is not None:
#     print(f'Najwięcej wydajesz na {most_important_category} i jest to {most_important_category_percentage:.0f}% budżetu')
# for category, percentage in expenditures_percentage.items():
#     print(f'Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków')

# lista = [30, 40, 51, 60, 71]
#
# for number in lista:
#     if number % 2 == 0:
#         continue
#     print(number)
