try:
    firstNumber = int(input("Введите первое число: "))
    secondNumber = int(input("Введите второе число: "))
    print("Результат: ", firstNumber / secondNumber)
except ValueError:
    print("Вы ввели не число!")
except ZeroDivisionError:
    print("Попытка деления на ноль!")
finally:
    print("Работа завершена.")