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


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Anttack")
        self.clock = pygame.time.Clock()

        self.game_state_manager = GameStateManager('main_menu')
        self.main_menu = MainMenu()
        self.stage_selection = StageSelection()
        self.stage_one = StageOne()
        self.stage_two = StageTwo()
        self.stage_three = StageThree()

        self.screens = {
            'main_menu': self.main_menu,
            'stage_selection': self.stage_selection,
            'stage_one': self.stage_one,
            'stage_two': self.stage_two,
            'stage_three': self.stage_three
        }

        self.current_screen = self.screens[self.game_state_manager.get_state()]
        self.running = True
        self.development_mode = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    if self.development_mode and hasattr(self.current_screen, 'path_points'):
                        print("Path points: ", self.current_screen.path_points)
                elif self.current_screen == self.main_menu:
                    new_state = self.main_menu.handle_event(event)
                    if new_state:
                        self.game_state_manager.set_state(new_state)
                elif self.current_screen == self.stage_selection:
                    new_state = self.stage_selection.handle_event(event)
                    if new_state:
                        self.game_state_manager.set_state(new_state)
                elif isinstance(self.current_screen, (StageOne, StageTwo, StageThree)):
                    if self.development_mode and event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                        pos = pygame.mouse.get_pos()
                        self.current_screen.path_points.append(pos)
                        print(f"Added path point: {pos}")

            current_time = pygame.time.get_ticks()
            self.screen.fill(pygame.Color("black"))

            if self.game_state_manager.get_state() in self.screens:
                self.current_screen = self.screens[self.game_state_manager.get_state()]
                self.current_screen.draw()

            self.screen.blit(self.current_screen, (0, 0))
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
