import pygame
import sys

import Enemy

enemy_path = [(25, 100), (200, 100), (1000, 100), (1100, 200), (900, 300), (800, 300), (100, 300)]
enemies = [Enemy.Enemy(f"Red ant {i}", 100, 5, enemy_path) for i in range(5)]

all_sprites = pygame.sprite.Group()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

last_spawn_time = 0
spawn_interval = 1000/2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    screen.fill(pygame.Color("black"))

    all_sprites.draw(screen)
    all_sprites.update()

    try:
        if current_time - last_spawn_time >= spawn_interval:
            print(f"Spawning enemy")
            all_sprites.add(enemies.pop(0))
            last_spawn_time = current_time
    except IndexError:
        pass
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
