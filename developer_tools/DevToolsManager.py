import pygame
from developer_tools.DevPanel import DevPanel
from config.constants import SCREEN_SIZE

class DevManager(pygame.surface.Surface):
    def __init__(self, stage_screens: dict):
        super().__init__(SCREEN_SIZE)
        self.stage_screens = stage_screens
        self.stage_screen = None
        self.dev_panel = DevPanel()

    def set_stage_screen(self, stage_screen):
        print(f"DevManager: set_stage_screen called with {stage_screen}")
        if stage_screen in self.stage_screens:
            print(f"Setting stage screen to: {type(self.stage_screens[stage_screen]).__name__}")
            self.stage_screen = self.stage_screens[stage_screen]

    def handle_event(self, event):
        self.dev_panel.handle_event(event)

    def draw(self):
        if self.stage_screen is None:
            return

        self.stage_screen.draw()
        self.blit(self.stage_screen, (0, 0))
        self.dev_panel.draw(self)
