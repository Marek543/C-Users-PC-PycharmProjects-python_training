import random
# from estudent.school import create_school_with_students
from estudent.school import School
from estudent.student import Student
from estudent.config import Config
from estudent.grade_calculator import GradeCalculator
from estudent import datagenerator
from estudent.department import Department, BioChemDepartment, MathPhysicsDepartment



def final_grades_no_encapsulation(school):
    for student in school.students:
        final_grade = random.randint(1,3)
        student.final_grades.append(final_grade)
    print(school)

def final_grades_with_encapsulation(school):
    for student in school.students:
        final_grade = random.randint(1, 3)
        student.add_final_grade(final_grade)
    print(school)

def grades_avg_for_student(student):
    return student.grades_avg()

# def another_example():
    # school = School.create_school_with_students('Hogwart')
    # students = school.students
    # for student in students:
        # print(student)
        # student.add_final_grade(1, check_promotion_policy=GradeCalculator.strict_promotion_policy)
        # student.add_final_grade(1)
    # print('-' * 20)
    # students.sort(key=grades_avg_for_student, reverse=True)
    # for student in students:
    #     print(student)
    # print('-' * 20)
    # students.sort(key=lambda student: student.grades_avg())
    # for student in students:
    #     print(student)


def run_example():

    # print(Config.ADMINISTRATOR_EMAIL)
    # print(Config.DATABASE_URL)
    # school = School.create_school_with_students('Hogwart')
    # harry = Student(first_name='Harry', last_name='Potter')
    # school.assign_student(harry)
    # print(school)

    # new_school = school.create_school_with_students('New school')
    # print(school.MAX_STUDENTS_NUMBER)
    # print(new_school.MAX_STUDENTS_NUMBER)
    # print(f'W szkole może być maksymalnie {school.MAX_STUDENTS_NUMBER} uczniów')

    # student = school.students[0]
    # student.add_final_grade(5)
    #
    # print(student._Student__final_grades)
    # school._School__promote_lucky_students()

    # for student in school.students:
    #     student.promote()
    #
    # final_grades_no_encapsulation(school)
    # print('=' * 20)
    # final_grades_with_encapsulation(school)

    students = datagenerator.generate_students()
    school = School(name='Hogwart', students=students)
    print(school)

# def example():
#     school = School.create_school_with_students('Hogwart')
#     new_school = school.create_school_with_students('New School')
#
#     print(f'school.MAX_STUDENTS_NUMBER: {school.MAX_STUDENTS_NUMBER}')
#     print(f'new_school.MAX_STUDENTS_NUMBER {new_school.MAX_STUDENTS_NUMBER}')
#
#     print()
#     print('Po modyfikacji na poziomie obiektu')
#     school.MAX_STUDENTS_NUMBER = 125
#     print(f'school.MAX_STUDENTS_NUMBER: {school.MAX_STUDENTS_NUMBER}')
#     print(f'new_school.MAX_STUDENTS_NUMBER {new_school.MAX_STUDENTS_NUMBER}')
#
#     print()
#     print('school self:')
#     school.self_print_max_student_number()
#     print('school cls:')
#     print(school.cls_print_max_student_number())
#
#     print()
#     print('Po modyfikacji na poziomie klasy')
#     School.MAX_STUDENTS_NUMBER = 330
#     print(f'school.MAX_STUDENTS_NUMBER: {school.MAX_STUDENTS_NUMBER}')
#     print(f'new_school.MAX_STUDENTS_NUMBER {new_school.MAX_STUDENTS_NUMBER}')
#
#     print()
#     print('school self:')
#     school.self_print_max_student_number()
#     print('school cls:')
#     print(school.cls_print_max_student_number())
#     another_school = School.create_school_with_students('Other')
#     print('another_school.MAX_STUDENTS_NUMBER:', another_school.MAX_STUDENTS_NUMBER)

def yet_another_example():
    students = datagenerator.generate_students()
    # students.sort(key=lambda student: student.grades_avg(), reverse=True)
    school = School(name='Hogwart', students=students)
    # best_student = school.students[0]
    best_student = school.best_student
    print(f'Średnia najlepszego ucznia: {best_student.grades_avg}')
    # print(f'Oceny najlepszego ucznia: {best_student.get_final_grades()}')
    # print(f'Oceny najlepszego ucznia: {best_student.final_grades}')

def here_we_go_again():
    students = datagenerator.generate_students()
    school = School(name='Hogwart', students=students)
    # print(school)
    print(students.first_student)

    new_students = datagenerator.generate_students(number_of_students=8)
    school.students = new_students
    # print(school)

    # too_many_students = datagenerator.generate_students(number_of_students=100)
    # school.students = too_many_students
    # print(school)

def assign_students_to_department(department, students):
    not_qualified = []
    for student in students:
        if not department.assign_student(student):
            not_qualified.append(student)
    return not_qualified

def ex6():
    students_prefer_bio_chem = datagenerator.generate_students(number_of_students=10)
    students_prefer_math_physics = datagenerator.generate_students(number_of_students=10)
    students = datagenerator.generate_students(number_of_students=5)

    bio_chem_department = BioChemDepartment(letter_identifier='A', year=1)
    math_physics_department = MathPhysicsDepartment(letter_identifier='B', year=1)
    general_department = Department(letter_identifier='C', year=1)

    not_qualified_bio_chem = assign_students_to_department(bio_chem_department, students_prefer_bio_chem)
    not_qualified_math_physics = assign_students_to_department(math_physics_department, students_prefer_math_physics)
    not_qualified = assign_students_to_department(general_department, students)
    not_qualified += assign_students_to_department(general_department, not_qualified_bio_chem)
    not_qualified += assign_students_to_department(general_department, not_qualified_math_physics)

    print(bio_chem_department)
    print(math_physics_department)
    print(general_department)


if __name__ == '__main__':
    ex6()