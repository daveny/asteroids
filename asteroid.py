import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            self.spawn(self.radius // 2, self.position, self.velocity*1.2)
            self.spawn(self.radius // 2, self.position, self.velocity*1.2)

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity.rotate(random.randint(-30, 30))
        return asteroid
        