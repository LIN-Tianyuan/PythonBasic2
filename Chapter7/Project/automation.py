def welcome():
    name_visitor = \
        input("Merci de contacter Thibault! Je peux avoir votre prénom ? ")
    print("Bienvenue chez Thibault, %s!" % name_visitor)

def choose_category():
    print('*** Menu général Thibault *** \n'
          '[1] Horaires & Accès\n'
          '[2] Gestion de commande \n'
          '[3] Suivi de livraison \n'
          '[4] Suggestion de produit\n'
          '[5] Autre sujet')
    cCatego = input("Choisissez une des catégories en tapant un chiffre entre 1 et 5:")
    if cCatego == '1':
        shop_info()
        return
    if cCatego == '2':
        order_management()
        return
    if cCatego == '3':
        tracking_deliveries()
        return
    if cCatego == '4':
        service_marketing()
        return
    if cCatego == '5':
        others()
        return
    if cCatego not in ['1', '2', '3', '4', '5']:
        choose_category()

def shop_info():
    address = "148 Boulevard Masséna 75013 PARIS"
    schedule = "du Lundi au Samedi 10h - 18h"
    print(f"\nThibault se retrouve au {address}, \nLa boutique est ouverte {schedule}.")
    other = input("Autre chose ?[y/n]").lower()
    if other == 'y':
        choose_category()
    else:
        print("Merci de nous avoir contacté.")
    return

def order_management():
    print("\nVous êtes au service de gestion des commandes.")
    client_name = input("Nom indiqué sur le bon de commande:")
    order_number = input("Indiquez le numéro de commande:")
    transfer_Eillot()
    return

def transfer_Eillot():
    print("Parfait! Je vérifie le status de votre commande.")
    return

def tracking_deliveries():
    print("Nous sommes désoles que vous avez subi un souci avec votre commande.")
    client_name = input("Nom indiqué sur le bon de commande:")
    order_number = input("Indiquez le numéro de commande:")
    follow = input("Décrivez votre problème:")
    transfer_Christine()
    return

def service_marketing():
    print("Nous vous remercions pour votre suggestion et "
          "allons vous mettre en relation avec le service concerné.")
    transfer_Raoul()

def others():
    transfer_Therese()
    return

def transfer_Christine():
    print("Merci pour vos détails. Nous vérifions votre commande et vous recontactons au plus vite.")
    return

def transfer_Raoul():
    suggestion_marketing = input("Dites-moi quel autre produit nous devrions proposer:")
    return

def transfer_Therese():
    other_info = input("De quoi aimeriez-vous nous informer?")
    return


welcome()
choose_category()