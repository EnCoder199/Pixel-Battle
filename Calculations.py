import pygame

def round_to_nearest_multiple(number, n):
    return round(number / n) * n

def balance_lists(a: list, b: list):
    a = a.copy()
    b = b.copy()

    a_length = len(a)
    b_length = len(b)

    if a_length > b_length:
        list_dif = a_length - b_length
        for _ in range(list_dif):
            b.append(None)

    elif a_length < b_length:
        list_dif = b_length - a_length
        for _ in range(list_dif):
            a.append(None)
    
    return a, b

def project_polygon(points, axis):
    min_proj = max_proj = points[0].dot(axis)
    for p in points[1:]:
        proj = p.dot(axis)
        min_proj = min(min_proj, proj)
        max_proj = max(max_proj, proj)
    return min_proj, max_proj

def overlap(min1, max1, min2, max2):
    return max1 >= min2 and max2 >= min1

def polygons_collide(poly1, poly2):
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

# Example usage
poly1 = [pygame.Vector2(100, 100), pygame.Vector2(150, 100), pygame.Vector2(125, 150)]
poly2 = [pygame.Vector2(130, 130), pygame.Vector2(180, 130), pygame.Vector2(155, 180)]

if polygons_collide(poly1, poly2):
    print("Polygons are colliding!")
