from characters.character_base import CharacterBase
from utilities.file_helpers import get_shopkeeper_path


class ShopKeeper(CharacterBase):
    """Shopkeeper npc class."""

    def __init__(self):
        image_path = get_shopkeeper_path() / "shopkeeper_down_right_foot.png"
        super().__init__(1, str(image_path), 1)
        self.money = 500
        self.health = 500
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.has_text = True

    def set_coordinates(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.rect.x = x
        self.rect.y = y

    def get_text(self):
        return "abcdefghijklmnopqrstuvwxyz"
