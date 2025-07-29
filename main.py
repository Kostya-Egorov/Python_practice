try:
    firstNumber = int(input("Введите первое число: "))
    secondNumber = int(input("Введите второе число: "))
    operand = input("Введите операцию (+, -, *, /): ")
    if operand == "+":
        print("Результат сложения: ", firstNumber + secondNumber, '\n')
    elif operand == "-":
        print("Результат вычитания: ", firstNumber - secondNumber, '\n')
    elif operand == "*":
        print("Результат умножения: ", firstNumber * secondNumber, '\n')
    elif operand == "/":
        print("Результат деления: ", firstNumber / secondNumber, '\n')
    else:
        print("Неправильная операция!")
except ValueError:
    print("Введите число!")
except ZeroDivisionError:
    print("Деление на ноль!")
finally:
    print("Программа завершена.")