import pygame
import math
from Graphics import *

# Entity
entities = []
ENTITY_WIDTH = 64
ENTITY_HEIGHT = 64

class Entity:
    x = None
    y = None
    pos = None
    skin = None
    aim_pos = None
    speed = None
    health = None

    def move(self, x: float = 0, y: float = 0):
        self.x += x
        self.y += y

    def set_skin(self, skin):
        self.skin = skin

    def set_pos(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def draw(self):
        pos = pygame.Vector2(self.x, self.y)
        skin = self.skin
        screen.blit(skin, pos)

# Tile
tiles = [] # tiles only has Tile(s) inside
TILE_WIDTH = 64
TILE_HEIGHT = 64

class Tile:
    x = None
    y = None
    pos = None
    skin = None

    def move(self, x: float = 0, y: float = 0):
        self.x += x
        self.y += y

    def set_skin(self, skin):
        self.skin = skin

    def set_pos(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def draw(self):
        pos = pygame.Vector2(self.x, self.y)
        skin = self.skin
        screen.blit(skin, pos)

# Bullet
bullets = []
#BULLET_WIDTH = 
#BULLET_HEIGHT = 
class Bullet:
    x = None
    y = None
    damage = None
    skin = None
    aim = None
    speed = 10
    xv = None
    yv = None

    def move(self, x: float = 0, y: float = 0):
        self.x += x
        self.y += y

    def set_skin(self, skin):
        self.skin = skin

    def set_pos(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
    
    def update(self):
        self.x += self.xv
        self.y += self.yv

    def draw(self):
        pos = pygame.Vector2(self.x, self.y)
        skin = self.skin
        screen.blit(skin, pos)