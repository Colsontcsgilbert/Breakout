import pygame
from pygame import Rect, Surface 
from pygame.locals import *
class Paddle:
     def __init__(self):
        self.rect = Rect(0,0,30,5)
        self.rect.center = (300,350)
     def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.rect.x += 9
        if keys[K_LEFT]:
            self.rect.x += -9
        self.rect.x = pygame.math.clamp(self.rect.x, 0,600-self.rect.w)
            
     def draw(self, screen:Surface):
          pygame.draw.rect(screen, "black", self.rect)