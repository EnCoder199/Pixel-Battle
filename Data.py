import pygame
import math
from Graphics import *

class Player:
    def __init__(self, pos: tuple | pygame.Vector2, health: int, speed: float, ammo: int, skin: pygame.Surface, reload_time: int = 5000):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.skin = skin
        self.speed = speed
        self.health = health
        self.ammo = ammo
        self.last_reload = 0
        self.reload_time = reload_time

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

# Obstacle
obstacles = []
class Obstacle:
    x = None
    y = None
    pos = None
    skin = None
    rect = None

    def move(self, x: float = 0, y: float = 0):
        self.x += x
        self.y += y

    def set_skin(self, skin):
        self.skin = skin

    def set_pos(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def change_dimentions(self, x: float = 0, y: float = 0):
        rect = self.rect
        self.rect = pygame.Rect((rect + x) - rect.get_width() / 2, (rect + x) - rect.get_height() / 2, rect.get_width(), rect.get_height())

    def draw(self):
        pos = pygame.Vector2(self.x, self.y)
        skin = pygame.transform.scale(self.skin, self.rect)
        screen.blit(skin, self.rect)

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