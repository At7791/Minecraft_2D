import pygame
from pygame import *
import sys

class Events():
    def __init__(self):
        self.backwardKeyPressed = False
        self.forwardKeyPressed = False

    def eventsMain(self):
        for event in pygame.event.get():
            # Exit program through pressing the windows red cross
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Keys pressed
            if event.type == KEYDOWN:
                # Exit program through pressing tab
                if event.key == K_TAB:
                    pygame.quit()
                    sys.exit()

                # Player movement related keys
                if event.key == K_w:
                    self.forwardKeyPressed = True
                if event.key == K_s:
                    self.backwardKeyPressed = True

            # Keys unpressed
            if event.type == KEYUP:
                # Player movement related keys
                if event.key == K_w:
                    self.forwardKeyPressed = False
                if event.key == K_s:
                    self.backwardKeyPressed = False