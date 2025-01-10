import pygame
import random
from circleshape import *
from constants import *

class Shot(CircleShape):
    SHOT_RADIUS = 5
    def __init__(self, x, y):
        super().__init__(x, y, self.SHOT_RADIUS)
        
    
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
