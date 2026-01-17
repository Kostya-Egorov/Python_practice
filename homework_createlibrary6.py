def book_list_view(lib):
    print("Список книг в библиотеке:")
    for name in lib:
        print(name)


def add_book(title, author, year, lib):
    if title in lib:
        if input("Книга с таким названием уже существует, хотите обновить информацию о ней? ").lower().strip() == "да":
            lib[title] = {'Автор': author, 'Год издания': year, "Наличие": None}
        return "Информация о книге обновлена"
    lib[title] = {'Автор': author, 'Год издания': year, "Наличие": None}
    return "Информация о книге добавлена"


def remove_book(title, lib):
    if title in lib:
        del lib[title]
        print(f"Книга '{title}' успешно удалена")
    else:
        print("Такой книги нет в библиотеке")


def issue_book(title, lib):
    if lib[title]["Наличие"] == "Нет в наличии":
        print("Книги нет в библиотеке")
    else:
        lib[title]["Наличие"] = "Нет в наличии"


def return_book(title, lib):
    if lib[title]["Наличие"] == "В наличии":
        print("Книга уже в библиотеке")
    else:
        lib[title]["Наличие"] = "В наличии"


def find_book(title, lib):
    if title in lib:
        if lib[title]['Наличие'] == "В наличии":
            book_access = "Книга доступна"
        elif lib[title]['Наличие'] == "Нет в наличии":
            book_access = "Книга выдана"
        else:
            book_access = "Книга в библиотеке, но ее статус не определен"
        return f"{title} - {lib[title]['Автор']}, {lib[title]['Год издания']}, {book_access}"
    else:
        return "Такой книги не существует"


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

menu = {1: ["Список книг", book_list_view],
        2: ["Добавить книгу", add_book],
        3: ["Удалить книгу", remove_book],
        4: ["Информация о книге", find_book],
        5: ["Отдать книгу", issue_book],
        6: ["Вернуть книгу", return_book]}

while True:
    try:
        for i in menu:
            print(f"{i} - {menu[i][0]}")
        action = int(input("Выберите действие: "))
        if action == 1:
            menu[action][1](library)
        elif action == 2:
            menu[action][1](input("Введите имя книги: "),
                            input("Введите автора книги: "), int(input("Введите дату выпуска книги: ")), library)
        elif action == 3:
            menu[action][1](input("Введите название книги: "), library)
        elif action == 4:
            print(menu[action][1](input("Введите название книги: "), library))
        elif action == 5:
            menu[action][1](input("Введите название книги: "), library)
        elif action == 6:
            menu[action][1](input("Введите название книги: "), library)
        elif action == 0:
            break
        else:
            print("Неверное действие.")
    except ValueError:
        print("Неверный тип данных.")
