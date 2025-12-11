def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)


def calculate_average_all(students):
    average_grade = 0
    for student in students:
        average_grade += calculate_average(student['grades'])
    return round(average_grade / len(students), 2)


def lowest_grade(students):
    lowest_student = students[0]
    lowest_grade = calculate_average(students[0]['grades'])
    for student in students:
        if calculate_average(student['grades']) < lowest_grade:
            lowest_grade = calculate_average(student['grades'])
            lowest_student = student
    return lowest_student


def info(students):
    for student in students:
        status = "Отстающий"
        if calculate_average(student['grades']) >= 75: status = "Успешный"
        print(f"Студент: {student['name']} \n"
              f"Средний балл: {calculate_average(student['grades'])} \n"
              f"Статус: {status} \n")
    print(f"Средний балл всех студентов: {calculate_average_all(students)}\n")
    print(f"Самый отстающий: {lowest_grade(students)['name']}\n")


def add_student(students, name, grades):
    for student in students:
        if student['name'] == name:
            print("Такой студент уже существует.")
            break
    try:
        students.append({'name': name, 'grades': grades})
        print(f"Студент {name} успешно добавлен.")
        info(students)
    except TypeError:
        print(f"У {name} нет оценок.")


def remove_student(students, name):
    for student in students:
        if student['name'] != name:
            continue
        else:
            students.remove(student)
            print(f"Студент {name} успешно удален.")
            info(students)
            return
    print("Такого студента не существует.")


students = [
    {'name': 'Harry', 'grades': [27, 80, 90]},
    {'name': 'Hermione', 'grades': [98, 76, 90]},
    {'name': 'Ron', 'grades': [45, 55, 63]},
    {'name': 'Draco', 'grades': [88, 67, 65]}
]

add_student(students, "Snake", [99, 99, 100])
remove_student(students, lowest_grade(students)['name'])
