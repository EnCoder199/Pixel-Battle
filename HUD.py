import pygame
from Graphics import *

# Health
heart_value = 20
class Health:
    def draw(health: int):
        left = 10
        top = HUD.full_heart.get_height()
        for n in range(health // 20):
            #screen.blit(HUD.full_heart, (screen.get_width() - (left + n * (HUD.full_heart.get_width() + 3)), top))
            screen.blit(HUD.full_heart, (left + n * (HUD.full_heart.get_width() + 3), top))

class Ammo:
    def draw(ammo: int):
        left = HUD.bullet_cartridge.get_width() + 10
        top = HUD.bullet_cartridge.get_height()
        for n in range(ammo // 4):
            screen.blit(HUD.bullet_cartridge, (screen.get_width() - (left + n * (HUD.bullet_cartridge.get_width() + 3)), top))