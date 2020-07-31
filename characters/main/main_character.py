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
        self.inventory = CharacterInventory()
        self.health = 100

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
                        print("Cannot move there!")
                        return
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
                        print("Cannot move there!")
                        return
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
                        print("Cannot move there!")
                        return
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
                        print("Cannot move there!")
                        return
                else:
                    self.character_direction = Directions.LEFT
                    self.movement_state = MovementStates.MOVE_LEFT_STAND
                    self.image = pygame.image.load(str(get_move_left_stand_image()))
            elif event.key == 105:
                # inventory key pressed
                if not self.is_inventory_open:
                    self.is_inventory_open = True
                    self.can_move = False
                    ScreenComponents().add_screen_component(self.inventory)
                else:
                    self.is_inventory_open = False
                    self.can_move = True
                    ScreenComponents().remove_screen_component(self.inventory.id)

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

    def is_movement_allowed(self):
        speed_check = 4 * self.speed
        rect_copy = copy.copy(self.rect)
        if self.character_direction == Directions.DOWN:
            rect_copy.bottom = self.rect.bottom + speed_check
        if self.character_direction == Directions.UP:
            rect_copy.top = self.rect.top - speed_check
        if self.character_direction == Directions.LEFT:
            rect_copy.left = self.rect.left - speed_check
        if self.character_direction == Directions.RIGHT:
            rect_copy.right = self.rect.right + speed_check
        relevant_comps = []
        for comp in ScreenComponents().get_components():
            if comp.density > 0 and comp.id != self.id:
                relevant_comps.append(comp)
        print(f"Density Components: {len(relevant_comps)}")
        screen_rects = [comp.rect for comp in relevant_comps]
        print(f"Rectangles: {len(screen_rects)}")
        collisions = rect_copy.collidelist(screen_rects)
        print(f"Collisions: {collisions}")
        if collisions == -1:
            return True
        else:
            return False
