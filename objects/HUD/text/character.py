from objects.object_base import ObjectBase
from utilities.file_helpers import get_hud_text_path
from objects.HUD.text.text_constants import get_character


class TextCharacter(ObjectBase):
    """Text character wrapper object"""

    def __init__(self, character):
        cleaned_character = get_character(character)
        image_path = get_hud_text_path() / f"{cleaned_character}.png"
        super().__init__(20, str(image_path))
