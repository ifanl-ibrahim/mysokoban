import pygame
from pygame.locals import *
from sys import exit
import classes, tools, maps

# Initialisation de la fenêtre
pygame.init()

# Création des fonctions
def draw_map():
    for y in range(12):
        for x in range(15):
            if maps.map_data[y][x] == 'W':
                tools.screen.blit(tools.wall_image, (x * 70, y * 79))
            elif maps.map_data[y][x] == 'T':
                tools.screen.blit(tools.target_image, (x * 70, y * 79))
            elif maps.map_data[y][x] == 'G':
                tools.screen.blit(tools.wall_image, (x * 70, y * 79))

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
    for y in range(12):
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
            player.image = tools.player_image
            classes.player_list.append(player)
        elif maps.map_data[y][x] == 'B':
            box = classes.Box(x, y)
            box.image = tools.box_image
            classes.box_list.append(box)
        elif maps.map_data[y][x] == 'T':
            target = classes.Target(x, y)
            target.image = tools.target_image
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
                player.image = tools.playerRight_image
                player.move(1, 0)
            if event.key == K_LEFT:
                player.image = tools.playerLeft_image
                player.move(-1, 0)
            if event.key == K_UP:
                player.image = tools.playerBack_image
                player.move(0, -1)
            if event.key == K_DOWN:
                player.image = tools.player_image
                player.move(0, 1)

    tools.screen.blit(tools.background, (0, 0))
    draw_map()
    draw_player()
    draw_box()
    draw_target()
    pygame.display.update()