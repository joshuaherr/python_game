from objects.object_base import ObjectBase
from utilities.file_helpers import get_hud_text_path
from components.screen_components import ScreenComponents
from objects.HUD.text.exit_button import ExitButton
from objects.HUD.text.character import TextCharacter

import pygame


class TextScreen(ObjectBase):
    """Screen for displaying text."""

    def __init__(self, player_id):
        image_path = get_hud_text_path() / "text_screen_medium.png"
        super().__init__(15, str(image_path))
        self.text_characters = []
        self.height = 150
        self.width = 350
        x_offset = int(self.width / 2)
        y_offset = int(self.height / 2)
        screen_height, screen_width = ScreenComponents().get_screen_size()
        self.x_coordinate = int((screen_width / 2) - x_offset)
        self.y_coordinate = int((screen_height / 2) - y_offset)
        self.character_components = []
        self.exit_component = None
        self.player_id = player_id
        self.buttons = []

    def set_text_characters(self, text):
        self.text_characters = text

    def add_button(self, button):
        self.buttons.append(button)

    def write_characters(self):
        # char length: 320 = 22 symbols per line
        ScreenComponents().add_screen_component(self)
        starting_x_coord = self.x_coordinate + 8
        starting_y_coord = self.y_coordinate + 5
        y_offset = 0
        x_offset = 0
        for index in range(0, len(self.text_characters)):
            curr_char = self.text_characters[index]
            char_comp = TextCharacter(curr_char)
            if index % 22 == 0 and index != 0:
                x_offset = 0
                y_offset += 1
            x_coord = starting_x_coord + (14 * x_offset)
            y_coord = starting_y_coord + (21 * y_offset)
            char_comp.set_coordinates(x_coord, y_coord)
            self.character_components.append(char_comp)
            ScreenComponents().add_screen_component(char_comp)
            x_offset += 1
        exit_x = self.x_coordinate + self.width - 25
        exit_y = self.y_coordinate + 5
        exit_comp = ExitButton()
        exit_comp.set_coordinates(exit_x, exit_y)
        self.exit_component = exit_comp
        ScreenComponents().add_screen_component(exit_comp)

    def close_text(self):
        for comp in self.character_components:
            ScreenComponents().remove_screen_component(comp.id)
        self.character_components = []
        ScreenComponents().remove_screen_component(self.exit_component.id)
        ScreenComponents().remove_screen_component(self.id)
        player = ScreenComponents().find_component(self.player_id)
        for button in self.buttons:
            button.close_button()
        self.buttons = []
        player.can_move = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = event.pos
            if self.exit_component.rect.collidepoint(x_pos, y_pos):
                self.close_text()
                player = ScreenComponents().find_component(self.player_id)
                player.action_disabled = False
                return
            for button in self.buttons:
                if button.is_button_clicked(x_pos, y_pos):
                    button.button_handle()
                    return
