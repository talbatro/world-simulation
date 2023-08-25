from Tile import Tile
from Configurations import Configurations
import random


class Terrain:
    def __init__(self):
        self.tile_rows = Configurations.SCREEN_HEIGHT // Configurations.TILE_SIZE
        self.tile_cols = Configurations.SCREEN_WIDTH // Configurations.TILE_SIZE
        self.tiles = []
        for row in range(self.tile_rows):
            for col in range(self.tile_cols):
                self.tiles.append(
                    Tile(
                        col * Configurations.TILE_SIZE,
                        row * Configurations.TILE_SIZE,
                        random.random(),
                    )
                )

    def draw(self, screen, season):
        for tile in self.tiles:
            tile.draw(screen, season)

    def update(self, season):
        for tile in self.tiles:
            tile.update(season)
