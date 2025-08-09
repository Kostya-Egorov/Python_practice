def switch(list):
    buffer = list[0]
    list[0] = list[-1]
    list[-1] = buffer
    return list


list = ["Один", "Два", "Три", "Четыре", "Пять"]
print(switch(list))