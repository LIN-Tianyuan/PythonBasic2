price_str = input("Veuillez entrer le prix des pommes: ")
weight_str = input("Veuillez entrer le poids des pommes: ")

money = float(price_str) * float(weight_str)
print("Vous devez payer " + str(money) + " euros.")
