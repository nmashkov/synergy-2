# import pygame
import pymunk
import pymunk.pygame_util

import settings


class Earth:
    def __init__(self, app):
        self.app = app
        # earth params
        self.earth_radius = settings.earth_radius
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = (settings.WIDTH // 2, settings.HEIGHT)
        self.shape = pymunk.Circle(self.body, self.earth_radius)
        self.shape.color = settings.light_grey
        self.shape.friction = settings.earth_friction
        self.app.space.add(self.body, self.shape)
