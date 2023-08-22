apples_price = 3
bananas_price = 4.5
pears_price = 3

# print(f'Czy jabłka są droższe od bananów {apples_price > bananas_price}')
# print(f'Czy jabłka są tańsze od bananów {apples_price < bananas_price}')
# print(f'Czy banany kosztują tyle samo co gruszki {bananas_price == pears_price}')
# print(f'Banany nie kosztują tyle samo co gruszki {bananas_price != pears_price}')
# print(f'Czy jabłka są droższe lub w takiej samej cenie jak gruszki {apples_price >= pears_price}')
# print(f'Czy jabłka są tańśze lub w takiej samej cenie jak gruszki {apples_price <= pears_price}')
# print(f'Czy jabłka są w takiej samej cenie jak gruszki {apples_price == pears_price}')

# result = apples_price > bananas_price
# print(type(result))
#
# print(f'{True} jest typu {type(True)}')
# print(f'{False} jest typu {type(False)}')

true_variable = True
false_variable = False
# print(true_variable == false_variable)

# result = bool(7)
# print(f'bool(7) -> {result}')
# result = bool(-3.4)
# print(f'bool(-3.4) -> {result}')
# result = bool(0)
# print(f'bool(0) -> {result}')
#
# result = bool('Napis')
# print(f'bool("Napis") -> {result}')
# result = bool('')
# print(f"bool('') -> {result} ")
#
# result = bool([4, 0])
# print(f'bool([4, 0]) -> {result}')
# result = bool([])
# print(f'bool([]) -> {result}')
#
# result = bool(None)
# print(f'bool(None) -> {result}')

name = "Mikołaj"
result = name == "Mikołaj"
# print(f"name == 'Mikołaj' -> {result}")

# your_name =input("Jak masz na imię? ")
# are_you_mikolaj = your_name == "Mikołaj"
# print(f'Twoje imię to Mikołaj? {are_you_mikolaj}')

# Wartość stringa większa od drugiej gdy jego litery są później w alabecie
# print(f'Warzywa > Słodycze -> {"Warzywa" > "Słodycze"}')

shopping_list = ["Mąka", "Jogurt"]
my_list = ["Czekolada", "Marchewka", "Chleb"]
# print(f'{shopping_list} > {my_list} -> {shopping_list > my_list}')

# Ropa = input("Wypisz cene ropy ")
# Złoto = input("Wypisz cene złota ")
# Zboże = input("Wypisz cene zboża ")
#
# print(f'Czy ropa jest droższa od złota? {Ropa > Złoto}')
# print(f'Czy ropa jest tańsza od złota? {Ropa < Złoto}')
# print(f'Czy zboże jest równe cenie ropy? {Zboże == Ropa}')
# print(f'Czy zboże jest różne od złota? {Zboże != Złoto}')
# print(f'Czy zboże jest równe lub większe od złota? {Zboże >= Złoto}')

# lista = input('Wypisz liste zakupów ')
# listunia = lista.split(',')
# długa_lista = len(listunia) > 4
# print(f'Czy lista jest długa? {długa_lista}')

value_input = input("Jaka jest początkowa wartość kapitału? ")
intrest_input = input("Jakie jest oprocentowanie? ")
time_input = input("Ile lat będzie trwać lokata? ")

wartość_pocz = float(value_input)
oprocentowanie = float(intrest_input)
liczba_lat = float(time_input)

wartość = wartość_pocz * (1 + oprocentowanie/100) ** liczba_lat

print("Po", liczba_lat,  "lokata będzie wynosić", wartość, "złotych")
cel = 1.1 * float(wartość_pocz)
print(cel)
print(f'Czy wartość lokaty wzrosła o 10%? {wartość >= cel}')
