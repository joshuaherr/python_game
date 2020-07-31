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
import pygame


class MainCharacter(CharacterBase):
    """Main Character controlled by the user."""

    def __init__(self):
        super().__init__(1, str(get_move_down_stand_image()), 1)
        self.movement_state = MovementStates.MOVE_DOWN_STAND
        self.character_direction = Directions.DOWN

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == 274:
                if self.character_direction == Directions.DOWN:
                    self.move_down()
                    self.update_image_movement()
                else:
                    self.character_direction = Directions.DOWN
                    self.movement_state = MovementStates.MOVE_DOWN_STAND
                    self.image = pygame.image.load(str(get_move_down_stand_image()))
            if event.key == 275:
                if self.character_direction == Directions.RIGHT:
                    self.move_right()
                    self.update_image_movement()
                else:
                    self.character_direction = Directions.RIGHT
                    self.movement_state = MovementStates.MOVE_RIGHT_STAND
                    self.image = pygame.image.load(str(get_move_right_stand_image()))
            if event.key == 273:
                if self.character_direction == Directions.UP:
                    self.move_up()
                    self.update_image_movement()
                else:
                    self.character_direction = Directions.UP
                    self.movement_state = MovementStates.MOVE_UP_STAND
                    self.image = pygame.image.load(str(get_move_up_stand_image()))
            if event.key == 276:
                if self.character_direction == Directions.LEFT:
                    self.move_left()
                    self.update_image_movement()
                else:
                    self.character_direction = Directions.LEFT
                    self.movement_state = MovementStates.MOVE_LEFT_STAND
                    self.image = pygame.image.load(str(get_move_left_stand_image()))

    def update_image_movement(self):
        print(f"Movement state: {self.movement_state}")
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
