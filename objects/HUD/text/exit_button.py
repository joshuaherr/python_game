from objects.object_base import ObjectBase
from utilities.file_helpers import get_hud_text_path


class ExitButton(ObjectBase):
    """Lowercase red x exit Button."""

    def __init__(self):
        image_path = get_hud_text_path() / "exitbutton.png"
        super().__init__(25, str(image_path))
        self.y_offset = 0


