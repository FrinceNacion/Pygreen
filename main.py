import pygame
import sys
from screens.MainMenu import MainMenu
from screens.StageSelection import StageSelection
from stages.StageOne import StageOne
from stages.StageTwo import StageTwo
from stages.StageThree import StageThree
from config.constants import SCREEN_SIZE, FPS

class GameStateManager:
    def __init__(self, current_state='main_menu'):
        self.current_state = current_state

    def get_state(self):
        return self.current_state

    def set_state(self, state):
        self.current_state = state


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Anttack")
clock = pygame.time.Clock()

game_state_manager = GameStateManager('main_menu')
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

current_screen = screens[game_state_manager.get_state()]
running = True
development_mode = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if development_mode and hasattr(current_screen, 'path_points'):
                print("Path points: ", current_screen.path_points)
        elif current_screen == main_menu:
            new_state = main_menu.handle_event(event)
            if new_state:
                game_state_manager.set_state(new_state)
        elif current_screen == stage_selection:
            new_state = stage_selection.handle_event(event)
            if new_state:
                game_state_manager.set_state(new_state)
        elif isinstance(current_screen, (StageOne, StageTwo, StageThree)):
            if development_mode and event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = pygame.mouse.get_pos()
                current_screen.path_points.append(pos)
                print(f"Added path point: {pos}")

    current_time = pygame.time.get_ticks()
    screen.fill(pygame.Color("black"))

    if game_state_manager.get_state() in screens:
        current_screen = screens[game_state_manager.get_state()]
        current_screen.draw()

    screen.blit(current_screen, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
