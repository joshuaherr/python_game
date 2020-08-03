import pygame

import uuid

from components.screen_components import ScreenComponents

PIXEL_MOVEMENT = 4


class CharacterBase:
    """Base Character object."""
    CHAR_LAYER = 200

    def __init__(self, speed, image, layer):
        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.sub_layer = layer
        self.density = 1
        self.id = uuid.uuid4()
        self.health = 1
        self.money = 0
        self.has_action = False

    def get_layer(self):
        return self.CHAR_LAYER + self.sub_layer

    def set_sub_layer(self, layer):
        self.sub_layer = layer

    def move_down(self):
        speed_check = self.rect.bottom + (self.speed * PIXEL_MOVEMENT)
        height = ScreenComponents().get_screen_size()[0]
        if not speed_check > height:
            down_speed = self.speed * PIXEL_MOVEMENT
            move_speed = [0, down_speed]
            self.rect = self.rect.move(move_speed)

    def move_up(self):
        speed_check = self.rect.top + (self.speed * -PIXEL_MOVEMENT)
        if not speed_check < 0:
            up_speed = self.speed * -PIXEL_MOVEMENT
            move_speed = [0, up_speed]
            self.rect = self.rect.move(move_speed)

    def move_right(self):
        speed_check = self.rect.right + (self.speed * PIXEL_MOVEMENT)
        width = ScreenComponents().get_screen_size()[1]
        if not speed_check > width:
            right_speed = self.speed * PIXEL_MOVEMENT
            move_speed = [right_speed, 0]
            self.rect = self.rect.move(move_speed)

    def move_left(self):
        speed_check = self.rect.left + (self.speed * -PIXEL_MOVEMENT)
        if not speed_check < 0:
            left_speed = self.speed * -PIXEL_MOVEMENT
            move_speed = [left_speed, 0]
            self.rect = self.rect.move(move_speed)

    def handle_event(self, event):
        pass

    def do_action(self, player_id):
        pass
