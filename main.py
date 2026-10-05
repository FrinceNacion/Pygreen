import pygame
import sys
from screens.MainMenu import MainMenu
from config.constants import SCREEN_SIZE, FPS

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
main_menu = MainMenu()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        main_menu.handle_event(event)

    current_time = pygame.time.get_ticks()
    screen.fill(pygame.Color("black"))

    main_menu.draw()
    screen.blit(main_menu, (0, 0))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
