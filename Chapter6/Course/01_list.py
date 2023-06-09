"""
leisure1 = "swim"
leisure2 = "dance"
leisure3 = "sing"

list
"""
# Création d'une liste
leisures = ['swim', 'dance', 'sing']
print(leisures)
# Longueur d'une liste
print(len(leisures))
# Test de présence d'un élément
print('basketball' in leisures)
print('dance' in leisures)
print('DANCE' in leisures)
print('----------')
# Obtenir l'index d'un élément
print(leisures.index('swim'))   # 0
print(leisures.index('dance'))  # 1
print('----------')
# Accéder aux éléments d'une liste
print(leisures[0]) # swim
print(leisures[1]) # dance
print('----------')
# Modifier la valeur d'un élément d'une liste
leisures[0] = 'ski'
print(leisures)
print('----------')
# Ajouter un élément à une liste
leisures.append('game')
print(leisures)
print('----------')
# Insérer un élément ailleurs qu'à la fin
leisures.insert(3, 'climb')
print(leisures)
print(leisures.index('game')) # 4
print('----------')
# Enlever un élément dans une liste
leisures.remove('climb')
print(leisures)
print('----------')
# Enlever un élément avec son index
leisures.pop(1)
print(leisures)
print('----------')
# Vider une liste
leisures.clear()
print(leisures)
print('----------')
# Concaténer deux listes
month = ['Janvier', 'Février', 'Mars']
season = ['Automne', 'Hiver', 'Printemps', 'Eté']
various_times = month + season
print(month)
print(various_times)
print('----------')
# Étendre une liste
month.extend(season)
print(month)
print(season)
print('----------')
# Créer une tranche de liste
rainbow = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
# Connaître la longueur de la liste
print(len(rainbow))
print(rainbow[1:4])
print(rainbow[3:])      # print(rainbow[3:7])
print(rainbow[:5])      # print(rainbow[0:5])
print(rainbow[-5:-2])   # print(rainbow[2:5])