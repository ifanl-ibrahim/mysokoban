import pygame
from pygame.locals import *
import maps, tools
pygame.init()

# Création des classes Player, Box, Wall, Target
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if maps.map_data[self.y + dy][self.x + dx] == 'W':
            tools.collision.play()
            return
        elif maps.map_data[self.y + dy][self.x + dx] == 'T':
            tools.success.play()
            return
        else :
            self.x += dx
            self.y += dy
            
            
class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x * 70, self.y * 79, tools.image_width, tools.image_height)
        
class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x * 70, self.y * 79, tools.image_width, tools.image_height)

class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Création des listes
player_list = []
box_list = []
wall_list = []
target_list = []