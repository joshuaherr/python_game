from turf.turf_base import TurfBase

import pygame

import sys

class_instance = None


class ScreenComponents:
    """Screen Components for the code."""

    class __ScreenComponentsSingleton:
        """Singleton private instance."""

        def __init__(self):
            self.height = 0
            self.width = 0
            self.components = []
            self.screen = None

    instance = None

    def __init__(self):
        if not ScreenComponents.instance:
            ScreenComponents.instance = ScreenComponents.__ScreenComponentsSingleton()

    def set_screen_size(self, height, width):
        self.instance.height = height
        self.instance.width = width

    def add_screen_component(self, component):
        self.instance.components.append(component)

    def get_screen_size(self):
        return self.instance.height, self.instance.width

    def set_screen(self, screen):
        self.instance.screen = screen

    def render_components(self):
        if not self.instance or not self.instance.screen:
            print("Screen Components are not properly initialized.")
            return
        sorted_layers = sorted(self.instance.components, key=lambda comp: comp.get_layer())
        for comp in sorted_layers:
            if isinstance(comp, TurfBase):
                self.instance.screen.blit(comp.image.convert(), (comp.x_coordinate, comp.y_coordinate))
            else:
                self.instance.screen.blit(comp.image, comp.rect)
        pygame.display.flip()

    def run_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(f"Event: {event}")
            if event.type == pygame.QUIT:
                sys.exit()
            for comp in self.instance.components:
                comp.handle_event(event)
