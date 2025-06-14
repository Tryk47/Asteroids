import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    # draws the shape onto the screen
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt