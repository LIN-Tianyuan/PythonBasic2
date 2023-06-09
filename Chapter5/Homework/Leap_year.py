year = int(input("Veuillez entrer une année: "))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(f"{year} est une année bissextile.")
else:
    print(f"{year} n'est pas une année bissextile.")