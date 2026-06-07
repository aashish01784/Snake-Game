import pygame
import sys
import random

# snake settings
snake_size = 20

# Window settings
WIDTH, HEIGHT = 600, 400
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
light_green = (110, 150, 60)  #  light green
dark_green = (85, 120, 40)    #dark green


def draw_background_grid():
    tile_size = snake_size  # use same size as snake blocks
    rows = HEIGHT // tile_size
    cols = WIDTH // tile_size

    for row in range(rows):
        for col in range(cols):
            color = light_green if (row + col) % 2 == 0 else dark_green
            pygame.draw.rect(Screen,color,pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size))