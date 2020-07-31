import pygame


class TurfBase:
	"""Turf base class for all background turf."""
	TURF_LAYER = 0

	def __init__(self, image, density, layer):
		self.image = pygame.image.load(image)
		self.density = density
		self.rect = self.image.get_rect()
		self.sub_layer = layer

	def get_layer(self):
		return self.TURF_LAYER + self.sub_layer

	def set_sub_layer(self, layer):
		self.sub_layer = layer

	def handle_event(self, event):
		pass
