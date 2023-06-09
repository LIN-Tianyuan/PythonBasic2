# Importation des modules requis
import pygame
import sys
# Initialiser avant d'utiliser pygame
pygame.init()
# Configuration de la fênêtre de l'écran d'accueil
screen = pygame.display.set_mode((400, 400))
# Configuration de la couleur d'arrière-plan
screen.fill('white')
# Définir le titre de la fenêtre (nom du jeu)
pygame.display.set_caption('My first game')
# Introduction des types de polices
f = pygame.font.SysFont('Arial', 50)
# Génère un message texte
# Premier paramètre: contenu du texte
# Deuxième paramètre: la police est lisse ou non
# Troisième paramètre: la couleur de la police en mode RGB
# Quatrième paramètre: la couleur de fond en mode RGB
text = f.render("Happy game", True, (0,255,0), (255,255,255))
# Obtenir les coordonnées de la zone rectangulaire de l'objet affiché
textRect = text.get_rect()
# Définir l'objet d'affichage pour qu'il soit centré
textRect.center = (200, 200)
# Prendre le message texte préparé et dessiner-le sur l'écran d'accueil
screen.blit(text, textRect)

while True:
    # Boucle pour les événements et écoute pour le statut de
    # l'événement
    for event in pygame.event.get():
        # Déterminer si l'utilisateur a cliqué sur le bouton de fermeture 'X'
        # et éxecuter le segment de code "if"
        if event.type == pygame.QUIT:
            # Désinstaller tous les modules
            pygame.quit()
            # Terminer la procédure et assurer la sortie
            sys.exit()
    # Mise à jour du contenu de l'écran
    pygame.display.flip()

