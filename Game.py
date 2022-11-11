import pygame
from pygame import *
import sys

pygame.init()
vec = pygame.math.Vector2

HEIGTH = 800
WIDTH = 600
ACC = 0.5
FRIC = -0.01
FPS = 60

FramePerSec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("DianoGame")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((0, 0, 0))


    pygame.display.update()
    FramePerSec.tick(FPS)