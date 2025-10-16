students = [
    {'name': 'Harry', 'grades': [27, 80, 90]},
    {'name': 'Hermione', 'grades': [98, 76, 90]},
    {'name': 'Ron', 'grades': [45, 55, 63]},
    {'name': 'Draco', 'grades': [88, 67, 65]}
]


def calculate_average(grades):
    average_grade = 0
    for grade in grades:
        average_grade += grade
    return average_grade / len(grades)


def info():
    for student in students:
        status = "Отстающий"
        if calculate_average(student['grades']) >= 75: status = "Успешный"
        print(f"Студент: {student['name']} \n"
              f"Средний балл: {calculate_average(student['grades'])} \n"
              f"Статус: {status} \n")


def add_student(name, grades):
    students.append({'name': name, 'grades': grades})
    info()


def remove_student(name, grades):
    for student in students:
        if student['name'] == name:
            students.remove(student)


add_student("Snake", [98, 95, 100])
