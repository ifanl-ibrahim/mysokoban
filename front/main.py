import pygame
from pygame.locals import *
from sys import exit
import classes, tools, maps

# Initialisation de la fenêtre
pygame.init()

# Création des fonctions
def draw_map():
    for y in range(11):
        for x in range(15):
            if maps.map_data[y][x] == 'W':
                tools.screen.blit(tools.wall_image, (x * 70, y * 79))
            elif maps.map_data[y][x] == 'T':
                tools.screen.blit(tools.target_image, (x * 70, y * 79))

def draw_player():
    for player in classes.player_list:
        tools.screen.blit(player.image, (player.x * 70, player.y * 79))

def draw_box():
    for box in classes.box_list:
        tools.screen.blit(box.image, (box.x * 70, box.y * 79))

def draw_target():
    for target in classes.target_list:
        tools.screen.blit(target.image, (target.x * 70, target.y * 79))

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
            player.image = pygame.transform.scale(pygame.image.load("assets/player.png").convert_alpha(), (tools.image_width, tools.image_height))
            classes.player_list.append(player)
        elif maps.map_data[y][x] == 'B':
            box = classes.Box(x, y)
            box.image = pygame.transform.scale(pygame.image.load("assets/box.png").convert_alpha(), (tools.image_width, tools.image_height))
            classes.box_list.append(box)
        elif maps.map_data[y][x] == 'T':
            target = classes.Target(x, y)
            target.image = pygame.transform.scale(pygame.image.load("assets/target.png").convert_alpha(), (tools.image_width, tools.image_height))
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
                player.push(1, 0)
            if event.key == K_LEFT:
                player.move(-1, 0)
                player.push(-1, 0)
            if event.key == K_UP:
                player.move(0, -1)
                player.push(0, -1)
            if event.key == K_DOWN:
                player.move(0, 1)
                player.push(0, 1)

    tools.screen.blit(tools.background, (0, 0))
    draw_map()
    draw_player()
    draw_box()
    draw_target()
    pygame.display.update()