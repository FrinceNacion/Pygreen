import pygame
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE_NORMAL, FONT_SIZE_LARGE
from config.ElementsUI import Button, COLOR_BG
from developer_tools.PathBuilder import PathBuilder

class DevPanel(pygame.surface.Surface):
    def __init__(self, path_builder=None):
        self.panel_width = (SCREEN_WIDTH * 2) // 6
        super().__init__((self.panel_width, SCREEN_HEIGHT))

        self.path_builder = path_builder

        self.panel_rect = pygame.Rect(SCREEN_WIDTH - self.panel_width, 0, self.panel_width, SCREEN_HEIGHT)
        self.is_minimized = False
        self.minimize_panel_btn = Button((10, 10, 80, 25), "<< Minimize", font_size=FONT_SIZE_NORMAL, callback=self.on_minimize)
        self.show_panel_btn = Button((SCREEN_WIDTH - 80, 40, 80, 25), ">> Show", font_size=FONT_SIZE_NORMAL, callback=self.on_show)

        # Pathbuilder buttons
        self.add_path_point_btn = Button((20, 50, 150, 25), "Add Path Point", font_size=FONT_SIZE_NORMAL, callback=self.path_builder.add_path_point)
        self.save_path_points_btn = Button((20, 80, 150, 25), "Save Path Points", font_size=FONT_SIZE_NORMAL, callback=self.path_builder.save_path_points)
        self.remove_path_point_btn = Button((20, 110, 150, 25), "Remove Path Point", font_size=FONT_SIZE_NORMAL, callback=self.path_builder.remove_path_point)

    def handle_event(self, event):
        if event.type not in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            return False

        if self.is_minimized:
            return self.show_panel_btn.handle_event(event)

        local_event_data = {
            "pos": (
                event.pos[0] - self.panel_rect.x,
                event.pos[1] - self.panel_rect.y,
            )
        }
        if hasattr(event, "button"):
            local_event_data["button"] = event.button

        local_event = pygame.event.Event(event.type, local_event_data)
        self.add_path_point_btn.handle_event(local_event)
        self.save_path_points_btn.handle_event(local_event)
        self.minimize_panel_btn.handle_event(local_event)
        self.remove_path_point_btn.handle_event(local_event)

    def on_minimize(self):
        self.panel_rect.x = SCREEN_WIDTH
        self.is_minimized = True

    def on_show(self):
        self.panel_rect.x = SCREEN_WIDTH - self.panel_width
        self.is_minimized = False

    def draw(self, surface):
        self.fill(COLOR_BG)
        if self.is_minimized:
            self.show_panel_btn.draw(surface)
        else:
            self.minimize_panel_btn.draw(self)
        self.add_path_point_btn.draw(self)
        self.save_path_points_btn.draw(self)
        self.remove_path_point_btn.draw(self)
        surface.blit(self, self.panel_rect)