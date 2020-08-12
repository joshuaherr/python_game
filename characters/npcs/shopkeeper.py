from characters.character_base import CharacterBase
from utilities.file_helpers import get_shopkeeper_path
from objects.HUD.text.text_screen import TextScreen
from objects.HUD.text.button import Button
from components.screen_components import ScreenComponents


class ShopKeeper(CharacterBase):
    """Shopkeeper npc class."""

    def __init__(self):
        image_path = get_shopkeeper_path() / "shopkeeper_down_right_foot.png"
        super().__init__(1, str(image_path), 1)
        self.money = 5000
        self.health = 500
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.has_action = True
        self.player_id = 0
        self.text_screen = None
        self.selected_item = None

    def __str__(self):
        return "shopkeeper"

    def set_coordinates(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.rect.x = x
        self.rect.y = y

    def do_action(self, player_id):
        self.player_id = player_id
        player = ScreenComponents().find_component(self.player_id)
        player.can_move = False
        player.action_disabled = True
        self.display_main_screen()

    def display_main_screen(self):
        self.text_screen = TextScreen(self.player_id)
        self.text_screen.set_text_characters("Welcome to the shop.  Please select an option:")
        self.text_screen.write_characters()
        # Buy Button
        buy_button = Button("Buy")
        buy_button_height = self.text_screen.y_coordinate + self.text_screen.height - 40
        buy_button_width = self.text_screen.x_coordinate + 8
        buy_button.set_coordinates(buy_button_width, buy_button_height)
        self.text_screen.add_button(buy_button)
        buy_button.render_button()
        buy_button.set_button_handle(self.buy_button_screen)
        # Sell Button
        sell_button = Button("Sell")
        sell_button_height = self.text_screen.y_coordinate + self.text_screen.height - 40
        sell_button_width = self.text_screen.x_coordinate + 85
        sell_button.set_coordinates(sell_button_width, sell_button_height)
        self.text_screen.add_button(sell_button)
        sell_button.render_button()
        sell_button.set_button_handle(self.sell_button_screen)

    def buy_button_screen(self):
        self.text_screen.close_text()
        self.text_screen.set_text_characters("What would you like to buy?")
        self.text_screen.write_characters()
        # Short Sword
        short_sword_button = Button("Short Sword: 1000")
        short_sword_button_height = self.text_screen.y_coordinate + self.text_screen.height - 90
        short_sword_button_width = self.text_screen.x_coordinate + 40
        short_sword_button.set_coordinates(short_sword_button_width, short_sword_button_height)
        self.text_screen.add_button(short_sword_button)
        short_sword_button.render_button()
        short_sword_button.set_button_handle(self.buy_short_sword)
        # Great Sword
        great_sword_button = Button("Great Sword: 3000")
        great_sword_button_height = self.text_screen.y_coordinate + self.text_screen.height - 65
        great_sword_button_width = self.text_screen.x_coordinate + 40
        great_sword_button.set_coordinates(great_sword_button_width, great_sword_button_height)
        self.text_screen.add_button(great_sword_button)
        great_sword_button.render_button()
        great_sword_button.set_button_handle(self.buy_great_sword)

    def sell_button_screen(self):
        self.text_screen.close_text()
        self.text_screen.set_text_characters("What would you like to sell?")
        self.text_screen.write_characters()
        player = ScreenComponents().find_component(self.player_id)
        inventory = player.get_inventory_contents()
        height, width = ScreenComponents().get_screen_size()
        x_coord = (width / 2) - 100
        y_coord = 100
        inventory.set_coordinates(x_coord, y_coord)
        inventory.selling_items = True
        inventory.sell_handle = self.sell_item_screen
        inventory.inventory_text = "Sell Item"
        inventory.open_inventory()

    def buy_short_sword(self):
        player = ScreenComponents().find_component(self.player_id)
        if player.money >= 1000:
            print("you can buy a short sword.")
        else:
            self.text_screen.close_text()
            self.text_screen.set_text_characters("You need 1000 money to buy a Short Sword.")
            self.text_screen.write_characters()

    def buy_great_sword(self):
        player = ScreenComponents().find_component(self.player_id)
        if player.money >= 3000:
            print("you can buy a great sword.")
        else:
            self.text_screen.close_text()
            self.text_screen.set_text_characters("You need 3000 money to buy a Great Sword.")
            self.text_screen.write_characters()

    def sell_item_screen(self, item):
        text = f"Sell {item} for {item.price}?"
        self.selected_item = item
        self.text_screen.close_text()
        self.text_screen.set_text_characters(text)
        self.text_screen.write_characters()
        # Buy Button
        buy_button = Button("Yes")
        buy_button_height = self.text_screen.y_coordinate + self.text_screen.height - 40
        buy_button_width = self.text_screen.x_coordinate + 8
        buy_button.set_coordinates(buy_button_width, buy_button_height)
        self.text_screen.add_button(buy_button)
        buy_button.render_button()
        buy_button.set_button_handle(self.sell_item)
        # Sell Button
        sell_button = Button("No")
        sell_button_height = self.text_screen.y_coordinate + self.text_screen.height - 40
        sell_button_width = self.text_screen.x_coordinate + 85
        sell_button.set_coordinates(sell_button_width, sell_button_height)
        self.text_screen.add_button(sell_button)
        sell_button.render_button()
        sell_button.set_button_handle(self.sell_button_screen)

    def sell_item(self):

        if self.money >= self.selected_item.price:
            player = ScreenComponents().find_component(self.player_id)
            player.money += self.selected_item.price
            ScreenComponents().remove_screen_component(self.selected_item.id)
            player.inventory.delete_inventory_item(self.selected_item.id)
            print(f"Sold {self.selected_item} for {self.selected_item.price}")
            print(f"current money: {player.money}")
        else:
            self.text_screen.close_text()
            self.text_screen.set_text_characters(f"Shopkeeper does not have {self.selected_item.price} money...")
            self.text_screen.write_characters()
        self.sell_button_screen()
