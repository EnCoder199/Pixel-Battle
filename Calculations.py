import pygame
import math

def round_to_nearest_multiple(number, n):
    return round(number / n) * n

def equalize_lists(lists, padding_value=None):
    max_length = max(len(lst) for lst in lists)
    return [lst + [padding_value] * (max_length - len(lst)) for lst in lists]

def project_polygon(points, axis):
    min_proj = max_proj = points[0].dot(axis)
    for p in points[1:]:
        proj = p.dot(axis)
        min_proj = min(min_proj, proj)
        max_proj = max(max_proj, proj)
    return min_proj, max_proj

def overlap(min1, max1, min2, max2):
    return max1 >= min2 and max2 >= min1

def polygons_collide(poly1: list, poly2: list):
    for polygon in [poly1, poly2]:
        for i in range(len(polygon)):
            p1 = polygon[i]
            p2 = polygon[(i + 1) % len(polygon)]
            edge = p2 - p1
            axis = pygame.Vector2(-edge.y, edge.x).normalize()

            min1, max1 = project_polygon(poly1, axis)
            min2, max2 = project_polygon(poly2, axis)

            if not overlap(min1, max1, min2, max2):
                return False  # Separating axis found

    return True  # No separating axis found, so collision

def get_angled_pos(pos: tuple, theta: float):
    new_x = pos[0] * math.cos(theta) - pos[1] * math.sin(theta)
    new_y = pos[1] * math.cos(theta) + pos[0] * math.sin(theta)
    return (new_x, new_y)