import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from player import Player


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, player):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            player.increase_score(3) # smallest asteroids reward the biggest points 
            return
        else: # creates 2 new velocity vectors with randam angle between 20 and 50 degrees.
              # Then creates 2 new asteroids on the spot the old one died. Also calls the 
              # increase_score function.
            rand_angle = random.uniform(20, 50)
            new_velocity_vector_positive = self.velocity.rotate(rand_angle)
            new_velocity_vector_negative = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            if new_radius == 40:
                player.increase_score(2) # medium asteroid gives medium reward
            elif new_radius == 20:
                player.increase_score(1) # biggest asteroid the smallest reward
            
            splitted_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            splitted_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

            splitted_asteroid_one.velocity = new_velocity_vector_positive * 1.2
            splitted_asteroid_two.velocity = new_velocity_vector_negative * 1.2