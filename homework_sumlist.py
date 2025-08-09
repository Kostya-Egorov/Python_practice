def list_summ(list1, list2):
    list3 = []
    if len(list1) >= len(list2):
        for i in range(len(list2)):
            list3.append(list1[i] + list2[i])
        list3.extend(list1[len(list2):])
    else:
        for i in range(len(list1)):
            list3.append(list1[i] + list2[i])
        list3.extend(list2[len(list1):])
    return list3


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(list_summ(list1, list2))
