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

    def walk(self):
        print(f"{self.name} is walking at speed {self.speed}.")
        distance = self.path[self.current_path][X] - self.rect.x
        
        if abs(distance) <= self.speed:
            self.rect.x = self.path[self.current_path][X]
            self.rect.y = self.path[self.current_path][Y]

            self.current_path += 1
            if self.current_path >= len(self.path):
                self.current_path = len(self.path) - 1
                #print(f"{self.name} has reached the end of the path. {self.current_path}")

        if self.rect.x < self.path[self.current_path][X]:
            self.rect.x += self.speed
        elif self.rect.x > self.path[self.current_path][X]:
            self.rect.x -= self.speed