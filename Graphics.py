import pygame
import os

screen = pygame.display.set_mode((1250, 700), pygame.RESIZABLE)

# Debug
test_surface = pygame.image.load(os.path.join("Graphics", "test.png")).convert_alpha()

# View cone
view_range_original = pygame.image.load(os.path.join("Graphics", "view_range.png")).convert_alpha()
view_range_original = pygame.transform.scale(view_range_original, (screen.get_width() * 2.5, screen.get_height() * 2.5))

# Bullet
bullet = pygame.image.load(os.path.join("Graphics", "bullet.png"))
bullet = pygame.transform.scale(bullet, (bullet.get_width() + 5, bullet.get_height() + 5))

# Player
player = pygame.image.load(os.path.join("Graphics", "player.png"))
#player = pygame.transform.scale(player, (player.get_width(), player.get_height()))

class HUD:
    # Bullet
    bullet_cartridge = pygame.image.load(os.path.join("Graphics", "bullet_cartridge.png")).convert_alpha()
    bullet_cartridge = pygame.transform.scale(bullet_cartridge, (bullet_cartridge.get_width() + 15, bullet_cartridge.get_height() + 15))

    # Health
    full_heart = pygame.image.load(os.path.join("Graphics", "full_heart.png")).convert_alpha()
    full_heart = pygame.transform.scale(full_heart, (full_heart.get_width() + 15, full_heart.get_height() + 15))
    half_heart = pygame.image.load(os.path.join("Graphics", "half_heart.png")).convert_alpha()
    half_heart = pygame.transform.scale(half_heart, (half_heart.get_width() + 15, half_heart.get_height() + 15))