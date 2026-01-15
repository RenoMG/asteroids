from circleshape import CircleShape
from constants import *
from logger import log_event
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        random_angel = random.uniform(25, 50)
        
        asteroid_1 = self.velocity.rotate(random_angel)
        asteroid_2 = self.velocity.rotate(random_angel - random_angel * 2)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1_obj = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1_obj.velocity = asteroid_1 * 1.2
        asteroid_2_obj = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2_obj.velocity = asteroid_2 * 1.2



