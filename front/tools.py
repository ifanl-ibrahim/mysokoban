import pygame
from pygame.locals import *
pygame.init()

# Création de la fenêtre
screen_width = 1041
screen_height = 862
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
background = pygame.image.load("assets/background.png").convert()
pygame.display.set_caption("Sokoban")

# Création des images
image_width = 64
image_height = 64
player_image = pygame.transform.scale(pygame.image.load("assets/player.png").convert_alpha(), (image_width, image_height))
box_image = pygame.transform.scale(pygame.image.load("assets/box.png").convert_alpha(), (image_width, image_height))
boxValid_image = pygame.transform.scale(pygame.image.load("assets/boxValid.png").convert_alpha(), (image_width, image_height))
wall_image = pygame.transform.scale(pygame.image.load("assets/wall.png").convert_alpha(), (image_width, image_height))
target_image = pygame.transform.scale(pygame.image.load("assets/target.png").convert_alpha(), (image_width, image_height))

# Création des sons
music = pygame.mixer.Sound("sounds/Pokémon Musique  - Jadielle, Argenta & Safrania.mp3")
music.set_volume(0.3)
music.play(-1)

success = pygame.mixer.Sound("sounds/Pokémon - Capture Sound Effect.mp3")
success.set_volume(1.0)

collision = pygame.mixer.Sound("sounds/Pokémon - Collision - Sound Effect.mp3")
collision.set_volume(1.0)

catch = pygame.mixer.Sound("sounds/Pokémon - Save Game - Sound Effect.mp3")
catch.set_volume(1.0)