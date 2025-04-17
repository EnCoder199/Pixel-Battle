import pygame
from Data import Obstacle, obstacles

def create(pos: tuple | pygame.Vector2, skin: pygame.Surface, rect: pygame.Rect):
    self = Obstacle()
    self.x = pos[0]
    self.y = pos[1]
    self.pos = (pos[0], pos[1])
    self.skin = skin
    self.rect = rect
    return self

def draw():
    for obstacle in obstacles:
        obstacle.draw()