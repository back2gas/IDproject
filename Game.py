import pygame
from pygame import *
import sys
import os
import math
import Unit

pygame.init()
vec = pygame.math.Vector2

HEIGTH = 800
WIDTH = 1280

FramePerSec = pygame.time.Clock()
win = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("DianoGame")

bg = pygame.image.load(os.path.join('sauce_image', 'background.png')).convert()
bgX = 0
bgX2 = bg.get_width()
clock = pygame.time.Clock()
FramePerSec = 60

run = True
speed = 150

Diano = Unit.player(600, 313, 100, 100)
def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    Diano.draw(win)
    pygame.display.update()

pygame.time.set_timer(USEREVENT+1, 500)



while run:
    redrawWindow()
    clock.tick(speed)
    bgX -= 1.4
    bgX2 -= 1.4

    if bgX < bg.get_width()*-1:
        bgX = bg.get_width()

    if bgX2 < bg.get_width()*-1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit()
            quit()
            sys.exit()

        if event.type == USEREVENT+1:
            speed += 1

    clock.tick(speed)





