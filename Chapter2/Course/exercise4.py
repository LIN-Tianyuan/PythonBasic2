number = int(input("Veuillez entrer un nombre entier à 4 chiffres: "))
result = number // 1000
result += number // 100 % 10
result += number // 10 % 10
result += number % 10
print(result)

"""
1234 -> 1    1234 // 1000
1234 -> 2    1234 // 100 % 10
1234 -> 3    1234 // 10
1234 -> 4    1234 % 10

1234 ➗ 1000 = 1 …… 234

1234 ➗ 100 = 12 …… 34
12 ➗ 10 = 1 …… 2

1234 ➗ 10 = 123 …… 4
123 ➗ 10 = 12 …… 3
"""
