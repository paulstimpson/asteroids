from circleshape import CircleShape 
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,width=2)

    def split(self):
        self.kill()
        if self.radius >= ASTEROID_MIN_RADIUS:
            split_angle = random.uniform(20, 50)
            new_radius=self.radius-ASTEROID_MIN_RADIUS
            a = Asteroid(self.position.x, self.position.y, new_radius)
            a.velocity = self.velocity.rotate(split_angle)*1.2
            b = Asteroid(self.position.x, self.position.y, new_radius)
            b.velocity = self.velocity.rotate(-split_angle)*1.2
            return [a, b]
        return []