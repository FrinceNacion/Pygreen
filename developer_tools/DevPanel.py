import pygame
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class DevPanel(pygame.surface.Surface):
    def __init__(self):
        self.panel_width = (SCREEN_WIDTH * 2) / 6
        super().__init__((self.panel_width, SCREEN_HEIGHT))

        self.panel_rect = pygame.Rect(SCREEN_WIDTH - self.panel_width, 0, self.panel_width, SCREEN_HEIGHT)

    def draw(self, surface):
        self.fill('gray20')
        surface.blit(self, self.panel_rect)