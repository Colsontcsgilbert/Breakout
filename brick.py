import pygame
from pygame import Rect, Surface, Vector2
class Brick:
    def __init__(self, color, pos):
        self.color = color
        self. rect = Rect (pos,(30,10))
        self.hidden = False
    def draw(self, screen:Surface):
        if self.hidden: return
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, 2)

