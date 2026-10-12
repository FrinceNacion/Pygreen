import pygame
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE_NORMAL, FONT_SIZE_LARGE
from config.ElementsUI import Button, COLOR_BG

class DevPanel(pygame.surface.Surface):
    def __init__(self):
        self.panel_width = (SCREEN_WIDTH * 2) // 6
        super().__init__((self.panel_width, SCREEN_HEIGHT))

        self.panel_rect = pygame.Rect(SCREEN_WIDTH - self.panel_width, 0, self.panel_width, SCREEN_HEIGHT)
        self.minimize_btn = Button((10, 10, 80, 25), "<< Minimize", font_size=FONT_SIZE_NORMAL, callback=self.on_minimize)

    def handle_event(self, event):
        if event.type not in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            return False

        local_event_data = {
            "pos": (
                event.pos[0] - self.panel_rect.x,
                event.pos[1] - self.panel_rect.y,
            )
        }
        if hasattr(event, "button"):
            local_event_data["button"] = event.button

        local_event = pygame.event.Event(event.type, local_event_data)
        return self.minimize_btn.handle_event(local_event)

    def on_minimize(self):
        print("DevPanel: Minimize button clicked")
        self.panel_rect.x = SCREEN_WIDTH

    def draw(self, surface):
        self.fill(COLOR_BG)
        self.minimize_btn.draw(self)
        surface.blit(self, self.panel_rect)