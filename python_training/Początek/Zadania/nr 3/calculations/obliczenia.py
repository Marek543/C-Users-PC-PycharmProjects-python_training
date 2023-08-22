
def value(wartość_pocz, procent, liczba_lat):
    wartość_końcowa = wartość_pocz * (1 + procent / 100) ** liczba_lat
    return wartość_końcowa
