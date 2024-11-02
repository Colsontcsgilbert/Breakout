from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame import Vector2
from pygame.locals import *
from sys import exit
from paddle import Paddle
from ball import Ball
from brick import Brick
from random import randint, choice
pygame.init()
FPS = 30
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("BoB")
clock = pygame.time.Clock()
revert_paddle = USEREVENT
spawn_power = USEREVENT + 1
pygame.time.set_timer(spawn_power,10_000)
paddle =Paddle()
ball = Ball()

bricks = []
colors = ["blue2","olivedrab3","firebrick"]
for y in range(30, 200, 10):
    row = []
    color = colors [(y-30)//60]
    for x in range(30,570, 30):
        row.append(Brick(color, (x, y)))
    bricks.append(row)

class Power:
    @staticmethod
    def long_paddle():
        global paddle
        paddle.rect.w +=20
        pygame.time.set_timer(revert_paddle, 20_000)
    @staticmethod
    #def teleport():
    def short_paddle():
        global paddle
        paddle.rect.w -=5
        pygame.time.set_timer(revert_paddle, 20_000)

    def __init__(self):
        self.rect = Rect(randint(0,500),-20,20,20)
        effects = [
            self.long_paddle,
            self.short_paddle
            ]
        self.effect = choice(effects)

    def update(self):
        self.rect.y+= 4

    def draw(self, screen):
            pygame.draw.circle(screen,(0,255,0), self.rect.center, self.rect.w// 2)
    

power = Power()
def main():
    while True:
        clock.tick(FPS)
        handle_events()
        update()
        draw()

def handle_events():
    global power
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == revert_paddle:
            paddle.rect.w = 30
        if event.type == spawn_power:
            power = Power()

def update():
    paddle.update()
    ball.update()
    if power is not None: power.update()
    handle_colision()



def draw():
    screen.fill((255,255,255))
    paddle.draw(screen)
    ball.draw (screen)
    for row in bricks:
        for brick in row:
            brick.draw(screen)
    if power is not None:
        power.draw(screen)
    pygame.display.flip()

def handle_colision():
    global power
    if ball.rect.colliderect(paddle.rect)and ball.velocity.y>=0:
        magnitude = ball.velocity.magnitude()
        ball.velocity = Vector2 (ball.rect.center) - Vector2 (paddle.rect.center)
        if ball.velocity.magnitude() == 0:
            ball.velocity = Vector2(0,-1)
        ball.velocity.scale_to_length(magnitude)
        # point = Vector2(paddle.rect.center)
        # point.y +=30
        # normal = Vector2(ball.rect.center) - point
        # ball.velocity.reflect_ip(normal)
    for row in bricks:
        for brick in [brick for brick in row if not brick.hidden]:
            if not ball.rect.colliderect(brick.rect): continue
            magnitude = ball.velocity.magnitude()
            ball.velocity = Vector2 (ball.rect.center) - Vector2 (brick.rect.center)
            if ball.velocity.magnitude() == 0:
                ball.velocity = Vector2(0,-1)
            ball.velocity.scale_to_length(magnitude)
            
            # if ball.rect.bottom in range(brick.rect.top, brick.rect.top + 5):
            #     ball.velocity.reflect_ip(Vector2(0,1))
            # if ball.rect.top in range(brick.rect.bottom - 5, brick.rect.bottom):
            #     ball.velocity.reflect_ip(Vector2(0,1))
            # if ball.rect.right in range(brick.rect.left, brick.rect.left + 5):
            #     ball.velocity.reflect_ip(Vector2(1,0))
            # if ball.rect.left in range(brick.rect.right - 5, brick.rect.right):
            #     ball.velocity.reflect_ip(Vector2(1,0))
            brick.hidden = True
    if power is not None:
        if power.rect.colliderect(paddle.rect):
            power.effect()
            power = None

main()