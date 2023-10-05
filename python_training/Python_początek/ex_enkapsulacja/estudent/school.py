import random
from estudent.config import Config
from estudent.student import Student


class School:

    MAX_STUDENTS_NUMBER = 50
    MAX_STUDENTS_PER_DEPARTMENT = 15

    def __init__(self, name, students):
        self.name = name
        self._students = students
        self.__promote_lucky_students()
        self.departments = self._split_students_to_departments()

    @property
    def students(self):
        return self._students

    def __promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()

    def _split_students_to_departments(self):
        departments = {}
        departments_letters = ['A', 'B', 'C', 'D', 'E', 'F']
        current_department_number = -1
        for index, student in enumerate(self.students):
            if index % School.MAX_STUDENTS_PER_DEPARTMENT == 0:
                current_department_number += 1
            current_department = departments_letters[current_department_number]
            if current_department not in departments:
                departments[current_department] = []
            departments[current_department].append(student)
        return departments

    def __str__(self):
        result = ''
        for department_name, students_in_department in self.departments.items():
            result += f'Oddział {department_name}\n'
            for student  in students_in_department:
                result += f'{student}\n'
        return f'Szkoła: {self.name}, z {len(self.students)} uczniami: \n{result}'
        # students = ""
        # for student in self.students:
        #     students += "\n"
        #     students += str(student)
        #
        # return f"School: {self.name}, with {len(self.students)} students: {students}"

    @students.setter
    def students(self, value):
        if len(value) < School.MAX_STUDENTS_NUMBER:
            self._students = value
        else:
            print('Nie ma już miejsca!')
            self._students = value[:School.MAX_STUDENTS_NUMBER]
        self.departments = self._split_students_to_departments()


    @classmethod
    def create_school_with_students(cls, school_name):
        number_of_students = random.randint(1, cls.MAX_STUDENTS_NUMBER)
        school = School(school_name, students=[])

        for student_number in range(number_of_students):
            first_name = f"Student-{student_number}"
            last_name = "Smith"
            student = Student(first_name, last_name)
            school.assign_student(student)
            for _ in range(Config.RANDOM_FINAL_GRADES_NUMBER):
                final_grade = random.randint(Config.MIN_RANDOM_GRADE, Config.MAX_RANDOM_GRADE)
                student.add_final_grade(final_grade)
        return school

        # students = []
        # for student_number in range(number_of_students):
        #     first_name = f"Student-{student_number}"
        #     last_name = "Smith"
        #     students.append(Student(first_name, last_name))
        #
        # school = School(school_name, students)
        # return school

    def assign_student(self, student):
        if len(self.students) < self.MAX_STUDENTS_NUMBER:
            self.students.append(student)
        else:
            print('Nie ma już miejsca')

    @property
    def best_student(self):
        if len(self.students):
            return sorted(self.students, key=lambda student: student.grades_avg, reverse=True)[0]
        return None

    # def self_print_max_student_number(self):
    #     print(self.MAX_STUDENTS_NUMBER)
    #
    # @classmethod
    # def cls_print_max_student_number(cls):
    #     print(cls.MAX_STUDENTS_NUMBER)