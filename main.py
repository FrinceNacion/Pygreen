import pygame
import sys
from screens.MainMenu import MainMenu
from stages.StageOne import StageOne
from config.constants import SCREEN_SIZE, FPS

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
state = 'main_menu'
main_menu = MainMenu()
stage_one = StageOne()
current_screen = main_menu

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if current_screen == main_menu:
            state = main_menu.handle_event(event)

    current_time = pygame.time.get_ticks()
    screen.fill(pygame.Color("black"))

    main_menu.draw()
    if state == "stage_one":
        stage_one.draw()
        current_screen = stage_one

    screen.blit(current_screen, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
