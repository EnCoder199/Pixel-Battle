import pygame
from Data import tiles, Tile, TILE_WIDTH, TILE_HEIGHT
import Graphics

def create(pos: tuple | pygame.Vector2, skin: pygame.Surface, resize: bool = True):
    self = Tile()
    self.x = pos[0] * TILE_WIDTH
    self.y = pos[1] * TILE_HEIGHT
    self.pos = (pos[0], pos[1])
    if resize:
        self.skin = pygame.transform.scale(skin, (TILE_WIDTH, TILE_HEIGHT))
    tiles.append(self)
    return self

def draw():
    for tile in tiles:
        tile.draw()

def generate(x: int, y: int, skins: list | pygame.Surface):
    for x in range(x):
        for y in range(y):
            tiles.append(create(pygame.Vector2(x * TILE_WIDTH, y * TILE_HEIGHT), Graphics.test_surface))