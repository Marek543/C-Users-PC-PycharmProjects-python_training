from symulator_sklepu.funkcje import składanie_zamówienia

shopping_list = składanie_zamówienia()
zakupy = print(shopping_list)
def łączny_koszt():
    zamówienie = shopping_list
    suma = 0
    for ilość, wydatki in zamówienie.values():
        suma += wydatki
    wynik = print(f'Łączny koszt zamówienia wynosi: {suma} zł')
    return wynik





