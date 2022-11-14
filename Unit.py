import os
import pygame
import pygame.image


class player(object):
    run = [pygame.image.load(os.path.join('sauce_image', 'yosi1.png')),
           pygame.image.load(os.path.join('sauce_image', 'yosi2.png')),
           pygame.image.load(os.path.join('sauce_image', 'yosi3.png')),
           pygame.image.load(os.path.join('sauce_image', 'yosi4.png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.runCount = 0

    def draw(self, win):
        win.blit(self.run[self.runCount % 4], (self.x, self.y))
        self.runCount += 1