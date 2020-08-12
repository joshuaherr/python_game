from objects.object_base import ObjectBase
from utilities.file_helpers import get_weapons_path


class ShortSword(ObjectBase):
    """Short Sword Object class."""

    def __init__(self):
        image_path = get_weapons_path() / "short_sword1.png"
        super().__init__(20, str(image_path))
        self.price = 1000
        self.weight = 5

    def __str__(self):
        return "Short Sword"
