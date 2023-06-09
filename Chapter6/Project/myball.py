import random

myCollection = ['rouge', 'rose', 'orange', 'rouge', 'rose', 'jaune', 'rose', 'jaune']
bag_of_balls = ['rose', 'bleu', 'vert', 'orange', 'rouge', 'pourpre',
                'vert', 'bleu', 'bleu', 'rouge', 'vert', 'poupre',
                'jaune', 'rouge', 'rose', 'rouge', 'vert', 'jaune']
balls_outputs = []

remaining_draws = 5
for x in range(5):
    if remaining_draws > 0:
        selection = random.choice(bag_of_balls)
        balls_outputs.append(selection)
        remaining_draws = remaining_draws - 1
        if selection == 'vert':
            myCollection.append(selection)
            bag_of_balls.remove(selection)
            print("Excellent! Tu as tiré ta bille verte !")
            print("Il restait %d tirages." %remaining_draws)
            break

if not ('vert' in myCollection):
    print("Tous les tirages sont faits. Aucunne bille verte.")
print(balls_outputs)
print("La nouvelle collection contient:")
print(myCollection)



