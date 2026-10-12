import pygame
from developer_tools.DevPanel import DevPanel
from developer_tools.PathBuilder import PathBuilder
from config.constants import SCREEN_SIZE

class DevManager(pygame.surface.Surface):
    def __init__(self, stage_screens: dict):
        super().__init__(SCREEN_SIZE)
        self.stage_screens = stage_screens
        self.stage_screen = None
        self.path_builder = PathBuilder(self.stage_screen)
        self.dev_panel = DevPanel(self.path_builder)

    def set_stage_screen(self, stage_screen):
        print(f"DevManager: set_stage_screen called with {stage_screen}")
        if stage_screen in self.stage_screens:
            print(f"Setting stage screen to: {type(self.stage_screens[stage_screen]).__name__}")
            self.stage_screen = self.stage_screens[stage_screen]
            self.path_builder.set_stage(self.stage_screen)

    def handle_event(self, event):
        if hasattr(event, 'pos') and not self.dev_panel.panel_rect.collidepoint(event.pos):
            self.path_builder.handle_event(event)
        self.dev_panel.handle_event(event)

    def draw(self):
        if self.stage_screen is None:
            return

        self.stage_screen.draw()
        self.path_builder.draw_path(self.stage_screen)
        self.blit(self.stage_screen, (0, 0))
        self.dev_panel.draw(self)
