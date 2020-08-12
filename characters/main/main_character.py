from characters.character_base import CharacterBase
from characters.character_constants import Directions, MovementStates
from characters.main.main_character_constants import (
    get_move_down_stand_image,
    get_move_down_right_foot_image,
    get_move_down_left_foot_image,
    get_move_right_stand_image,
    get_move_right_right_foot_image,
    get_move_right_left_foot_image,
    get_move_up_stand_image,
    get_move_up_right_foot_image,
    get_move_up_left_foot_image,
    get_move_left_stand_image,
    get_move_left_right_foot_image,
    get_move_left_left_foot_image
)
from components.screen_components import ScreenComponents
from characters.main.inventory import CharacterInventory
from objects.object_base import ObjectBase
import copy
import pygame


class MainCharacter(CharacterBase):
    """Main Character controlled by the user."""

    def __init__(self):
        super().__init__(1, str(get_move_down_stand_image()), 1)
        self.movement_state = MovementStates.MOVE_DOWN_STAND
        self.character_direction = Directions.DOWN
        self.can_move = True
        self.is_inventory_open = False
        self.inventory = CharacterInventory(self.id)
        self.health = 100
        self.money = 10000
        self.action_disabled = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == 274:
                if not self.can_move:
                    return
                if self.character_direction == Directions.DOWN:
                    if self.is_movement_allowed():
                        self.move_down()
                        self.update_image_movement()
                else:
                    self.character_direction = Directions.DOWN
                    self.movement_state = MovementStates.MOVE_DOWN_STAND
                    self.image = pygame.image.load(str(get_move_down_stand_image()))
            elif event.key == 275:
                if not self.can_move:
                    return
                if self.character_direction == Directions.RIGHT:
                    if self.is_movement_allowed():
                        self.move_right()
                        self.update_image_movement()
                else:
                    self.character_direction = Directions.RIGHT
                    self.movement_state = MovementStates.MOVE_RIGHT_STAND
                    self.image = pygame.image.load(str(get_move_right_stand_image()))
            elif event.key == 273:
                if not self.can_move:
                    return
                if self.character_direction == Directions.UP:
                    if self.is_movement_allowed():
                        self.move_up()
                        self.update_image_movement()
                else:
                    self.character_direction = Directions.UP
                    self.movement_state = MovementStates.MOVE_UP_STAND
                    self.image = pygame.image.load(str(get_move_up_stand_image()))
            elif event.key == 276:
                if not self.can_move:
                    return
                if self.character_direction == Directions.LEFT:
                    if self.is_movement_allowed():
                        self.move_left()
                        self.update_image_movement()
                else:
                    self.character_direction = Directions.LEFT
                    self.movement_state = MovementStates.MOVE_LEFT_STAND
                    self.image = pygame.image.load(str(get_move_left_stand_image()))
            elif event.key == 105:
                # inventory key pressed
                if not self.inventory.is_inventory_open:
                    self.can_move = False
                    self.inventory.open_inventory()
                else:
                    self.can_move = True
                    self.inventory.close_inventory()
            elif event.key == 103:
                # g pressed for get object
                if len(self.inventory.inventory_items) >= 9:
                    return
                self.get_object()
            elif event.key == 32:
                # space bar pressed (action button)
                self.do_action()

    def update_image_movement(self):
        if self.movement_state == MovementStates.MOVE_DOWN_STAND:
            self.image = pygame.image.load(str(get_move_down_right_foot_image()))
            self.movement_state = MovementStates.MOVE_DOWN_RIGHT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_DOWN_RIGHT_FOOT:
            self.image = pygame.image.load(str(get_move_down_left_foot_image()))
            self.movement_state = MovementStates.MOVE_DOWN_LEFT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_DOWN_LEFT_FOOT:
            self.image = pygame.image.load(str(get_move_down_right_foot_image()))
            self.movement_state = MovementStates.MOVE_DOWN_RIGHT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_RIGHT_STAND:
            self.image = pygame.image.load(str(get_move_right_right_foot_image()))
            self.movement_state = MovementStates.MOVE_RIGHT_RIGHT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_RIGHT_RIGHT_FOOT:
            self.image = pygame.image.load(str(get_move_right_left_foot_image()))
            self.movement_state = MovementStates.MOVE_RIGHT_LEFT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_RIGHT_LEFT_FOOT:
            self.image = pygame.image.load(str(get_move_right_right_foot_image()))
            self.movement_state = MovementStates.MOVE_RIGHT_RIGHT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_UP_STAND:
            self.image = pygame.image.load(str(get_move_up_right_foot_image()))
            self.movement_state = MovementStates.MOVE_UP_RIGHT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_UP_RIGHT_FOOT:
            self.image = pygame.image.load(str(get_move_up_left_foot_image()))
            self.movement_state = MovementStates.MOVE_UP_LEFT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_UP_LEFT_FOOT:
            self.image = pygame.image.load(str(get_move_up_right_foot_image()))
            self.movement_state = MovementStates.MOVE_UP_RIGHT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_LEFT_STAND:
            self.image = pygame.image.load(str(get_move_left_right_foot_image()))
            self.movement_state = MovementStates.MOVE_LEFT_RIGHT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_LEFT_RIGHT_FOOT:
            self.image = pygame.image.load(str(get_move_left_left_foot_image()))
            self.movement_state = MovementStates.MOVE_LEFT_LEFT_FOOT
            return
        if self.movement_state == MovementStates.MOVE_LEFT_LEFT_FOOT:
            self.image = pygame.image.load(str(get_move_left_right_foot_image()))
            self.movement_state = MovementStates.MOVE_LEFT_RIGHT_FOOT
            return

    def get_rect_in_front(self, offset=0):
        check = (4 * self.speed) + offset
        rect_copy = copy.copy(self.rect)
        if self.character_direction == Directions.DOWN:
            rect_copy.bottom = self.rect.bottom + check
        if self.character_direction == Directions.UP:
            rect_copy.top = self.rect.top - check
        if self.character_direction == Directions.LEFT:
            rect_copy.left = self.rect.left - check
        if self.character_direction == Directions.RIGHT:
            rect_copy.right = self.rect.right + check
        return rect_copy

    def is_movement_allowed(self):
        rect_copy = self.get_rect_in_front()
        dense_comps = ScreenComponents().get_dense_components()
        dense_without_char_rects = [comp.rect for comp in dense_comps if comp.id != self.id]
        collisions = rect_copy.collidelist(dense_without_char_rects)
        if collisions == -1:
            return True
        else:
            return False

    def get_object(self):
        rect_copy = self.get_rect_in_front()
        dense_comps = ScreenComponents().get_dense_components()
        dense_without_char = [comp for comp in dense_comps if comp.id != self.id]
        dense_without_char_rects = [comp.rect for comp in dense_without_char]
        collisions = rect_copy.collidelist(dense_without_char_rects)
        if collisions == -1:
            return
        other_object = dense_without_char[collisions]
        if not isinstance(other_object, ObjectBase):
            return
        other_object.set_layer(101)
        self.inventory.add_item(other_object)
        ScreenComponents().remove_screen_component(other_object.id)
        print(f"Got item: {other_object}")

    def do_action(self):
        if self.action_disabled:
            return
        rect_copy = self.get_rect_in_front()
        dense_comps = ScreenComponents().get_dense_components()
        dense_without_char = [comp for comp in dense_comps if comp.id != self.id]
        dense_without_char_rects = [comp.rect for comp in dense_without_char]
        collisions = rect_copy.collidelist(dense_without_char_rects)
        if collisions == -1:
            return
        npc = dense_without_char[collisions]
        if not isinstance(npc, CharacterBase):
            return
        if npc.has_action:
            npc.do_action(self.id)

    def get_inventory_contents(self):
        return self.inventory
