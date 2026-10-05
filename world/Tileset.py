import pygame

class Tileset:
    def __init__(self, image_path, tile_size):
        self.sheet = pygame.image.load(image_path).convert_alpha()
        self.tile_size = tile_size
        
        self.cols = self.sheet.get_width() // tile_size
        self.rows = self.sheet.get_height() // tile_size

    def get_tile(self, col, row):
        rect = pygame.Rect(
            col * self.tile_size, 
            row * self.tile_size, 
            self.tile_size, 
            self.tile_size
        )
        # Create a sub-surface that points to the specific tile region
        return self.sheet.subsurface(rect)