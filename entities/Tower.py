import pygame

class Tower(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.name = 'none'
        self.damage = 0
        self.range = 0
        self.cooldown = 0

        self.last_shot_time = 0

        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.center = position

    def set_tower_properties(self, name, damage, range, cooldown):
        self.name = name
        self.damage = damage
        self.range = range
        self.cooldown = cooldown

    def is_enemy_in_range(self, enemy):
        distance = ((self.rect.x - enemy.rect.x) ** 2 + (self.rect.y - enemy.rect.y) ** 2) ** 0.5
        return distance <= self.range

    def update(self, enemies,  *args, **kwargs):
        current_time = pygame.time.get_ticks()
        pygame.draw.circle(kwargs['screen'], (0, 255, 0), self.rect.center, self.range, 1)
        for enemy in enemies:
            if not self.is_enemy_in_range(enemy):
                continue
                
            if current_time - self.last_shot_time >= self.cooldown:
                print(f"{self.name} shooting at {enemy.name}")
                enemy.take_damage(self.damage)
                self.last_shot_time = current_time