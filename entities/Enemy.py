import math

import pygame
X = 0
Y = 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, health, speed, path):
        super().__init__()

        self.path = path
        self.image = pygame.Surface((25, 25))
        self.image.fill((225, 75, 0))

        self.rect = self.image.get_rect()
        self.rect.topleft = path[0]
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.current_path = 1  

        self.name = name
        self.max_health = health
        self.health = health
        self.speed = speed

        self.health_bar_surface = pygame.Surface((25, 5))
        self.health_bar_surface.fill('green3')
        self.health_bar_rect = self.health_bar_surface.get_rect()

        self.white_flash_duration = 100
        self.white_flash_until = 0

    def update_health_bar(self):
        health_ratio = self.health / self.max_health
        health_bar_width = int(25 * health_ratio)
        self.health_bar_surface.fill('gray20')
        pygame.draw.rect(self.health_bar_surface, 'green3', (0, 0, health_bar_width, 5))

    def take_damage(self, damage):
        current_time = pygame.time.get_ticks()

        self.health -= damage
        self.update_health_bar()
        self.white_flash_until = current_time + self.white_flash_duration
        print(f"{self.name} took {damage} damage, health is now {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            self.kill()

    def handle_end_of_path(self):
        if not (self.x == self.path[-1][X] and self.y == self.path[-1][Y]):
            return False
        if self.current_path == len(self.path) - 1:
            return True
        return False

    def update(self, *args, **kwargs):
        kwargs.get('screen').blit(self.health_bar_surface, (int(self.x), int(self.y - 15)))
        if self.handle_end_of_path():
            self.kill()
            return 

        if pygame.time.get_ticks() < self.white_flash_until:
            self.image.fill((225, 225, 225))
        else:
            self.image.fill((225, 75, 0))

        distance_x = self.path[self.current_path][X] - self.x
        distance_y = self.path[self.current_path][Y] - self.y
        distance = math.hypot(distance_x, distance_y)

        if distance <= self.speed:
            self.x = float(self.path[self.current_path][X])
            self.y = float(self.path[self.current_path][Y])
            self.current_path += 1
            if self.current_path >= len(self.path):
                self.current_path = len(self.path) - 1
        elif distance:
            self.x += distance_x / distance * self.speed
            self.y += distance_y / distance * self.speed

        self.rect.topleft = (int(self.x), int(self.y))