import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            positive_velocity = self.velocity.rotate(split_angle)
            negative_velocity = self.velocity.rotate(split_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroids = (
                Asteroid(self.position.x, self.position.y, new_radius),
                Asteroid(self.position.x, self.position.y, new_radius),
            )

            a1, a2 = new_asteroids
            a1.velocity = positive_velocity * 1.2
            a2.velocity = negative_velocity * 1.2
