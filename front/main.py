import pygame
from pygame.locals import *
from sys import exit
import maps
import classes

# Initialisation de la fenêtre
pygame.init()

# Création de la fenêtre
screen_width = 1041
screen_height = 862
image_width = 64
image_height = 64
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
music = pygame.mixer.Sound("sounds/Pokemon Musique  - Jadielle, Argenta & Safrania.mp3")
music.set_volume(0.3)
background = pygame.image.load("assets/background.png").convert()
player = pygame.transform.scale(pygame.image.load("assets/player.png").convert_alpha(), (image_width, image_height))
box = pygame.transform.scale(pygame.image.load("assets/box.png").convert_alpha(), (image_width, image_height))
boxValid = pygame.transform.scale(pygame.image.load("assets/boxValid.png").convert_alpha(), (image_width, image_height))
wall = pygame.transform.scale(pygame.image.load("assets/wall.png").convert_alpha(), (image_width, image_height))
target = pygame.transform.scale(pygame.image.load("assets/target.png").convert_alpha(), (image_width, image_height))
pygame.display.set_caption("Sokoban")
music.play(-1)

# Création des fonctions
def draw_map():
    for y in range(11):
        for x in range(15):
            if maps.map_data[y][x] == 'W':
                screen.blit(wall, (x * 70, y * 79))
            elif maps.map_data[y][x] == 2:
                screen.blit(target, (x * 70, y * 79))

def draw_player():
    for player in classes.player_list:
        screen.blit(player.image, (player.x * 70, player.y * 79))

def draw_box():
    for box in classes.box_list:
        screen.blit(box.image, (box.x * 70, box.y * 79))

def draw_target():
    for target in classes.target_list:
        screen.blit(target.image, (target.x * 70, target.y * 79))

# Redemarre le jeu
def restart():
    for y in range(11):
        for x in range(15):
            if maps.map_data[y][x] == 'P':
                player.x = x
                player.y = y
            elif maps.map_data[y][x] == 'B':
                box.x = x
                box.y = y
            elif maps.map_data[y][x] == 'T':
                target.x = x
                target.y = y

# Création des instances
for y in range(11):
    for x in range(15):
        if maps.map_data[y][x] == 'P':
            player = classes.Player(x, y)
            player.image = pygame.transform.scale(pygame.image.load("assets/player.png").convert_alpha(), (image_width, image_height))
            classes.player_list.append(player)
        elif maps.map_data[y][x] == 'B':
            box = classes.Box(x, y)
            box.image = pygame.transform.scale(pygame.image.load("assets/box.png").convert_alpha(), (image_width, image_height))
            classes.box_list.append(box)
        elif maps.map_data[y][x] == 'T':
            target = classes.Target(x, y)
            target.image = pygame.transform.scale(pygame.image.load("assets/target.png").convert_alpha(), (image_width, image_height))
            classes.target_list.append(target)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            if event.key == K_SPACE:
                restart()
            if event.key == K_RIGHT:
                player.move(1, 0)
            if event.key == K_LEFT:
                player.move(-1, 0)
            if event.key == K_UP:
                player.move(0, -1)
            if event.key == K_DOWN:
                player.move(0, 1)

    screen.blit(background, (0, 0))
    draw_map()
    draw_player()
    draw_box()
    draw_target()
    pygame.display.update()