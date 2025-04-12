import pygame
import random
from Data import *

def create(pos: tuple | pygame.Vector2, skin: pygame.Surface, health: int, speed: float = 250, aim_pos: pygame.Vector2 | None = None, resize: bool = True):
    self = Entity()
    self.x = pos[0]
    self.y = pos[1]
    self.pos = (pos[0], pos[1])
    self.speed = speed
    self.health = health
    if aim_pos == None:
        self.aim_pos = pygame.Vector2(random.randint(int(pos[0]) - 10, int(pos[0]) + 10), random.randint(int(pos[1]) - 10, int(pos[1]) + 10))
    else:
        self.aim_pos = aim_pos
    if resize:
        self.skin = pygame.transform.scale(skin, (ENTITY_WIDTH, ENTITY_HEIGHT))
    return self

def draw(self: Entity | None = None):
    if self == None:
        for entity in entities:
            entity.draw()
    elif type(self) == Entity:
        self.draw()

def is_shot(self):
    self_rect = pygame.Rect(self.x - ENTITY_WIDTH / 2, self.y - ENTITY_HEIGHT / 2, ENTITY_WIDTH, ENTITY_HEIGHT)
    for bullet in bullets:
        bullet_rect = pygame.Rect()