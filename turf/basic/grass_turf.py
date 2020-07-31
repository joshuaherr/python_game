from utilities.file_helpers import get_turf_images_path
from turf.turf_base import TurfBase


class GrassTurf(TurfBase):
    """Basic Grass Turf."""

    def __init__(self):
        grass_image = get_turf_images_path() / "grass1.png"
        super().__init__(str(grass_image), 1)
        self.x_coordinate = 0
        self.y_coordinate = 0

    def set_coordinates(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.rect.x = x
        self.rect.y = y
