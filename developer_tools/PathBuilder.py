import pygame

class PathBuilder:
    def __init__(self, stage):
        self.stage = stage
        self.path_points = []
        self.default_path_point = (100, 100)

    def set_stage(self, stage):
        self.stage = stage

    def add_path_point(self, path_point=None):
        if path_point is None:
            path_point = self.default_path_point
            self.default_path_point = (self.default_path_point[0] + 100, 100)
        self.path_points.append(path_point)
        print(f"Added path point: {path_point}")

    def draw_path(self, surface=None):
        if self.path_points is None:
            return
        for i in range(len(self.path_points)):
            point = self.path_points[i]
            if i > 0:
                prev_point = self.path_points[i - 1]
                pygame.draw.line(surface, 'white', prev_point, point , 2)
        for i in range(len(self.path_points)):
            point = self.path_points[i]
            path_point_color = 'cadetblue' if i != 0 else 'green'
            if i == len(self.path_points) - 1:
                path_point_color = 'red'
            pygame.draw.circle(surface, path_point_color, point, 10)
            pygame.draw.circle(surface, 'white', point, 10, width=1)
            