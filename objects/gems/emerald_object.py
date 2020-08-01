from objects.object_base import ObjectBase
from utilities.file_helpers import get_gem_object_path


class EmeraldObject(ObjectBase):
    """Emerald Object class."""

    def __init__(self):
        image_path = get_gem_object_path() / "emerald.png"
        super().__init__(1, str(image_path))
        self.price = 50
        self.weight = 2

    def __str__(self):
        return "Emerald"
