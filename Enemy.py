import pygame
X = 0
Y = 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, health, speed, path):
        super().__init__()

        self.path = path
        self.image = pygame.Surface((50, 50))
        self.image.fill((230, 25, 0))

        self.rect = self.image.get_rect()
        self.rect.topleft = path[0]
        self.current_path = 1  

        self.name = name
        self.health = health
        self.speed = speed

    def handle_end_of_path(self):
        if not (self.rect.x == self.path[-1][X] and self.rect.y == self.path[-1][Y]):
            return False
        if self.current_path == len(self.path) - 1:
            return True
        return False

    def walk(self):
        if self.handle_end_of_path():
            return 

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