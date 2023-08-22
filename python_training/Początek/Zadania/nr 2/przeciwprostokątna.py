
import funkcja

bok_nr1 = funkcja.turn_to_float(input('Podaj długośc boku a(cm): '))
bok_nr2 = funkcja.turn_to_float(input('Podaj długośc boku b(cm): '))
print(f'Długość przeciwprostokątnej wynosi {funkcja.hypotenuse_equation(bok_nr1, bok_nr2):.2f} cm')
