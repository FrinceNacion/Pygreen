import pygame
class Tilemap:
    def __init__(self, tileset, map_data):
        self.tileset = tileset
        self.map_data = map_data
        self.tile_size = tileset.tile_size

        # Pre-cache tile surfaces mapped to integer IDs
        # Tile IDs use row-major order across the tileset.
        self.tile_dictionary = {
            'Top_separate': self.tileset.get_tile(0, 0),  
            'Middle_separate': self.tileset.get_tile(0, 1),  
            'Bottom_separate': self.tileset.get_tile(0, 2),
            'Top_left_corner': self.tileset.get_tile(1, 0),
            'Top_middle': self.tileset.get_tile(2, 0),
            'Top_right_corner': self.tileset.get_tile(3, 0),
        }

    def render(self, surface, camera_offset=(0, 0)):
        """Renders the entire tilemap layer onto a target Pygame surface."""
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile_id in enumerate(row):
                # Skip empty spaces or negative IDs (e.g., -1 for transparent/empty)
                if tile_id in self.tile_dictionary:
                    tile_image = self.tile_dictionary[tile_id]
                    tile_image = pygame.transform.scale(tile_image, (64, 64))
                    
                    # Calculate world coordinates offset by camera position
                    x = (col_idx * 64) - camera_offset[0]
                    y = (row_idx * 64) - camera_offset[1]
                    
                    surface.blit(tile_image, (x, y))