def book_list_view(library):
    for name in library:
        print(f"{name} - {library[name]['Автор']}, {library[name]['Год издания']}, {library[name]['Наличие']}")


def add_book(title, author, year):
    if title in library:
        print("Книга с таким названием уже существует, хотите обновить информацию о ней?")
        if input() != "Да":
            return None
        else:
            library[title] = {'Автор': author, 'Год издания': year, "Наличие": None}
        return print("Информация о книге обновлена")
    library[title] = {'Автор': author, 'Год издания': year, "Наличие": None}
    return print("Информация о книге добавлена")


def remove_book(title):
    if title in library:
        del library[title]
        print(f"Книга '{title}' успешно удалена")
    else:
        print("Такой книги нет в библиотеке")


def issue_book(title):
    library[title]["Наличие"] = "Нет в наличии"


def return_book(title):
    library[title]["Наличие"] = "В наличии"


library = {"Капитанская дочка": {"Автор": "А.С.Пушкин", "Год издания": 1836, "Наличие": "В наличии"},
           "Мцыри": {"Автор": "М.Ю.Лермонтов", "Год издания": 1840, "Наличие": "Нет в наличии"},
           "Крестный отец": {"Автор": "Марио Пьюзо", "Год издания": 1969, "Наличие": "В наличии"}}

add_book("Мцыри", "М.Ю.Лермонтов", 1999)
remove_book("Крестный отец")
issue_book("Капитанская дочка")
return_book("Мцыри")
book_list_view(library)
