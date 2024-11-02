import pygame
from pygame import Rect, Surface, Vector2

class Ball:
    speed = 6.5
    def __init__(self):
        self.rect: Rect = Rect(0,0,10,10)
        self.rect.center = (300, 300)
        self.velocity:Vector2 = Vector2(5,-5)
        self.velocity.scale_to_length(Ball.speed)
    def update(self):
        if self.velocity.y == 0:
            self.velocity = Vector2(5,-5)
            self.velocity.scale_to_length(Ball.speed)
        self.rect.center += self.velocity
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.reflect_ip(Vector2(0,1))
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.reflect_ip(Vector2(1,0))
        if self.rect.right >= 600:
            self.rect.right = 599
            self.velocity.reflect_ip(Vector2(1,0))
        if self.velocity.y == 0:
            self.velocity.y = -5
    def draw(self, screen:Surface):
        pygame.draw.ellipse(screen, 'green4', self.rect)
