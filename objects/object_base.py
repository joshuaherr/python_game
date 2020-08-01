import pygame
import uuid


class ObjectBase:
    """Base class for all objects."""

    OBJECT_LAYER = 400

    def __init__(self, layer, image):
        self.sub_layer = layer
        self.id = uuid.uuid4()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.density = 1
        self.original_density = self.density

    def get_layer(self):
        return self.OBJECT_LAYER + self.sub_layer

    def set_layer(self, layer):
        self.sub_layer = layer

    def set_coordinates(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.rect.x = x
        self.rect.y = y

    def handle_event(self, event):
        pass
