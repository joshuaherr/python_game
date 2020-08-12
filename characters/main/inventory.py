import pygame

from utilities.file_helpers import get_hud_screen_path
from objects.object_base import ObjectBase
from components.screen_components import ScreenComponents
from objects.HUD.text.character import TextCharacter


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
        self.selling_items = False
        self.sell_handle = None
        self.default_x_coordinate = obj_height
        self.default_y_coordinate = obj_width
        self.inventory_text = "inventory"
        self.default_inventory_text = "inventory"
        self.text_components = []

    def add_item(self, item):
        self.inventory_items.append(item)

    def open_inventory(self):
        self.is_inventory_open = True
        ScreenComponents().add_screen_component(self)
        x_coord_offset = self.x_coordinate + 11
        y_coord_offset = self.y_coordinate + 38
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
        title_x_offset = self.x_coordinate + 5
        title_y_offset = self.y_coordinate + 8
        for char_index in range(0, len(self.inventory_text)):
            title_x = title_x_offset + (char_index * 13)
            char_comp = TextCharacter(self.inventory_text[char_index])
            char_comp.set_coordinates(title_x, title_y_offset)
            char_comp.set_layer(101)
            self.text_components.append(char_comp)
            ScreenComponents().add_screen_component(char_comp)

    def close_inventory(self):
        self.is_inventory_open = False
        ScreenComponents().remove_screen_component(self.id)
        for item in self.inventory_items:
            ScreenComponents().remove_screen_component(item.id)
        for comp in self.text_components:
            ScreenComponents().remove_screen_component(comp.id)

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
            if self.selling_items:
                self.sell_handle(item)
            else:
                player = ScreenComponents().find_component(self.character_id)
                if not player:
                    print("ERROR: could not find player component.")
                rect_check = player.get_rect_in_front(30)
                x_coord = rect_check.x
                y_coord = rect_check.y
                item.set_coordinates(x_coord, y_coord)
                self.inventory_items = [comp for comp in self.inventory_items if comp.id != item.id]

    def get_inventory_contents(self):
        return self.inventory_items

    def delete_inventory_item(self, item_id):
        self.inventory_items = [item for item in self.inventory_items if item.id != item_id]
