from pathlib import Path

import pygame

from config.constants import SCREEN_SIZE


class StageOne(pygame.Surface):
    def __init__(self):
        super().__init__(SCREEN_SIZE)
        # path builder mode
        self.path_points = []

        asset_path = "./assets/StageOneMap.png"
        map_image = pygame.image.load(asset_path).convert()
        self.background = pygame.transform.scale(map_image, SCREEN_SIZE)

    def draw(self):
        self.blit(self.background, (0, 0))

        for point in self.path_points:
            pygame.draw.circle(self, 'salmon', point, 5)
    


