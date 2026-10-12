import pygame

class PathBuilder:
    def __init__(self, stage):
        self.stage = stage
        self.path_points = []
        self.default_path_point = (100, 100)
        self.selected_point_index = None
        self.drag_offset = (0, 0)

    def set_stage(self, stage):
        self.stage = stage

    def add_path_point(self, path_point=None):
        if path_point is None:
            path_point = self.default_path_point
            self.default_path_point = (self.default_path_point[0] + 100, 100)
        self.path_points.append(path_point)
        print(f"Added path point: {path_point}")

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for index, point in enumerate(self.path_points):
                if pygame.Vector2(event.pos).distance_to(point) <= 10:
                    self.selected_point_index = index
                    self.drag_offset = (point[0] - event.pos[0], point[1] - event.pos[1])
                    return True

        elif event.type == pygame.MOUSEMOTION and self.selected_point_index is not None:
            self.path_points[self.selected_point_index] = (
                event.pos[0] + self.drag_offset[0],
                event.pos[1] + self.drag_offset[1],
            )
            return True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.selected_point_index = None

        return False

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
            outline_width = 1
            if i == len(self.path_points) - 1:
                path_point_color = 'red'
            pygame.draw.circle(surface, path_point_color, point, 10)
            if i == self.selected_point_index:
                outline_width = 3 
            pygame.draw.circle(surface, 'white', point, 10, width=outline_width)
            