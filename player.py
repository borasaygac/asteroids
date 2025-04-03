import pygame, sys
from circleshape import CircleShape
from constants import *
from shot import Shot
# Class for the player obkect
class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.score = 0 

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): # draws the player "triangle"
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        self.shot_timer -= dt # If the player has shot and is in cooldown, decrease cooldown time by dt    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt=-dt)
        if keys[pygame.K_d]:
            self.rotate(dt=dt)
        if keys[pygame.K_w]:
            self.move(dt=dt)
        if keys[pygame.K_s]:
            self.move(dt=-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_ESCAPE]: # Currently directly exits, will provide a screen later
            sys.exit()
            

    def shoot(self):
        if self.shot_timer > 0:
            return
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(x=self.position.x, y=self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def increase_score(self, amount):
        self.score += amount
        print(f"current score {self.score}")
        
    