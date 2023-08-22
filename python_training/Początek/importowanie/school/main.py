# from school import promotion_status
from school import promotion_status as status
from school.grade_calculator import calculate_student_final_grades
# from school.promote import check_promotion
from school.promote import check_promotion as promotion_checker
from school.students_data import is_student_in_school

def check_student_promotion():
    student_name = input('Podaj imię ucznia żeby dowiedzieć się czy zdał do następnej klasy: ')

    if not is_student_in_school(student_name):
        print(f'Niestety {student_name} nie ma na liście')
    else:
        final_grades = calculate_student_final_grades(student_name)
        promotion_result = promotion_checker(final_grades)

        if promotion_result == status.PASSED:
            print(f'{student_name} zdał do następnej klasy')
        elif promotion_result == status.FAILED:
            print(f'{student_name} nie zdał do następnej klasy')
        else:
            print('Coś poszło nie tak, zgłoś to do obsługi')