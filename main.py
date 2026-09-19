import sys
# pyrefly: ignore [missing-import]
import pygame

from Tilemap import Tilemap
from Tileset import Tileset

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Valley")
clock = pygame.time.Clock()

TILE_SIZE = 16
TILE_RENDER_SIZE = 64 

MAP_LAYOUT = [
    ['Top_left_corner', 'Top_middle', 'Top_middle', 'Top_right_corner'],
    ['Left_middle', 'Middle_middle', 'Middle_middle', 'Right_middle'],
    ['Left_middle', 'Middle_middle', 'Middle_middle', 'Middle_middle', 'Separate_middle', 'Separate_middle', 'Separate_right'],
    ['Bottom_left_corner', 'Bottom_middle', 'Bottom_middle', 'Bottom_right_corner'],
]

# --- Setup Tileset & Tilemap ---
# Replace 'rpg_tileset.png' with your sprite sheet path
# If testing without an image, mock a surface or load your custom Aseprite sheet
try:
    tileset = Tileset("tileset.png", TILE_SIZE)
    tilemap = Tilemap(tileset, MAP_LAYOUT, TILE_RENDER_SIZE)
except FileNotFoundError:
    print("Tileset PNG file not found. Ensure the image path is correct.")
    pygame.quit()
    sys.exit()

running = True
while running:
  dt = clock.tick(60)

  screen.fill((13, 26, 26))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  tilemap.render(screen)

  pygame.display.flip()

pygame.quit()
sys.exit()