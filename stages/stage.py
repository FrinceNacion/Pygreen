import pygame
from config.constants import SCREEN_SIZE


class Stage(pygame.Surface):
    def __init__(self, size=SCREEN_SIZE):
        super().__init__(size)
        self.background = pygame.Surface(size)
        self.is_started = False
        self.menu_button = pygame.Rect(size[0] - 70, 10, 60, 40)
        self.start_button = pygame.Rect(size[0] - 150, 10, 60, 40)

    def handle_event(self, event):
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.menu_button.collidepoint(event.pos)
        ):
            return "stage_selection"
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.start_button.collidepoint(event.pos)
        ):
            self.is_started = True
            self.start_button = pygame.Rect(0, 0, 0, 0)
        return None

    def draw_stage_buttons(self):
        pygame.draw.rect(self, (220, 40, 40), self.menu_button, border_radius=4)
        pygame.draw.rect(self, (40, 220, 40), self.start_button, border_radius=4)
