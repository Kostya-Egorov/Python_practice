def book_list_view(lib):
    print("Список книг в библиотеке:")
    for name in lib:
        print(name)


def add_book(lib):
    title = input("Введите имя книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите дату выпуска книги: "))
    if title in lib:
        if input("Книга с таким названием уже существует, хотите обновить информацию о ней? ").lower().strip() == "да":
            lib[title] = {'Автор': author, 'Год издания': year, "Наличие": None}
        return "Информация о книге обновлена"
    lib[title] = {'Автор': author, 'Год издания': year, "Наличие": None}
    return "Информация о книге добавлена"


def remove_book(lib):
    title = input("Введите название книги: ")
    if title in lib:
        del lib[title]
        print(f"Книга '{title}' успешно удалена")
    else:
        print("Такой книги нет в библиотеке")


def issue_book(lib):
    title = input("Введите название книги: ")
    if lib[title]["Наличие"] == "Нет в наличии":
        print("Книги нет в библиотеке")
    else:
        lib[title]["Наличие"] = "Нет в наличии"


def return_book(lib):
    title = input("Введите название книги: ")
    if lib[title]["Наличие"] == "В наличии":
        print("Книга уже в библиотеке")
    else:
        lib[title]["Наличие"] = "В наличии"


def find_book(lib):
    title = input("Введите название книги: ")
    if title in lib:
        if lib[title]['Наличие'] == "В наличии":
            book_access = "Книга доступна"
        elif lib[title]['Наличие'] == "Нет в наличии":
            book_access = "Книга выдана"
        else:
            book_access = "Книга в библиотеке, но ее статус не определен"
        print(f"{title} - {lib[title]['Автор']}, {lib[title]['Год издания']}, {book_access}")
    else:
        print("Такой книги не существует")


library = {
    "Капитанская дочка": {
        "Автор": "А.С.Пушкин",
        "Год издания": 1836,
        "Наличие": "В наличии"
    },
    "Мцыри": {
        "Автор": "М.Ю.Лермонтов",
        "Год издания": 1840,
        "Наличие": "Нет в наличии"
    },
    "Крестный отец": {
        "Автор": "Марио Пьюзо",
        "Год издания": 1969,
        "Наличие": "В наличии"}
}

menu = {1: {"Название": "Список книг", "Функция": book_list_view},
        2: {"Название": "Добавить книгу", "Функция": add_book},
        3: {"Название": "Удалить книгу", "Функция": remove_book},
        4: {"Название": "Информация о книге", "Функция": find_book},
        5: {"Название": "Отдать книгу", "Функция": issue_book},
        6: {"Название": "Вернуть книгу", "Функция": return_book},
        0: {"Название": "Выход"}}

while True:
    try:
        for i in menu:
            print(f"{i} - {menu[i]["Название"]}")
        action = int(input("Выберите действие: "))
        if action == 0:
            break
        else:
            menu[action]["Функция"](library)
    except ValueError:
        print("Неверный тип данных.")
