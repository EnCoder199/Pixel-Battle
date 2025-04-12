import pygame
from Data import tiles, bullets, Player
from Graphics import screen
import Graphics
import Tiles
import Entities
import Projectiles
import Aiming
import HUD

# Pygame setup
pygame.init()
pygame.display.set_caption("Pixel Battle")
clock = pygame.time.Clock()
dt = 0
running = True

# Debugging
debug = False

# Setup
player = Player((screen.get_width() / 2, screen.get_height() / 2), 200, 5, 50, Graphics.player)
tiles.append(Tiles.create((10, 10), Graphics.test_surface))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.ammo > 0:
                    bullets.append(Projectiles.create(pygame.Vector2(player.x, player.y + 27), pygame.Vector2(pygame.mouse.get_pos()), pygame.transform.rotate(Graphics.bullet, Aiming.get_vision_angle(player.pos, pygame.mouse.get_pos()) + 180)))
                    player.ammo -= 1
            if event.key == pygame.K_r:
                current_time = pygame.time.get_ticks()
                if current_time - player.last_reload >= player.reload_time:
                    player.last_reload = current_time
                    player.ammo = 50

    screen.fill("white")
    Tiles.draw()
    Entities.draw()
    player.draw()
    Projectiles.draw()
    Projectiles.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        for tile in tiles:
            tile.move(0, 300 * dt)
    if keys[pygame.K_a]:
        for tile in tiles:
            tile.move(300 * dt)
    if keys[pygame.K_s]:
        for tile in tiles:
            tile.move(0, -300 * dt)
    if keys[pygame.K_d]:
        for tile in tiles:
            tile.move(-300 * dt)
    if keys[pygame.K_SPACE] and keys[pygame.K_LSHIFT]:
        if player.ammo > 0:
            bullets.append(Projectiles.create(pygame.Vector2(player.x, player.y + 27), pygame.Vector2(pygame.mouse.get_pos()), pygame.transform.rotate(Graphics.bullet, Aiming.get_vision_angle(player.pos, pygame.mouse.get_pos()) + 180)))
            player.ammo -= 1
    
    # View range
    view_range = pygame.transform.rotate(Graphics.view_range_original, Aiming.get_vision_angle(player.pos, pygame.mouse.get_pos()) - 90)
    view_range_rect = view_range.get_rect(center=player.pos)
    previous_view_angle = Aiming.get_vision_angle(player.pos, pygame.mouse.get_pos())

    screen.blit(view_range, view_range_rect)
    HUD.Health.draw(player.health)
    HUD.Ammo.draw(player.ammo)
    Projectiles.delete_on_edge()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()