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
        if maps.map_data[self.y + dy][self.x + dx] != 'W':
            self.x += dx
            self.y += dy
        else :
            tools.collision.play()
            return
        
    def push(self, dx, dy):
        if maps.map_data[self.y + dy][self.x + dx] == 'B':
            box_hit = Box(self.x + dx, self.y + dy) 
            if maps.map_data[self.y + dy * 2][self.x + dx * 2] != 'W' and maps.map_data[self.y + dy * 2][self.x + dx * 2] != 'B':
                self.x += dx
                self.y += dy
                for box in box_list:
                    if box_hit.x == self.x and box_hit.y == self.y:
                        box_hit.x += dx
                        box_hit.y += dy
                        for target in target_list:
                            if box_hit.x == target.x and box_hit.y == target.y:
                                box.image = pygame.transform.scale(pygame.image.load("assets/boxValid.png").convert_alpha(), (tools.image_width, tools.image_height))
                                tools.catch.play()
            else:
                tools.collision.play()
                return
            
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