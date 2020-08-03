from objects.object_base import ObjectBase
from utilities.file_helpers import get_hud_text_path


class PeriodText(ObjectBase):
    """Period."""

    def __init__(self):
        image_path = get_hud_text_path() / "period.png"
        super().__init__(20, str(image_path))
        self.y_offset = 0

    def set_coordinates(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y + self.y_offset
        self.rect.x = x
        self.rect.y = y + self.y_offset
