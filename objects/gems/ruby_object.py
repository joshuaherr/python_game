from objects.object_base import ObjectBase
from utilities.file_helpers import get_gem_object_path


class RubyObject(ObjectBase):
    """Ruby Object class."""

    def __init__(self):
        image_path = get_gem_object_path() / "ruby.png"
        super().__init__(1, str(image_path))
        self.price = 30
        self.weight = 1

    def __str__(self):
        return "ruby"
