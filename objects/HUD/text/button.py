from components.screen_components import ScreenComponents
from objects.HUD.text.arrow import Arrow
from objects.HUD.text.character import TextCharacter


class Button():
    """Button with text."""

    def __init__(self, text):
        self.button_text = text
        self.button_components = []
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.y_offset = 0
        self.button_handle = None
        self.arrow = None
        self.rendered = False

    def set_coordinates(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y + self.y_offset

    def render_button(self):
        if self.rendered:
            return
        self.arrow = Arrow()
        arrow_x_coord = self.x_coordinate + 5
        self.arrow.set_coordinates(arrow_x_coord, self.y_coordinate)
        ScreenComponents().add_screen_component(self.arrow)
        arrow_offset = 2
        for index in range(1, (len(self.button_text) + 1)):
            curr_char = self.button_text[index - 1]
            comp = TextCharacter(curr_char)
            comp_x_coord = self.x_coordinate + (index * 14) + arrow_offset
            arrow_offset = 0
            comp.set_coordinates(comp_x_coord, self.y_coordinate)
            ScreenComponents().add_screen_component(comp)
            self.button_components.append(comp)
        self.rendered = True

    def close_button(self):
        if not self.rendered:
            return
        ScreenComponents().remove_screen_component(self.arrow.id)
        for comp in self.button_components:
            ScreenComponents().remove_screen_component(comp.id)
        self.rendered = False

    def set_button_handle(self, handle):
        self.button_handle = handle

    def is_button_clicked(self, x_pos, y_pos):
        for comp in self.button_components:
            if comp.rect.collidepoint(x_pos, y_pos):
                return True
        return False
