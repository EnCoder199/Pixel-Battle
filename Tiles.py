import pygame
from Data import *

def create(pos: tuple | pygame.Vector2, skin: pygame.Surface, resize: bool = True):
    self = Tile()
    self.x = pos[0]
    self.y = pos[1]
    self.pos = (pos[0], pos[1])
    if resize:
        self.skin = pygame.transform.scale(skin, (TILE_WIDTH, TILE_HEIGHT))
    return self

def draw():
    for tile in tiles:
        tile.draw()

def generate(x: int, y: int):
    for x in range(x):
        for y in range(y):
            tiles.append(create(pygame.Vector2(x * TILE_WIDTH, y * TILE_HEIGHT), test_surface))