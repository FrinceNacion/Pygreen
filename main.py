import pygame
import sys
from screens.MainMenu import MainMenu
from screens.StageSelection import StageSelection
from stages.StageOne import StageOne
from stages.StageTwo import StageTwo
from stages.StageThree import StageThree
from config.constants import SCREEN_SIZE, FPS

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Anttack")
clock = pygame.time.Clock()

state = 'main_menu'
main_menu = MainMenu()
stage_selection = StageSelection()
stage_one = StageOne()
stage_two = StageTwo()
stage_three = StageThree()

screens = {
    'main_menu': main_menu,
    'stage_selection': stage_selection,
    'stage_one': stage_one,
    'stage_two': stage_two,
    'stage_three': stage_three
}

current_screen = main_menu
running = True
development_mode = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if development_mode and hasattr(current_screen, 'path_points'):
                print("Path points: ", current_screen.path_points)
        elif current_screen == main_menu:
            state = main_menu.handle_event(event)
        elif current_screen == stage_selection:
            state = stage_selection.handle_event(event)
        elif isinstance(current_screen, (StageOne, StageTwo, StageThree)):
            if development_mode and event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = pygame.mouse.get_pos()
                current_screen.path_points.append(pos)
                print(f"Added path point: {pos}")

    current_time = pygame.time.get_ticks()
    screen.fill(pygame.Color("black"))

    if state in screens:
        current_screen = screens[state]
        current_screen.draw()

    screen.blit(current_screen, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
