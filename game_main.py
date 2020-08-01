import pygame

import sys

from turf.basic.grass_turf import GrassTurf
from characters.main.main_character import MainCharacter
from components.screen_components import ScreenComponents
from objects.object_generator import generate_gem_objects

pygame.init()

size = width, height = 960, 960

screen = pygame.display.set_mode(size)

ScreenComponents().set_screen(screen)
ScreenComponents().set_screen_size(height, width)

pygame.display.set_caption("First Game Attempt.")

background_grass = []
for x in range(0, 60):
    for y in range(0, 60):
        temp_x = x * 16
        temp_y = y * 16
        temp_grass = GrassTurf()
        temp_grass.set_coordinates(temp_x, temp_y)
        ScreenComponents().add_screen_component(temp_grass)

main_character = MainCharacter()
ScreenComponents().add_screen_component(main_character)
generate_gem_objects(15)

while 1:
    ScreenComponents().run_events()
    ScreenComponents().render_components()
