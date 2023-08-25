import pygame
from Colors import Colors
from Terrain import Terrain
from Configurations import Configurations

pygame.init()
clock = pygame.time.Clock()

screen_resolution = (Configurations.SCREEN_WIDTH, Configurations.SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_resolution)
pygame.display.set_caption("Terrain Simulation")

terrain = Terrain()

# Seasons
seasons = ["Summer", "Winter"]
season_index = 0
current_season = seasons[season_index]

time_elapsed = 0
running = True
while running:
    clock.tick(120)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Colors.WHITE)
    terrain.update(current_season)
    terrain.draw(screen, current_season)

    pygame.display.flip()
    time_elapsed += 1
    if time_elapsed == 1200:
        season_index += 1
        season_index %= len(seasons)
        current_season = seasons[season_index]
        time_elapsed = 0

pygame.quit()
