from objects.object_base import ObjectBase
from utilities.file_helpers import get_weapons_path


class GreatSword(ObjectBase):
    """Great Sword Object class."""

    def __init__(self):
        image_path = get_weapons_path() / "great_sword.png"
        super().__init__(20, str(image_path))
        self.price = 3000
        self.weight = 7

    def __str__(self):
        return "Great Sword"
