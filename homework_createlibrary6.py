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

while True:
    try:
        action = int(
            input("Выберите действие: \n1 - Список книг\n2 - Добавить книгу\n3 - Удалить книгу\n4 - Информация о книге\n"
                  "5 - Отдать книгу\n6 - Вернуть книгу\n0 - Выход\n"))
        if action == 1:
            book_list_view(library)
        elif action == 2:
            add_book(input("Введите имя книги: "),
                     input("Введите автора книги: "), int(input("Введите дату выпуска книги: ")), library)
        elif action == 3:
            remove_book(input("Введите название книги: "), library)
        elif action == 4:
            print(find_book(input("Введите название книги: "), library))
        elif action == 5:
            issue_book(input("Введите название книги: "), library)
        elif action == 6:
            return_book(input("Введите название книги: "), library)
        elif action == 0:
            break
        else:
            print("Неверное действие.")
    except ValueError:
        print("Неверный тип данных.")
