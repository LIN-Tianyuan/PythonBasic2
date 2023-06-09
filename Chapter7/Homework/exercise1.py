def indexMax(list):
    max_number = list[0]
    i = 0
    while i < len(list) - 1:
        if max_number < list[i + 1]:
            max_number = list[i + 1]
        i = i + 1
    return list.index(max_number)


list = [5, 8, 2, 1, 9, 3, 6, 7]
print(indexMax(list))
