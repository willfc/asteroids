import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, dt):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_vector_1 = self.velocity.rotate(-random_angle)
            new_vector_2 = self.velocity.rotate(random_angle)
            new_radi = self.radius - ASTEROID_MIN_RADIUS
        
            split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radi)
            split_asteroid_1.velocity = new_vector_1
            split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radi)
            split_asteroid_2.velocity = new_vector_2