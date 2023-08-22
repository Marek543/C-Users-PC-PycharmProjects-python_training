import funkcja

distance = funkcja.turn_to_float(input('Jaki jest przebyty dystans? (km) '))
time = funkcja.turn_to_float(input('Ile zajęło to czasu? (h) '))
print(f'Podróżujesz ze średnią prędkością {funkcja.average_speed(distance, time):.2f} km/h')