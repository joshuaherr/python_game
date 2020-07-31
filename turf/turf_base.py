import pygame
import uuid


class TurfBase:
	"""Turf base class for all background turf."""
	TURF_LAYER = 0

	def __init__(self, image, layer):
		self.image = pygame.image.load(image)
		self.density = 0
		self.rect = self.image.get_rect()
		self.sub_layer = layer
		self.id = uuid.uuid4()

	def get_layer(self):
		return self.TURF_LAYER + self.sub_layer

	def set_sub_layer(self, layer):
		self.sub_layer = layer

	def handle_event(self, event):
		pass
