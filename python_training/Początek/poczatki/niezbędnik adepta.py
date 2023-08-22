
# favourite_sports = ['bieganie', 'pływanie', 'jazda na rowerze', 'triathlon']
# print(favourite_sports[2:])

# def find_best_grade(grades_by_subject):
#     best_grade = 0
#     for subject, grades in grades_by_subject.items():
#         best_grade_from_subject = max(grades)
#         if best_grade_from_subject > best_grade:
#             best_grade = best_grade_from_subject
#     return best_grade
#
# grades_data = {
#     'Historia': [5, 5, 4, 5],
#     'Matematyka': [5, 4, 3, 6],
#     "Fizyka": [4, 3, 2, 5]
# }
# the_best_grade = find_best_grade(grades_data)
# print(f'Najlepsza uzyskana ocena to {the_best_grade}')

import math

print('pi', math.pi)
sinus_180 = math.sin(math.pi)
print('sinus_180', sinus_180)
print('math.inf', math.inf)
very_big_number = 100_000_000_000_000
the_biggest_number = math.inf
print('the_biggest_number > very_big_number', the_biggest_number > very_big_number)