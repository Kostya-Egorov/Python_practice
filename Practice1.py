def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)


def info(students):
    for student in students:
        status = "Отстающий"
        if calculate_average(student['grades']) >= 75: status = "Успешный"
        print(f"Студент: {student['name']} \n"
              f"Средний балл: {calculate_average(student['grades'])} \n"
              f"Статус: {status} \n")


def add_student(students, name, grades):
    for student in students:
        if student['name'] == name:
            print("Такой студент уже существует.")
            break
    try:
        students.append({'name': name, 'grades': grades})
        print("Студент успешно добавлен.")
        info(students)
    except TypeError:
        print(f"У {name} нет оценок.")


def remove_student(students, name):
    for student in students:
        if student['name'] != name:
            continue
        else:
            students.remove(student)
            print("Студент успешно удален.")
            break
    print("Такого студента не существует.")


students = [
    {'name': 'Harry', 'grades': [27, 80, 90]},
    {'name': 'Hermione', 'grades': [98, 76, 90]},
    {'name': 'Ron', 'grades': [45, 55, 63]},
    {'name': 'Draco', 'grades': [88, 67, 65]}
]

add_student(students, "Snake", None)
