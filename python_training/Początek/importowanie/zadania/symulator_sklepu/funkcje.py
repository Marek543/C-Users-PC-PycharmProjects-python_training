from .oferta import czy_produkt_jest_w_sklepie
from .oferta import znajdź_ilość, wyznacz_cene_jednostkową

def składanie_zamówienia():
    lista_zamówień = {}
    nazwa_produktu = ""

    while nazwa_produktu != 'X':
        nazwa_produktu = input('Podaj nazwę produktu który chcesz zamówić(wpisz X żeby przerwać): ')
        while czy_produkt_jest_w_sklepie(nazwa_produktu) == False and nazwa_produktu != 'X':
            nazwa_produktu = input('Niestety nie ma takiego produktu w sklepie podaj nazwę innego produktu który chcesz zamówić(wpisz X żeby przerwać): ')
        if nazwa_produktu != 'X':
            lista_zamówień[nazwa_produktu] = []
            ilość_produktu = obliczanie_ilości(nazwa_produktu)
            lista_zamówień[nazwa_produktu].append(ilość_produktu)
            koszt_produktu = obliczanie_ceny_zamówienia(nazwa_produktu, ilość_produktu)
            lista_zamówień[nazwa_produktu].append(koszt_produktu)

    return lista_zamówień

def obliczanie_ilości(nazwa_produktu):
    ilość = int(input('Podaj ile sztuk chcesz zamówić: '))
    while ilość > znajdź_ilość(nazwa_produktu):
        ilość = int(input(f'Niestety w sklepie znajduje się jedynie {znajdź_ilość(nazwa_produktu)} sztuk, podaj ile sztuk z dostępnego zakresu chcesz zamówić: '))
    return ilość

def obliczanie_ceny_zamówienia(nazwa_produktu, ilość_produktu):
    cena = wyznacz_cene_jednostkową(nazwa_produktu)
    koszt = ilość_produktu * cena
    return koszt






