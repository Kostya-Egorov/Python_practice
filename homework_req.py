def req():
    summ = 0
    for i in range(2, 100, 2):
        summ += i
    print(f"Сумма всех четных чисел от 1 до 100: {summ}")

    squares = [i ** 2 for i in range(1, 10, 2)]
    print(f"Квадраты всех нечетных чисел от 1 до 10: {squares}")

    count_numbers = 0
    while True:
        if int(input("Введите не отрицательное число: ")) >= 0: count_numbers += 1
        else: break
    print(f"Количество введенных не отрицательных чисел: {count_numbers}")

    return 1


req()
