try:
    print("# Сложение")
    firstNumber = int(input("Введите первое число: "))
    secondNumber = int(input("Введите второе число: "))
    print("Результат сложения: ", firstNumber + secondNumber, '\n')

    print("# Вычитание")
    firstNumber = int(input("Введите первое число: "))
    secondNumber = int(input("Введите второе число: "))
    print("Результат вычитания: ", firstNumber - secondNumber, '\n')

    print("# Умножение")
    firstNumber = int(input("Введите первое число: "))
    secondNumber = int(input("Введите второе число: "))
    print("Результат умножения: ", firstNumber * secondNumber, '\n')

    print("# Деление")
    firstNumber = int(input("Введите первое число: "))
    secondNumber = int(input("Введите второе число: "))
    print("Результат деления: ", firstNumber / secondNumber, '\n')
except ValueError:
    print("Введите число!")
except ZeroDivisionError:
    print("Деление на ноль!")
finally:
    print("Программа завершена.")