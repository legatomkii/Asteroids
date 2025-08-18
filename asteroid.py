import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    #Logic for Asteroids to split on death into 2 smaller ones
    def split(self):
        random_angle = random.uniform(20,50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_vector_1 = self.velocity.rotate(random_angle)
            new_vector_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = new_vector_1 * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = new_vector_2 * 1.2