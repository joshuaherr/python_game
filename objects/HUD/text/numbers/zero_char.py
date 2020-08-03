from objects.object_base import ObjectBase
from utilities.file_helpers import get_hud_text_path


class ZeroText(ObjectBase):
    """0 text."""

    def __init__(self):
        image_path = get_hud_text_path() / "0_char.png"
        super().__init__(20, str(image_path))