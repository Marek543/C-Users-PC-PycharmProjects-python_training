
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

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self.final_grades = []
    def promote(self):
        self.promoted = True

    def print_self(self):
        print(f'Student: {self.first_name} {self.last_name}, promoted: {self.promoted}')

    def add_final_grade(self, grade):
        self.final_grades.append(grade)
        if grade == 1:
            self.promoted = False