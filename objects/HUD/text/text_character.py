from objects.object_base import ObjectBase
from utilities.file_helpers import get_hud_text_path


class TextCharacter(ObjectBase):
    """All character text."""

    def __init__(self, character):
        image_path = get_hud_text_path() / f"{character}.png"
        super().__init__(20, str(image_path))
