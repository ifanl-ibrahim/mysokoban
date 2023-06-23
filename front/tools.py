import pygame
from pygame.locals import *
pygame.init()

# Création de la fenêtre
screen_width = 1041
screen_height = 862
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
background = pygame.image.load("assets/background.png")
pygame.display.set_caption("Rocket Catcher")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
check_win = False

# Création des images
image_width = 64
image_height = 64
home_image = pygame.image.load("assets/home.jpg")
finish_image = pygame.image.load("assets/finish.png")
player_image = pygame.transform.scale(pygame.image.load("assets/player_sprite-face.png"), (image_width, image_height))
playerLeft_image = pygame.transform.scale(pygame.image.load("assets/player_sprite-left.png"), (image_width, image_height))
playerRight_image = pygame.transform.scale(pygame.image.load("assets/player_sprite-right.png"), (image_width, image_height))
playerBack_image = pygame.transform.scale(pygame.image.load("assets/player_sprite-back.png"), (image_width, image_height))
wall_image = pygame.transform.scale(pygame.image.load("assets/wall.png"), (image_width, image_height))
target_image = pygame.transform.scale(pygame.image.load("assets/target.png"), (image_width, image_height))

# Création des sons
home_music = pygame.mixer.Sound("sounds/Devise de la Team Rocket.mp3")
music = pygame.mixer.Sound("sounds/Pokémon Musique  - Jadielle, Argenta & Safrania.mp3")
success = pygame.mixer.Sound("sounds/Pokémon - Capture Sound Effect.mp3")
collision = pygame.mixer.Sound("sounds/Pokémon - Collision - Sound Effect.mp3")