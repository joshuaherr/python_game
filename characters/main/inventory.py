import pygame

from utilities.file_helpers import get_hud_screen_path
from objects.object_base import ObjectBase
from components.screen_components import ScreenComponents


class CharacterInventory(ObjectBase):
    """Class encapsulating inventory for a character."""

    def __init__(self, char_id):
        image_path = get_hud_screen_path() / "inventory.png"
        super().__init__(100, str(image_path))
        self.inventory_items = []
        height, width = ScreenComponents().get_screen_size()
        obj_height = (height / 2) - 64
        obj_width = (width / 2) - 64
        self.x_coordinate = obj_height
        self.y_coordinate = obj_width
        self.is_inventory_open = False
        self.character_id = char_id

    def add_item(self, item):
        self.inventory_items.append(item)

    def open_inventory(self):
        self.is_inventory_open = True
        ScreenComponents().add_screen_component(self)
        x_coord_offset = self.x_coordinate + 11
        y_coord_offset = self.y_coordinate + 11
        x_offset = 0
        y_offset = 0
        for index in range(0, len(self.inventory_items)):
            item = self.inventory_items[index]
            if index == 3:
                x_offset = 0
                y_offset = 1
            elif index == 6:
                x_offset = 0
                y_offset = 2
            x_coord = x_coord_offset + (36 * x_offset)
            y_coord = y_coord_offset + (36 * y_offset)
            x_offset += 1
            item.set_coordinates(x_coord, y_coord)
            ScreenComponents().add_screen_component(item)

    def close_inventory(self):
        self.is_inventory_open = False
        ScreenComponents().remove_screen_component(self.id)
        for item in self.inventory_items:
            ScreenComponents().remove_screen_component(item.id)

    def handle_event(self, event):
        if not self.is_inventory_open:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = event.pos
            item_clicked = [comp for comp in self.inventory_items if comp.rect.collidepoint(x_pos, y_pos)]
            if len(item_clicked) < 1:
                return
            if len(item_clicked) > 1:
                print(f"Error: Multiple items clicked! {item_clicked}")
            item = item_clicked[0]
            item.density = item.original_density
            player = ScreenComponents().find_component(self.character_id)
            if not player:
                print("ERROR: could not find player component.")
            rect_check = player.get_rect_in_front(30)
            x_coord = rect_check.x
            y_coord = rect_check.y
            item.set_coordinates(x_coord, y_coord)
            self.inventory_items = [comp for comp in self.inventory_items if comp.id != item.id]

