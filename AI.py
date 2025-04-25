import pygame
from Data import *

def check_if_in_range(self: Entity):
    pass # NOTE: Get rect for view area where can shoot and return true if collidrect

class Pathfind:
    def move(entity: Entity, towards: bool = True):
        left = pygame.Vector2(entity.x + 1, entity.y)
        right = pygame.Vector2(entity.x - 1, entity.y)
        up = pygame.Vector2(entity.x, entity.y - 1)
        down = pygame.Vector2(entity.x, entity.y + 1)
        aim_pos = entity.aim_pos

        left_d = (aim_pos.x - left.x)**2 + (aim_pos.y - left.y)**2
        right_d = ((aim_pos.x - right.x)**2 + (aim_pos.y - right.y)**2)
        up_d = ((aim_pos.x - up.x)**2 + (aim_pos.y - up.y)**2)
        down_d = ((aim_pos.x - down.x)**2 + (aim_pos.y - down.y)**2)
        differences = [left_d, right_d, up_d, down_d]

        if towards:
            if max(differences) == left_d:
                entity.move(entity.speed * dt)
            if max(differences) == right_d:
                entity.move(-entity.speed * dt)
            if max(differences) == up_d:
                entity.move(0, -entity.speed * dt)
            if max(differences) == down_d:
                entity.move(0, entity.speed * dt)
        elif not towards:
            if min(differences) == left_d:
                entity.move(entity.speed * dt)
            if min(differences) == right_d:
                entity.move(-entity.speed * dt)
            if min(differences) == up_d:
                entity.move(0, -entity.speed * dt)
            if min(differences) == down_d:
                entity.move(0, entity.speed * dt)