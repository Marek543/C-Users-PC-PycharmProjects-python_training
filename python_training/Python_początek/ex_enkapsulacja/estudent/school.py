import random

from estudent.student import Student


class School:

    def __init__(self, name, students):
        self.name = name
        self.students = students
        self.__promote_lucky_students()

    def __promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()

    def __str__(self):
        students = ""
        for student in self.students:
            students += "\n"
            students += str(student)

        return f"School: {self.name}, with {len(self.students)} students: {students}"


def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student_number in range(number_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school