import pygame
import sys

import Enemy

enemy_path = [(25, 100), (200, 100), (1000, 100)]

enemy = Enemy.Enemy("Goblin", 100, 5, enemy_path)

all_sprites = pygame.sprite.Group()
all_sprites.add(enemy)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
