score = int(input("Veuillez entrer votre score: "))
if score >= 60:
    print("Vous avez passé.")
    if score >= 80: # > 80
        print("Vous êtes très bon.")
    else:
        print("Vous êtes juste dans la moyenne.")
else:
    print("Éhec à la réussite.")
    if score < 30:
        print("De très mauvaises notes.")
    else:
        print("Il faut continuer à faire du bon travail.")