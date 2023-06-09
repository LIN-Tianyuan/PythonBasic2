"""
Chapter 1 Introduction
Python est un langage de programmation.

Installation de Python:
    Interpréteur Python
    Pycharm: Éditeur de code
    IDE：Integrated development environment

Fontion de print(): afficher un texte
    print("1+1")  # 1+1
    print(1+1)    # 2

Caractère d'échappement:
    \n saut de ligne (print())


Chapter 2 Variable
Une variable est un nom qui symbolise une valeur.

Définition d'une variable:
    nom_variable = valeur

Un nom de variable est un mot sans espace,
pas commencer par un chiffre, ni par un caractère
spécial.
On utilise souvent le caractère de soulignement
pour séparer les différentes portions du nom d'une
variable. （student_name）

Type de variables(données):
    int: integer
    float: float
    str: string '' " "
    boolean: True False

Connaître le type de données:
    type()

Transtypage:
    int() float() str()

Opérateurs arithmétiques:
    +-*/
    9 / 2 = 4.5
    // faire une division qui reste entière  9 // 2 = 4
    % obtenir le reste 9 % 2 = 1
    ** exponentiation 2 ** 3 = 8       3 ** 2 = 9

input():
    recueillir ce qui est tapé au clavier
    Tout ce que l'utilisateur tape est considéré par Python comme une chaîne de caractères.
    (str)

Chapter 3 Instruction conditionnelle (If)
Opérateurs relationnels:
    == égalité
    != différence
    > supérieur
    < inférieur
    >= supérieur ou égal
    <= inférieur ou égal

Opérateurs logiques:
    and
    or
    not

Instructions conditionnelles:
    1. 1 condition
       if condition:
        action
    2. 2 conditions
       if condition:
        action
       else:
        action
    3. 3+ conditions
       if condition:
        action
       elif:
        action
       else:
        action

Chapter 4 Boucle de répétition
1. for
    for element in variable:
        action

break:      sortir de la boucle
continue:   abréger un tour / continue pour la prochain boucle

2. while
    while condition:
        action
"""

sum = 3.4 + 2.7
sum = int(sum)
print(sum) # 6

print(9 / 2) # 4.5
print(9 // 2) # 4
print(9 % 2) # 1
print(2 ** 3) # 8      2 * 2 * 2 = 8
print("-----------")
print(4 < 5) # True
print(9 < 6) # False
print("-----------")
print(2 < 3 and 5 > 10)  # 2 < 3 => True   5 > 10 => False   True and False => False
print(2 < 3 or 5 > 10)   # 2 < 3 => True   5 > 10 => False   True or False => True
print(not(1 == 1))       # 1 == 1 => True  not True => False
print(8 == 10 and 6 < 7) # 8 == 10 => False 6 < 7 ==> True   False and True => False

for i in range(5):
    print(i) # 0 1 2 3 4

for i in range(3, 6):
    print(i) # 3 4 5

for i in range(2, 10, 2):
    print(i) # 2 4 6 8