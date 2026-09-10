import pygame
class Tilemap:
    def __init__(self, tileset, map_data, render_size):
        self.tileset = tileset
        self.map_data = map_data
        self.tile_size = tileset.tile_size
        self.tile_render_size = render_size

        self.tile_dictionary = {
            'Top_separate': self.tileset.get_tile(0, 0),  
            'Middle_separate': self.tileset.get_tile(0, 1),  
            'Bottom_separate': self.tileset.get_tile(0, 2),
            'Top_left_corner': self.tileset.get_tile(1, 0),
            'Top_middle': self.tileset.get_tile(2, 0),
            'Top_right_corner': self.tileset.get_tile(3, 0),
            'Left_middle': self.tileset.get_tile(1, 1),
            'Middle_middle': self.tileset.get_tile(2, 1),
            'Right_middle': self.tileset.get_tile(3, 1),
            'Bottom_left_corner': self.tileset.get_tile(1, 2),
            'Bottom_middle': self.tileset.get_tile(2, 2),
            'Bottom_right_corner': self.tileset.get_tile(3, 2)
        }

    def render(self, surface, camera_offset=(0, 0)):
        """Renders the entire tilemap layer onto a target Pygame surface."""
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile_id in enumerate(row):

                x = (col_idx * self.tile_render_size) - camera_offset[0]
                y = (row_idx * self.tile_render_size) - camera_offset[1]

                if tile_id not in self.tile_dictionary:
                    continue 

                tile_image = self.tile_dictionary[tile_id]
                tile_image = pygame.transform.scale(tile_image, (self.tile_render_size, self.tile_render_size))

                surface.blit(tile_image, (x, y))