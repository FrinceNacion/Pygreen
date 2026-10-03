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
        self.current_path = 1  

        self.name = name
        self.health = health
        self.speed = speed

        self.white_flash_duration = 100
        self.white_flash_until = 0

    def take_damage(self, damage):
        current_time = pygame.time.get_ticks()

        self.health -= damage
        self.white_flash_until = current_time + self.white_flash_duration
        print(f"{self.name} took {damage} damage, health is now {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            self.kill()

    def handle_end_of_path(self):
        if not (self.rect.x == self.path[-1][X] and self.rect.y == self.path[-1][Y]):
            return False
        if self.current_path == len(self.path) - 1:
            return True
        return False

    def update(self, *args, **kwargs):
        if self.handle_end_of_path():
            self.kill()
            return 

        if pygame.time.get_ticks() < self.white_flash_until:
            self.image.fill((225, 225, 225))
        else:
            self.image.fill((225, 75, 0))

        distance_x = self.path[self.current_path][X] - self.rect.x
        distance_y = self.path[self.current_path][Y] - self.rect.y

        if abs(distance_x) <= self.speed and abs(distance_y) <= self.speed:
            self.rect.x = self.path[self.current_path][X]
            self.rect.y = self.path[self.current_path][Y]

            self.current_path += 1
            if self.current_path >= len(self.path):
                self.current_path = len(self.path) - 1

        if self.rect.x < self.path[self.current_path][X]:
            self.rect.x += self.speed
        elif self.rect.x > self.path[self.current_path][X]:
            self.rect.x -= self.speed

        if self.rect.y < self.path[self.current_path][Y]:
            self.rect.y += self.speed
        elif self.rect.y > self.path[self.current_path][Y]:
            self.rect.y -= self.speed