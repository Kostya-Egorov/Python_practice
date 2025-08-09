def countdown(number):
    while number >= 0:
        print(number)
        number -= 1
    return "Готово"


print(countdown(5))
print(countdown(-5))