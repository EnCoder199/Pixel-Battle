import pygame
import random
from Data import entities, ENTITY_WIDTH, ENTITY_HEIGHT, Entity, bullets

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
    entities.append(self)
    return self

def draw(self: Entity | None = None):
    if self == None:
        for entity in entities:
            entity.draw()
    elif type(self) == Entity:
        self.draw()

def touching_bullet(self: Entity):
    entity_rect = pygame.Rect(self.x - self.skin.get_width() / 2, self.y - self.skin.get_height() / 2, self.skin.get_width(), self.skin.get_height())
    for bullet in bullets:
        bullet_rect = pygame.Rect(bullet.x - bullet.skin.get_width() / 2, bullet.y - bullet.skin.get_height() / 2, bullet.skin.get_width(), bullet.skin.get_height())
        if pygame.Rect.colliderect(entity_rect, bullet_rect):
            return True
    return False

def damage_on_bullet(self: Entity):
    entity_rect = pygame.Rect(self.x - self.skin.get_width() / 2, self.y - self.skin.get_height() / 2, self.skin.get_width(), self.skin.get_height())
    for bullet in bullets:
        bullet_rect = pygame.Rect(bullet.x - bullet.skin.get_width() / 2, bullet.y - bullet.skin.get_height() / 2, bullet.skin.get_width(), bullet.skin.get_height())
        if pygame.Rect.colliderect(entity_rect, bullet_rect):
            self.health -= bullet.damage
            del bullets[bullets.index(bullet)]

def check_if_dead():
    for entity in entities:
        if entity.health <= 0:
            del entities[entities.index(entity)]