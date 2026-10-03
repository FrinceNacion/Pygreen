import pygame

class Tower(pygame.sprite.Sprite):
    def __init__(self, name, damage, range, cooldown, position):
        super().__init__()

        self.name = name
        self.damage = damage
        self.range = range
        self.cooldown = cooldown

        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.center = position