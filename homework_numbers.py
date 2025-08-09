def numbers(number):
    if number == 1: return "Один"
    elif number == 2: return "Два"
    elif number == 3: return "Три"
    elif number == 4: return "Четыре"
    elif number == 5: return "Пять"
    return "Число вне диапозона"


def tests():
    assert numbers(1) == "Один"
    assert numbers(2) == "Два"
    assert numbers(3) == "Три"
    assert numbers(4) == "Четыре"
    assert numbers(5) == "Пять"
    assert numbers(6) == "Число вне диапозона"


tests()
print(numbers(int(input("Введите число от 1 до 5: "))))