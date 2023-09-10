
# class Student:
#     def __init__(self, name):
#         self.name = name
#     def print_something(self):
#         print('To - ja metoda studenta')
#     def print_self(self):
#         print('Czym jest self?', self)
#         print('Jest tutaj dostęp do name:', self.name)
#     def do_all_work(self):
#         print('Teraz to się napracuję')
#         self.do_piece_of_work()
#         self.do_piece_of_work()
#         self.do_piece_of_work()
#         print('Koniec')
#     def do_piece_of_work(self):
#         print('Robota')
# def run_example():
#     student = Student(name='Mikołaj')
#     student.print_something()
#     student.print_self()
#     student.do_all_work()
#
# if __name__ == '__main__':
#     run_example()

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#         self.final_grades = []
#     def promote(self):
#         self.promoted = True
#
#     def print_self(self):
#         print(f'Student: {self.first_name} {self.last_name}, promoted: {self.promoted}')
#
#     def add_final_grade(self, grade):
#         self.final_grades.append(grade)
#         if grade == 1:
#             self.promoted = False

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#
#     def __repr__(self):
#         return f"<Student first_name='{self.first_name}', last_name='{self.last_name}', promoted={self.promoted}>"
#
#     def __str__(self):
#         return f'Student: {self.first_name} {self.last_name}, promoted: {self.promoted}'
#
#     def __bool__(self):
#         return self.promoted
#
# class School:
#     def __init__(self, name, students):
#         self.name = name
#         self.students = students
#
#     def __repr__(self):
#         students_reprs = []
#         for student in self.students:
#             students_reprs.append(repr(student))
#         all_students_repr = ", ".join(students_reprs)
#
#         return f"<School name='{self.name}', students=[{all_students_repr}]>"
#
#     def __str__(self):
#         students = ""
#         for student in self.students:
#             students += '\n'
#             students += str(student)
#
#         return f'School: {self.name}, with {len(self.students)} students: {students}'
#
#     def __int__(self):
#         return len(self.students)
#
#     def __len__(self):
#         return len(self.students)
#
#
# import random
# def create_school_with_students(school_name):
#     number_of_students = random.randint(1, 20)
#     students = []
#     for student_number in range(number_of_students):
#         first_name = f'Student-{student_number}'
#         last_name = "Smith"
#         students.append(Student(first_name, last_name))
#
#     school = School(school_name, students)
#     return  school

# def run_example():
#     school = create_school_with_students('Hogwart')
    # str_school = str(school)
    # print(str_school)
    # print(school)
    # school_repr = repr(school)
    # print(school_repr)
    # student_repr = repr(school.students[0])
    # print(student_repr)
    # school_as_number = int(school)
    # print(school_as_number)
    # print(len(school))
    # student = Student(first_name='Mikołaj', last_name="Lewandowski")
    # print(bool(student))
    # student.promoted = True
    # print(bool(student))
    # if student:
    #     print('If student')
    # student.promoted = False
    # if student:
    #     print('If student')
    # school.students = []
    # print(bool(school))

class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def as_cents(self):
        return self.dollars * 100 + self.cents

    def __add__(self, other):
        all_cents = self.as_cents() + other.as_cents()
        dollars = int(all_cents / 100)
        cents = all_cents % 100
        return Money(dollars, cents)

    def __str__(self):
        return f'{self.dollars}$ and {self.cents} cents'

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() == other.as_cents()

    def __ne__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() != other.as_cents()

    def __lt__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() < other.as_cents()

    def __le__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() <= other.as_cents()

    def __gt__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() > other.as_cents()

    def __ge__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() >= other.as_cents()

def compare_money_lists(first, second):
    for money in first:
        if money not in second:
            return False
    return True

def run_example():
    # some_money = Money(dollars=100, cents=55)
    # extra_money = Money(dollars=5, cents=80)
    # all_money = some_money + extra_money
    # print(all_money)
    # print(f'{Money(dollars=1, cents=20)} == {Money(dollars=100, cents=5)}?')
    # print(Money(dollars=1, cents=20) == Money(dollars=100, cents=5))
    #
    # print(f'{Money(dollars=100, cents=5)} == {Money(dollars=100, cents=5)}?')
    # print(Money(dollars=100, cents=5) == Money(dollars=100, cents=5))
    #
    # print(f'{Money(dollars=100, cents=5)} != {Money(dollars=100, cents=5)}?')
    # print(Money(dollars=100, cents=5) != Money(dollars=100, cents=5))
    #
    # print(f'{Money(dollars=1, cents=20)} < {Money(dollars=100, cents=5)}?')
    # print(Money(dollars=1, cents=20) < Money(dollars=100, cents=5))
    #
    # print(f'{Money(dollars=1, cents=20)} <= {Money(dollars=100, cents=5)}?')
    # print(Money(dollars=1, cents=20) <= Money(dollars=100, cents=5))
    #
    # print(f'{Money(dollars=1, cents=20)} > {Money(dollars=100, cents=5)}?')
    # print(Money(dollars=1, cents=20) > Money(dollars=100, cents=5))
    #
    # print(f'{Money(dollars=1, cents=20)} >= {Money(dollars=100, cents=5)}?')
    # print(Money(dollars=1, cents=20) >= Money(dollars=100, cents=5))

    some_money = [
        Money(dollars=1, cents=20),
        Money(dollars=10, cents=20),
        Money(dollars=100, cents=20),
        Money(dollars=1000, cents=20),
        Money(dollars=10000, cents=20),
    ]

    other_money = [
        Money(dollars=10000, cents=20),
        Money(dollars=1000, cents=20),
        Money(dollars=100, cents=20),
        Money(dollars=10, cents=20),
        Money(dollars=1, cents=20),
    ]

    # print(f'{Money(dollars=1, cents=20)} in some money?')
    # print(Money(dollars=1, cents=20) in some_money)
    #
    # print(f'{Money(dollars=55, cents=20)} in some money?')
    # print(Money(dollars=55, cents=20) in some_money)

    print(compare_money_lists(some_money, other_money))

if __name__ == '__main__':
    run_example()