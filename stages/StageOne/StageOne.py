from pathlib import Path
import pygame
from config.constants import SCREEN_SIZE
from stages.StageOne import stage_data


class StageOne(pygame.Surface):
    def __init__(self):
        super().__init__(SCREEN_SIZE)
        self.stage_dir = Path(__file__).resolve().parent

        self.data_module = stage_data
        self.path_points = stage_data.load_path_points()
        self.path_one = self.path_points

        self.enemies = stage_data.get_enemies(self.path_points)
        self.towers = pygame.sprite.Group(stage_data.get_tower_slots())

        asset_path = "./assets/StageOneMap.png"
        map_image = pygame.image.load(asset_path).convert()
        self.background = pygame.transform.scale(map_image, SCREEN_SIZE)

    def handle_event(self, event):
        for tower in self.towers:
            tower.handle_event(event)

    def load_path_points(self):
        self.path_points = self.data_module.load_path_points()
        self.path_one = self.path_points
        return self.path_points

    def save_path_points(self, points):
        self.data_module.save_path_points(points)
        self.path_points = [list(pt) for pt in points]
        self.path_one = self.path_points

    def draw(self):
        self.blit(self.background, (0, 0))
        self.towers.update(self.enemies)
        self.towers.draw(self)

        for tower in self.towers:
            tower.show_options(self)
