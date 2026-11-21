import pygame
from config.constants import SCREEN_SIZE
from stages.stage import Stage


class StageTwo(Stage):
    def __init__(self):
        super().__init__(SCREEN_SIZE)
        # path builder mode
        self.path_points = []

        self.background = pygame.Surface(SCREEN_SIZE)
        self.background.fill('seagreen')

    def draw(self):
        self.blit(self.background, (0, 0))

        for point in self.path_points:
            pygame.draw.circle(self, 'salmon', point, 5)
        self.draw_stage_buttons()
