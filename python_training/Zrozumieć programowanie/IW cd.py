
# kwota = float(input("Jaka jest kwota kredytu? "))
# oprocentowanie = float(input("Jakie jest oprocentowanie kredytu? "))
# WW_własnego = float(input("Jak jest wartość wkładu własnego? "))
# lata = float(input("Ile lat będzie trwał kredyt? "))
# przychód = float(input("Jaki jest przychód miesięczny? "))
# wydatki = float(input("Jakie są wydatki miesięczne? "))
#
# Rata_kredytu = (kwota * oprocentowanie / 100) / 12 + kwota / (lata * 12)
# print(f'Rata kredytu wynosi {Rata_kredytu}')
#
# Dostępne_środki = przychód - wydatki
# print(f'Dostępne środki wynoszą {Dostępne_środki}')
#
# Wartość_nieruchomości = WW_własnego + kwota
# print(f'WW własnego wynosi {(WW_własnego / Wartość_nieruchomości) * 100:.2f} %')
#
# if WW_własnego >= 0.2 * Wartość_nieruchomości and Dostępne_środki > Rata_kredytu + 1000:
#     print("Możesz wziąć kredyt")
# if 0.2 * Wartość_nieruchomości > WW_własnego >= 0.1 * Wartość_nieruchomości and Dostępne_środki > Rata_kredytu + 2000:
#     print("Możesz wziąć kredyt")
# else:
#     print("Nie możesz wziąć kredytu")

# income = 5000
# employees_number = 7
# years_on_the_market = 3

# if income < 5000:
#     print('Przyznano główne wsparcie')
# else:
#     if 5 <= employees_number <= 10:
#         print("Przyznano wsparcie z funduszu pracowników")
#     else:
#         if years_on_the_market < 3:
#             print('Przyznano wsparcie dla nowych firm')
#         else:
#             print('Przyznano wsparcie na pocieszenie')

# if income < 5000:
#     print('Przyznano główne wsparcie')
# elif 5 <= employees_number <= 10:
#     print("Przyznano wsparcie z funduszu pracowników")
# elif years_on_the_market < 3:
#     print('Przyznano wsparcie dla nowych firm')
# else:
#     print('Przyznano wsparcie na pocieszenie')

# selection = input('Czy chcesz obliczyć lokate czy kredyt? (L/K) ')
#
# if selection == 'L':
#     value_input = input("Jaka jest początkowa wartość kapitału? ")
#     intrest_input = input("Jakie jest oprocentowanie? ")
#     time_input = input("Ile lat będzie trwać lokata? ")
#     wartość_pocz = float(value_input)
#     oprocentowanie = float(intrest_input)
#     liczba_lat = float(time_input)
#     wartość = wartość_pocz * (1 + oprocentowanie/100) ** liczba_lat
#     print("Po", liczba_lat,  "lokata będzie wynosić", wartość, "złotych")
#     cel = 1.1 * float(wartość_pocz)
#     print(cel)
#     print(f'Czy wartość lokaty wzrosła o 10%? {wartość >= cel}')
# elif selection == 'K':
#     kwota = float(input("Jaka jest kwota kredytu? "))
#     oprocentowanie = float(input("Jakie jest oprocentowanie kredytu? "))
#     WW_własnego = float(input("Jak jest wartość wkładu własnego? "))
#     lata = float(input("Ile lat będzie trwał kredyt? "))
#     przychód = float(input("Jaki jest przychód miesięczny? "))
#     wydatki = float(input("Jakie są wydatki miesięczne? "))
#     Rata_kredytu = (kwota * oprocentowanie / 100) / 12 + kwota / (lata * 12)
#     print(f'Rata kredytu wynosi {Rata_kredytu}')
#     Dostępne_środki = przychód - wydatki
#     print(f'Dostępne środki wynoszą {Dostępne_środki}')
#     Wartość_nieruchomości = WW_własnego + kwota
#     print(f'WW własnego wynosi {(WW_własnego / Wartość_nieruchomości) * 100:.2f} %')
#     if WW_własnego >= 0.2 * Wartość_nieruchomości and Dostępne_środki > Rata_kredytu + 1000:
#         print("Możesz wziąć kredyt")
#     if 0.2 * Wartość_nieruchomości > WW_własnego >= 0.1 * Wartość_nieruchomości and Dostępne_środki > Rata_kredytu + 2000:
#         print("Możesz wziąć kredyt")
#     else:
#         print("Nie możesz wziąć kredytu")
# else:
#     print("Powinieneś był wpisać 'L' lub 'K'")
#
wiek = int(input("Ile masz lat? "))
płeć = input('Jaka jest twoja płeć? (M/K) ')
uzyskany_wynik = int(input('Jaki jest twój wynik testu Coopera? '))

# if 17 <= wiek <= 20:
#     if płeć == 'M':
#         if uzyskany_wynik < 2300:
#             print('Bardzo źle')
#         if 2300 <= uzyskany_wynik <= 2499:
#             print('Źle')
#         if 2499 < uzyskany_wynik <= 2699:
#             print('Średnio')
#         if 2700 <= uzyskany_wynik < 3000:
#             print('Dobrze')
#         if uzyskany_wynik >= 3000:
#             print('Bardzo dobrze')
#     if płeć == 'K':
#         if uzyskany_wynik < 1700:
#             print('Bardzo źle')
#         if 1700 <= uzyskany_wynik <= 1799:
#             print('Źle')
#         if 1799 < uzyskany_wynik <= 2099:
#             print('Średnio')
#         if 2100 <= uzyskany_wynik < 2300:
#             print('Dobrze')
#         if uzyskany_wynik >= 2300:
#             print('Bardzo dobrze')
# if 20 < wiek <= 29:
#     if płeć == 'M':
#         if uzyskany_wynik < 1600:
#             print('Bardzo źle')
#         if 1600 <= uzyskany_wynik <= 2199:
#             print('Źle')
#         if 2199 < uzyskany_wynik <= 2399:
#             print('Średnio')
#         if 2399 <= uzyskany_wynik < 2800:
#             print('Dobrze')
#         if uzyskany_wynik >= 2800:
#             print('Bardzo dobrze')
#     if płeć == 'K':
#         if uzyskany_wynik < 1500:
#             print('Bardzo źle')
#         if 1500 <= uzyskany_wynik <= 1799:
#             print('Źle')
#         if 1799 < uzyskany_wynik <= 2199:
#             print('Średnio')
#         if 2199 <= uzyskany_wynik < 2700:
#             print('Dobrze')
#         if uzyskany_wynik >= 2700:
#             print('Bardzo dobrze')
# else:
#     print('Płeć ci się pomerdała')

if 17 <= wiek <= 20:
    if płeć == 'M':
        if uzyskany_wynik < 2300:
            print('Bardzo źle')
        elif uzyskany_wynik <= 2499:
            print('Źle')
        elif uzyskany_wynik <= 2699:
            print('Średnio')
        elif uzyskany_wynik < 3000:
            print('Dobrze')
        else:
            print('Bardzo dobrze')
    if płeć == 'K':
        if uzyskany_wynik < 1700:
            print('Bardzo źle')
        elif uzyskany_wynik <= 1799:
            print('Źle')
        elif uzyskany_wynik <= 2099:
            print('Średnio')
        elif uzyskany_wynik < 2300:
            print('Dobrze')
        else:
            print('Bardzo dobrze')
if 20 < wiek <= 29:
    if płeć == 'M':
        if uzyskany_wynik < 1600:
            print('Bardzo źle')
        elif uzyskany_wynik <= 2199:
            print('Źle')
        elif uzyskany_wynik <= 2399:
            print('Średnio')
        elif uzyskany_wynik < 2800:
            print('Dobrze')
        else:
            print('Bardzo dobrze')
    if płeć == 'K':
        if uzyskany_wynik < 1500:
            print('Bardzo źle')
        elif uzyskany_wynik <= 1799:
            print('Źle')
        elif uzyskany_wynik <= 2199:
            print('Średnio')
        elif uzyskany_wynik < 2700:
            print('Dobrze')
        else:
            print('Bardzo dobrze')