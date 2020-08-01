from objects.object_base import ObjectBase
from utilities.file_helpers import get_gem_object_path


class DiamondObject(ObjectBase):
    """Diamond Object class."""

    def __init__(self):
        image_path = get_gem_object_path() / "diamond.png"
        super().__init__(1, str(image_path))
        self.price = 100
        self.weight = 3

    def __str__(self):
        return "Diamond"
