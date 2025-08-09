def countdown(number):
    while number >= 0:
        print(number)
        number -= 1
    return "Готово"


print(countdown(int(input("Введите число для обратного отсчета: "))))
