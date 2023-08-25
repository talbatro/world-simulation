import pygame
from Colors import Colors
from Configurations import Configurations
import random


class Tile:
    def __init__(self, x, y, fertility):
        self.x = x
        self.y = y
        self.fertility = fertility
        self.fertility_rate = random.uniform(0.002, 0.005)
        self.ice_probability = random.uniform(0.7, 1)

    def draw(self, screen, season):
        color_with_fertility = get_rated_color(
            Colors.DIRT, Colors.GRASS, self.fertility
        )

        pygame.draw.rect(
            screen,
            Colors.ICE
            if season == "Winter"
            and self.fertility <= 0
            or season == "Summer"
            and self.fertility <= 0.2
            else color_with_fertility,
            (self.x, self.y, Configurations.TILE_SIZE, Configurations.TILE_SIZE),
        )
        pygame.draw.rect(
            screen,
            Colors.BLACK,
            (self.x, self.y, Configurations.TILE_SIZE, Configurations.TILE_SIZE),
            1,
        )

    def update(self, season):
        if season == "Summer":
            if self.fertility <= 1:
                self.fertility += self.fertility_rate
        elif season == "Winter":
            if self.fertility >= 0:
                self.fertility -= self.fertility_rate


def get_rated_color(color1, color2, rate):
    red = color2[0] - color1[0]
    green = color2[1] - color1[1]
    blue = color2[2] - color1[2]

    rated_color = (
        color1[0] + red * rate,
        color1[1] + green * rate,
        color1[2] + blue * rate,
    )
    return rated_color
