def max_number(a, b):
    if a >= b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    for y in range(1, n + 1):
        if y % 2 == 0: yield y


for i in even_numbers(10):
    print(i)


def auto_test():
    assert max_number(10, 10) == 10
    assert max_number(5, 10) == 10
    assert max_number(10, 5) == 10
    assert max_number(-5, 5) == 5
    assert max_number(-5, -10) == -5


auto_test()
