import pygame
from Graphics import screen
from Data import tiles, obstacles, entities, Tile, Obstacle, Entity, Player, TILE_WIDTH, TILE_HEIGHT

map_area = pygame.Rect(0, screen.get_height() - screen.get_height() // 3, screen.get_width() // 3, screen.get_height() // 3)
map_surface = pygame.Surface((map_area.width, map_area.height))

def world_to_minimap(x: float, y: float, player: Player, map_area: pygame.Rect):
    # Ratio of minimap size to screen size
    scale_x = map_area.width / screen.get_width()
    scale_y = map_area.height / screen.get_height()

    # Distance from player to object
    dx = x - player.x
    dy = y - player.y

    # Place relative to center of the map
    center_x = map_area.width // 2
    center_y = map_area.height // 2

    mini_x = center_x + dx * scale_x
    mini_y = center_y + dy * scale_y

    return mini_x, mini_y # Get the position of the object reletave to the mini map

def blit_obstacles_to_map(objects: list, target_surface: pygame.Surface, map_area: pygame.Rect, player: Player):
    scale_x = map_area.width / screen.get_width()
    scale_y = map_area.height / screen.get_height()
    for obj in objects:
        if (obj.x >= 0 - TILE_WIDTH * 3 and obj.x <= screen.get_width() + TILE_WIDTH * 3) and (obj.y >= 0 - TILE_HEIGHT * 3 and obj.y <= screen.get_height() + TILE_HEIGHT * 3):
            try:
                mini_x, mini_y = world_to_minimap(obj.x, obj.y, player, map_area)
            except Exception as e:
                print(f"Error getting mini map x and y: {e}")
            if isinstance(obj, (Tile, Obstacle)):
                try:
                    scaled = pygame.transform.scale(obj.skin, (obj.skin.get_width() * scale_x, obj.skin.get_height() * scale_y))
                    target_surface.blit(scaled, (mini_x, mini_y))
                except Exception as e:
                    print(f"Failed blitting Tile, Obstacle:  {e}")
            elif isinstance(obj, Entity):
                try:
                    scaled = pygame.transform.scale(obj.skin, (obj.skin.get_width() * scale_x, obj.skin.get_height() * scale_y))
                    target_surface.blit(scaled, (mini_x, mini_y))
                except Exception as e:
                    print(f"Failed blitting Entity:  {e}")
            elif isinstance(obj, Player):
                try:
                    scaled = pygame.transform.scale(obj.skin, (obj.skin.get_width() * scale_x, obj.skin.get_height() * scale_y))
                    target_surface.blit(scaled, (mini_x, mini_y))
                except Exception as e:
                    print(f"Failed blitting Player:  {e}")

def update_and_draw(player):
    map_area = pygame.Rect(
        0,
        screen.get_height() - screen.get_height() // 3,
        screen.get_width() // 3,
        screen.get_height() // 3
    )

    map_surface = pygame.Surface((map_area.width, map_area.height))
    map_surface.fill((50, 50, 50))

    blit_obstacles_to_map(tiles, map_surface, map_area, player)
    blit_obstacles_to_map(obstacles, map_surface, map_area, player)
    blit_obstacles_to_map(entities, map_surface, map_area, player)
    blit_obstacles_to_map([player], map_surface, map_area, player)

    screen.blit(map_surface, map_area)