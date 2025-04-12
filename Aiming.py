import pygame
import math

def get_angle(self: pygame.Vector2 | tuple, other: pygame.Vector2 | tuple):
    delta_x = other[0] - self[0]
    delta_y = other[1] - self[1]
    theta = math.atan(delta_y / delta_x)
    if delta_x <= 0:
        theta += math.pi
    if delta_x >= 0 and delta_y < 0:
        theta += math.pi * 2
    return theta

def get_vision_angle(player: tuple | pygame.Vector2, mouse: tuple | pygame.Vector2):
    dx = mouse[0] - player[0]
    dy = mouse[1] - player[1]
    return math.degrees(math.atan2(-dy, dx))