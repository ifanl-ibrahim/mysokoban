import pygame
from pygame.locals import *
import maps
pygame.init()
success = pygame.mixer.Sound("sounds/Pokémon - Capture Sound Effect.mp3")
success.set_volume(1.0)
collision = pygame.mixer.Sound("sounds/Pokémon - Collision - Sound Effect.mp3")
collision.set_volume(1.0)
catch = pygame.mixer.Sound("sounds/Pokémon - Save Game - Sound Effect.mp3")
catch.set_volume(1.0)

# Création des classes Player, Box, Wall, Target
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if not self.collides_with_wall(dx, dy):
            if self.collides_with_box(dx, dy):
                box = get_box(self, self.x + dx, self.y + dy)
                if box and box.move(dx, dy):
                    self.x += dx
                    self.y += dy
                    pygame.display.update()
                    return True
                return False
            else:
                self.x += dx
                self.y += dy
                pygame.display.update()
                return True
        collision.play()
        return False
    
    def collides_with_wall(self, dx, dy):
        return maps.map_data[self.y + dy][self.x + dx] == 'W'

    def collides_with_box(self, dx, dy):
        return maps.map_data[self.y + dy][self.x + dx] == 'B'

def get_box(self, x, y):
    for box in box_list:
        if box.x == x and box.y == y:
            return box
    return None

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if not collides_with_wall(self, new_x, new_y) and not collides_with_box(self, new_x, new_y):
            self.x = new_x
            self.y = new_y
            pygame.display.update()
            return True
        return False
    
def collides_with_wall(self, x, y):
    return maps.map_data[y][x] == 'W'

def collides_with_box(self, x, y):
    return maps.map_data[y][x] == 'B'
        
class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Création des listes
player_list = []
box_list = []
wall_list = []
target_list = []