import pygame
from constants import SCREEN_SIZE, FONT_SIZE_NORMAL, FONT_SIZE_LARGE

class MainMenu(pygame.surface.Surface):
    def __init__(self):
        super().__init__(SCREEN_SIZE)
        self.fill("black")
        self.title_font = pygame.font.Font(None, FONT_SIZE_LARGE)
        self.button_font = pygame.font.Font(None, FONT_SIZE_NORMAL)

        center_x = SCREEN_SIZE[0] // 2
        self.play_button = pygame.Rect(0, 0, 220, 50)
        self.settings_button = pygame.Rect(0, 0, 220, 50)
        self.play_button.center = (center_x, SCREEN_SIZE[1] // 2)
        self.settings_button.center = (center_x, SCREEN_SIZE[1] // 2 + 70)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.play_button.collidepoint(event.pos):
                self.on_play()
            elif self.settings_button.collidepoint(event.pos):
                self.on_settings()

    def on_play(self):
        pass

    def on_settings(self):
        pass

    def draw(self):
        self.fill("black")

        title_surface = self.title_font.render("Anttack", True, 'tomato3')
        title_rect = title_surface.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2 - 100))
        self.blit(title_surface, title_rect)

        buttons = [(self.play_button, "Play"), (self.settings_button, "Settings")]

        for button_rect, label in buttons:
            pygame.draw.rect(self, (45, 45, 45), button_rect, border_radius=6)
            pygame.draw.rect(self, 'white', button_rect, width=2, border_radius=6)
            label_surface = self.button_font.render(label, True, 'white')
            label_rect = label_surface.get_rect(center=button_rect.center)
            self.blit(label_surface, label_rect)
        