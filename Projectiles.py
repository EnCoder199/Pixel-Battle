import pygame
import math
from Data import Bullet
from Data import bullets
from Graphics import screen

def create(pos: tuple | pygame.Vector2, aim: pygame.Vector2, skin: pygame.Surface, damage: int = 2):
    self = Bullet()
    self.x = pos[0]
    self.y = pos[1]
    self.skin = skin
    self.aim = aim
    self.damage = damage

    # Calculate direction vector from bullet to mouse
    dx = self.aim.x - self.x
    dy = self.aim.y - self.y

    # Calculate the length of the vector
    distance = math.sqrt(dx**2 + dy**2)

    # Normalize the vector
    dx /= distance
    dy /= distance

    self.xv = dx * self.speed
    self.yv = dy * self.speed
    
    bullets.append(self)
    return self

def draw():
    for bullet in bullets:
        bullet.draw()

def update():
    for bullet in bullets:
        bullet.update()

def delete_on_edge():
    for bullet in bullets:
        if bullet.x <= 0:
            del bullets[bullets.index(bullet)]
            break
        if bullet.y <= 0:
            del bullets[bullets.index(bullet)]
            break
        if bullet.x >= screen.get_width():
            del bullets[bullets.index(bullet)]
            break
        if bullet.y >= screen.get_height():
            del bullets[bullets.index(bullet)]
            break