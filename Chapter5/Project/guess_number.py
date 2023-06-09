import random
random_number = random.randint(1, 100)
count = 0
while True:
    if count == 5:
        print("Game over, vous avez échoué!")
        break
    number = int(input("Veuillez entrer un nombre: "))
    count = count + 1
    if number < random_number:
        print("Plus petit.")
    elif number > random_number:
        print("Plus grand.")
    else:
        print("Vous avez bien deviné " + str(count) + " fois au total.")
        break
