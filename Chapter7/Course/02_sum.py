# def sum(number1, number2):
#     print(number1 + number2)
#
# sum(8, 8)

# Paramètre par défaut
# def season_pref(season="Eté"):
#     print("Ma saison préférée est %s." %season)
#
# season_pref("Hiver")

# Paramètre par mot-clé
def list_game(competitor_1, competitor_2, competitor_3):
    print("Concurrents du jour: %s, %s, %s" %(competitor_1, competitor_2, competitor_3))

list_game("Yilong", "Weiqi", "Zhaoxiao")
list_game(competitor_2="Yilong", competitor_3="Weiqi", competitor_1="Zhaoxiao")