import calculations.obliczenia

kapitał = float(input('Jaka jest początkowa wartość kapitału? '))
oprocentowanie = float(input('Jakie jest oprocentowanie? '))
czas = int(input('Jaki jest okres trwania inwestycji? '))

print(f'Wartośc lokaty po {czas} latach będzie wynosić {calculations.obliczenia.value(kapitał, oprocentowanie, czas):.2f} zł')
