
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.assigned_departments = []
        self.__private_info = 'Dane prywatne klasy bazowej'

    def assign_department(self, department):
        self.assigned_departments.append(department)

    def __str__(self):
        return f'Nauczyciel przedmiotu {self.subject} - {self.name}. Uczy klasy: {self.assigned_departments}'

class Tutor(Teacher):
    def __init__(self, name, subject, department):
        super().__init__(name, subject)
        self.guided_department = department

    # def __init__(self, department, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.guided_department = department

    def send_message_from_parents(self, message):
        print(f'Wiadomość od rodziców wysłana: {message}')

def run_example():
    teacher = Teacher(name='Mikołaj', subject='Matematyka')
    teacher.assign_department('C1')
    # print(f'Nauczyciel: {teacher}')

    tutor = Tutor(name='Jakub', subject='Historia', department='A2')
    print(f'Wychowawca nazywa się {tutor.name}')
    tutor.assign_department('A2')
    tutor.assign_department('B1')
    print(f'Wychowawca {tutor}')

    print(tutor.guided_department)
    print(tutor.assigned_departments)
    tutor.send_message_from_parents(message='Pozdrowienia')

    # print(f'Nauczyciel jest typu {type(teacher)}')
    # print(f'Wychowawca jest typu {type(tutor)}')


if __name__ == '__main__':
    run_example()