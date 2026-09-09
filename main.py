import sys
import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Valley")
clock = pygame.time.Clock()

running = True
while running:
  dt = clock.tick(60)

  screen.fill((13, 26, 26))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.flip()

pygame.quit()
sys.exit()