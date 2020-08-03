from objects.object_base import ObjectBase
from utilities.file_helpers import get_hud_text_path


class qText(ObjectBase):
    """Lowercase q text."""

    def __init__(self):
        image_path = get_hud_text_path() / "q.png"
        super().__init__(20, str(image_path))
        self.y_offset = 2

    def set_coordinates(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y + self.y_offset
        self.rect.x = x
        self.rect.y = y + self.y_offset
