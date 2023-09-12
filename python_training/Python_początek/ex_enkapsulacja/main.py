import random
# from estudent.school import create_school_with_students
from estudent.school import School
from estudent.student import Student
from estudent.config import Config
from estudent.grade_calculator import GradeCalculator



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

def another_example():
    school = School.create_school_with_students('Hogwart')
    students = school.students
    for student in students:
        # print(student)
        # student.add_final_grade(1, check_promotion_policy=GradeCalculator.strict_promotion_policy)
        student.add_final_grade(1)
    # print('-' * 20)
    students.sort(key=grades_avg_for_student, reverse=True)
    for student in students:
        print(student)

def run_example():

    # print(Config.ADMINISTRATOR_EMAIL)
    # print(Config.DATABASE_URL)
    school = School.create_school_with_students('Hogwart')
    # harry = Student(first_name='Harry', last_name='Potter')
    # school.assign_student(harry)
    print(school)

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

def example():
    school = School.create_school_with_students('Hogwart')
    new_school = school.create_school_with_students('New School')

    print(f'school.MAX_STUDENTS_NUMBER: {school.MAX_STUDENTS_NUMBER}')
    print(f'new_school.MAX_STUDENTS_NUMBER {new_school.MAX_STUDENTS_NUMBER}')

    print()
    print('Po modyfikacji na poziomie obiektu')
    school.MAX_STUDENTS_NUMBER = 125
    print(f'school.MAX_STUDENTS_NUMBER: {school.MAX_STUDENTS_NUMBER}')
    print(f'new_school.MAX_STUDENTS_NUMBER {new_school.MAX_STUDENTS_NUMBER}')

    print()
    print('school self:')
    school.self_print_max_student_number()
    print('school cls:')
    print(school.cls_print_max_student_number())

    print()
    print('Po modyfikacji na poziomie klasy')
    School.MAX_STUDENTS_NUMBER = 330
    print(f'school.MAX_STUDENTS_NUMBER: {school.MAX_STUDENTS_NUMBER}')
    print(f'new_school.MAX_STUDENTS_NUMBER {new_school.MAX_STUDENTS_NUMBER}')

    print()
    print('school self:')
    school.self_print_max_student_number()
    print('school cls:')
    print(school.cls_print_max_student_number())
    another_school = School.create_school_with_students('Other')
    print('another_school.MAX_STUDENTS_NUMBER:', another_school.MAX_STUDENTS_NUMBER)


if __name__ == '__main__':
    another_example()