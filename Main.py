import pygame
from Data import tiles, entities, Player
from Graphics import screen
import Graphics
import Tiles
import Entities
import Projectiles
import Aiming
import HUD
import Calculations
import Mini_map

# Pygame setup
pygame.init()
pygame.display.set_caption("Pixel Battle")
pygame.display.set_icon(Graphics.player)
clock = pygame.time.Clock()
dt = 0
running = True

# Debugging
debug = False

# Setup
player = Player((screen.get_width() / 2, screen.get_height() / 2), 200, 300, 50, Graphics.player)
Tiles.create((10, 10), Graphics.generic_tile)
Tiles.create((11, 10), Graphics.generic_tile)
Entities.create((10, 10), Graphics.test_surface, 20)

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.ammo > 0:
                    Projectiles.create(pygame.Vector2(player.x, player.y + 27), pygame.Vector2(pygame.mouse.get_pos()), pygame.transform.rotate(Graphics.bullet, Aiming.get_vision_angle(player.pos, pygame.mouse.get_pos()) + 180))
                    player.ammo -= 1
            if event.key == pygame.K_r:
                current_time = pygame.time.get_ticks()
                if current_time - player.last_reload >= player.reload_time:
                    player.last_reload = current_time
                    player.ammo = 30

    screen.fill("white")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        temp_tiles, temp_entities = Calculations.balance_lists(tiles, entities) # Equalising the lists so the function does both even if one list is empty
        for (tile, entity) in zip(temp_tiles, temp_entities):
            if tile != None:
                tile.move(0, player.speed * dt)
            if entity != None:
                entity.move(0, player.speed * dt)
    if keys[pygame.K_a]:
        temp_tiles, temp_entities = Calculations.balance_lists(tiles, entities)
        for (tile, entity) in zip(temp_tiles, temp_entities):
            if tile != None:
                tile.move(player.speed * dt)
            if entity != None:
                entity.move(player.speed * dt)
    if keys[pygame.K_s]:
        temp_tiles, temp_entities = Calculations.balance_lists(tiles, entities)
        for (tile, entity) in zip(temp_tiles, temp_entities):
            if tile != None:
                tile.move(0, -(player.speed * dt))
            if entity != None:
                entity.move(0, -(player.speed * dt))
    if keys[pygame.K_d]:
        temp_tiles, temp_entities = Calculations.balance_lists(tiles, entities)
        for (tile, entity) in zip(temp_tiles, temp_entities):
            if tile != None:
                tile.move(-(player.speed * dt))
            if entity != None:
                entity.move(-(player.speed * dt))
    if keys[pygame.K_SPACE] and keys[pygame.K_LSHIFT]:
        if player.ammo > 0:
            Projectiles.create(pygame.Vector2(player.x, player.y + 27), pygame.Vector2(pygame.mouse.get_pos()), pygame.transform.rotate(Graphics.bullet, Aiming.get_vision_angle(player.pos, pygame.mouse.get_pos()) + 180))
            player.ammo -= 1
    
    # View range
    view_range = pygame.transform.rotate(Graphics.view_range_original, Aiming.get_vision_angle(player.pos, pygame.mouse.get_pos()) - 90)
    view_range_rect = view_range.get_rect(center=player.pos)
    previous_view_angle = Aiming.get_vision_angle(player.pos, pygame.mouse.get_pos())

    Tiles.draw()
    Entities.draw()
    player.draw()
    Projectiles.draw()
    Projectiles.update()
    for entity in entities:
        Entities.damage_on_bullet(entity)
    Entities.check_if_dead()
    screen.blit(view_range, view_range_rect)
    HUD.Health.draw(player.health)
    HUD.Ammo.draw(player.ammo)
    Mini_map.update_and_draw(player)
    Projectiles.delete_on_edge()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()