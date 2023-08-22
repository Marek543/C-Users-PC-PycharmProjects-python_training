
# def best_grades(grades, best_grades_number=1):
#     grades.sort(reverse=True)
#     if best_grades_number < len(grades):
#         return grades[:best_grades_number]
#     print('Nie można zwrócić więcej ocen niż jest na liście zostaną zwrócone wszystkie')
#     return grades
#
# math_grades = [1, 3, 4, 1, 2, 5, 4]
# print(best_grades(math_grades))
# print(best_grades(math_grades, 4))
# print(best_grades(math_grades, best_grades_number=4))

# print('Domyślny', 'separator')
# print('Własny', 'separator', sep='---')

# def best_grades(best_grades_number=1), grades: #argumenty domyślne na końcu
#     grades.sort(reverse=True)
#     if best_grades_number < len(grades):
#         return grades[:best_grades_number]
#     print('Nie można zwrócić więcej ocen niż jest na liście zostaną zwrócone wszystkie')
#     return grades

# def write_final_grade(subject_grades, final_grades=None):
#     if final_grades is None:
#         final_grades = []
#     grades_avg = sum(subject_grades) / len(subject_grades)
#     final_grades.append(int(grades_avg))
#     return final_grades
#
# john_math_grades = [3, 4, 5, 2, 5]
# john_physics_grades = [4, 4, 4, 4, 4]
# john_final_grades = write_final_grade(subject_grades=john_math_grades)
# john_final_grades = write_final_grade(subject_grades=john_physics_grades, final_grades=john_final_grades)
# print(f'Oceny Johna to {john_final_grades}')

# def do_something_with_default_dict(something=None):
#     if something is None:
#         something ={}
#     print('Tutaj dalsza implementacja')

# def zamiana_liczby_na_zakres(liczba, zakres=0.1):
#     lewa_granica = (liczba) - (liczba * zakres)
#     prawa_granica = (liczba) + (liczba * zakres)
#     return lewa_granica, prawa_granica
#     # return print(f'Zakres dla {liczba} = [{lewa_granica:.2f},{prawa_granica:.2f}]')
#
# print(zamiana_liczby_na_zakres(liczba=100, zakres=0.2))

# def lista_uczniów(lista=None):
#     if lista is None:
#         lista = []
#     while True:
#         uczeń = input('Podaj imię ucznia(wpisz X żeby zakończyć): ')
#         if uczeń == "X":
#             print(f'Lista uczniów to: {lista}')
#             return lista
#         lista.append(uczeń)
# attendance = lista_uczniów()
# lista_uczniów(attendance)

def lista_uczniów(imiona_str, lista=None):
    if lista is None:
        lista = []
    imiona = imiona_str.split(',')
    lista += imiona
    return lista

attendance = 'Marek,Maria,Magda'
list = lista_uczniów(imiona_str=attendance)
spóźniony = 'Bartek,Michał'
print(lista_uczniów(imiona_str=spóźniony, lista=list))
