def password_check(password):
    while True:
        if password == input("Введите пароль: "): return "Пароль верный."
        else: print("Неверный пароль")


key = "1234555"
print(password_check(key))
