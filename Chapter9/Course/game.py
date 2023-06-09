import pygame
import sys
import random
import time
# Initialisation de Pygame
pygame.init()
# Initialisation de la fenêtre de jeu
pygame.display.set_caption('Snake')
# Vitesse du serpent
snake_speed = 20
# Définir la taille de la fenêtre
window_x = 720
window_y = 480

# Définir la couleur
blue = pygame.Color(0, 0, 255)
red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
pink = pygame.Color(255, 192, 203)
violet = pygame.Color(238, 130, 238)
# Initialisation de la fenêtre de jeu
game_window = pygame.display.set_mode((window_x, window_y))
# Contrôleur FPS
fps = pygame.time.Clock()

# Définir la position par défaut du serpent
snake_position = [100, 50]

# Définir les 4 premiers blocs du corps du serpent
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Définir la position de la fruit
fruit_position = [random.randint(0, 72) * 10, random.randint(0, 48) * 10]
fruit_spawn = True
# Score initial
score = 0
# Définir la direction par défaut du serpent à droite
direction = "RIGHT"
change_to = direction

def show_score(color, font, size):
    # Créer un objet police
    score_font = pygame.font.SysFont(font, size)
    # Créer une surface d'arrière-plan de score
    score_surface = score_font.render('Score: ' + str(score), True, color)
    # Créer un objet rectangulaire pour l'objet de surface du texte
    score_rect = score_surface.get_rect();
    # Afficher le score
    game_window.blit(score_surface, score_rect)

def game_over(color, font, size):
    my_font = pygame.font.SysFont(font, size)
    game_over_surface = my_font.render('Your score is: ' + str(score), True, color)
    game_over_rect = game_over_surface.get_rect()
    # game_over_rect.center = (360, 240)
    game_over_rect.midtop = (360, 120)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

while True:
    # Boucle pour les événements et écoute pour le statut de
    # l'événement
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
        # Déterminer si l'utilisateur a cliqué sur le bouton de fermeture 'X'
        # et éxecuter le segment de code "if"
        if event.type == pygame.QUIT:
            # Désinstaller tous les modules
            pygame.quit()
            # Terminer la procédure et assurer la sortie
            sys.exit()

    # Si deux touches sont pressées en même temps
    # Nous ne voulons pas que le serpent se déplace dans deux directions
    # en même temps
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Déplacer le serpent
    if direction == "RIGHT":
        snake_position[0] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10

    # Croissance du corps du serpent
    snake_body.insert(0, list(snake_position))
    if fruit_position[0] == snake_position[0] and fruit_position[1] == snake_position[1]:
        score += 40
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randint(0, 72) * 10, random.randint(0, 48) * 10]

    fruit_spawn = True
    game_window.fill(violet)
    for pos in snake_body:
        pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] > window_x - 10 or snake_position[0] < 0:
        game_over(red, 'times new roman', 50)
    if snake_position[1] > window_y - 10 or snake_position[1] < 0:
        game_over(red, 'times new roman', 50)
    # toucher le serpent
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over(red, 'times new roman', 50)
    show_score(white, "times new roman", 20)

    # Actualiser l'écran de jeu
    pygame.display.update()

    # Taux de rafraîchissement
    fps.tick(snake_speed)

