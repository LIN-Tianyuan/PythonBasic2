list = [32, 5, 12, 8, 3, 75, 2, 15, 920, 2837, 221, 76, 27, 33]
max_number = list[0]
i = 0
while i < len(list) - 1:
    if max_number < list[i + 1]:
        max_number = list[i + 1]
    i = i + 1

print("Le plus grand élément de cette liste a la valeur %d." %max_number)