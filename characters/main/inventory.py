import pygame

from utilities.file_helpers import get_hud_screen_path
from objects.object_base import ObjectBase
from components.screen_components import ScreenComponents


class CharacterInventory(ObjectBase):
    """Class encapsulating inventory for a character."""

    def __init__(self):
        image_path = get_hud_screen_path() / "inventory.png"
        super().__init__(100, str(image_path))
        self.inventory_items = []
        height, width = ScreenComponents().get_screen_size()
        obj_height = (height / 2) - 64
        obj_width = (width / 2) - 64
        self.x_coordinate = obj_height
        self.y_coordinate = obj_width

    def add_item(self, item):
        self.inventory_items.append(item)
