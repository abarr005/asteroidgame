import pygame, random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = velocity
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("this was a small asteroid and we're done")
        else:
            angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(angle)
            new_velocity2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity1 * 1.2)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity2 * 1.2)

