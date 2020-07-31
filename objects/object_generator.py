from components.screen_components import ScreenComponents
import random
from objects.gems.ruby_object import RubyObject
from objects.gems.diamond_object import DiamondObject
from objects.gems.emerald_object import EmeraldObject
from objects.gems.sapphire_object import SapphireObject


def generate_gem_objects(number_of_objects):
    lower_height_bound = 32
    lower_width_bound = 32
    screen_height, screen_width = ScreenComponents().get_screen_size()
    upper_height_bound = int((screen_height - 32) / 3)
    upper_width_bound = int((screen_width - 32) / 3)
    for i in range(0, number_of_objects):
        gem_type = random.randrange(0, 100)
        x_coord = random.randrange(lower_width_bound, upper_width_bound)
        y_coord = random.randrange(lower_height_bound, upper_height_bound)
        new_gem = None
        if gem_type < 30:
            new_gem = RubyObject()
        if gem_type >= 30 and gem_type < 55:
            new_gem = EmeraldObject()
        if gem_type >= 55 and gem_type < 80:
            new_gem = SapphireObject()
        if gem_type >= 80:
            new_gem = DiamondObject()
        new_gem.set_coordinates(x_coord, y_coord)
        ScreenComponents().add_screen_component(new_gem)

    return
