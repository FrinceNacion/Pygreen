import pygame
import sys

import Enemy
import Tower

enemy_path = [(25, 100), (200, 100), (1000, 100), (1100, 200), (900, 300), (800, 300), (100, 300)]
enemies = [Enemy.Enemy(f"Red ant {i}", 100, 3, enemy_path) for i in range(5)]
enemies_in_battlefield = pygame.sprite.Group()

tower = Tower.Tower("Ant tower", 10, 250, 700, (640, 350))
tower1 = Tower.Tower("Ant tower", 10, 250, 700, (300, 350))

all_sprites = pygame.sprite.Group()
all_sprites.add(tower)
all_sprites.add(tower1)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 16)

last_spawn_time = 0
spawn_interval = 1000/2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    screen.fill(pygame.Color("black"))

    all_sprites.draw(screen)
    all_sprites.update(enemies_in_battlefield, screen=screen)

    try:
        if current_time - last_spawn_time >= spawn_interval:
            current_enemy = enemies.pop(0)
            all_sprites.add(current_enemy)
            enemies_in_battlefield.add(current_enemy)
            last_spawn_time = current_time
    except IndexError:
        pass

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
