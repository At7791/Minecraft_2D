import pygame
from pygame import *
import sys

class Events():
    def __init__(self):
        self.backwardKeyPressed = False
        self.forwardKeyPressed = False
        self.sprintKeyPressed = False
        self.jumpKeyPressed = False

        # debug variables
        self.debugTrigger1 = False

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
                if event.key == K_d:
                    self.forwardKeyPressed = True
                if event.key == K_a:
                    self.backwardKeyPressed = True
                if event.key == K_LCTRL:
                    self.sprintKeyPressed = True
                if event.key == K_SPACE:
                    self.jumpKeyPressed = True

                # debug keys
                if event.key == K_u:
                    self.debugTrigger1 = True

            # Keys unpressed
            if event.type == KEYUP:
                # Player movement related keys
                if event.key == K_d:
                    self.forwardKeyPressed = False
                if event.key == K_a:
                    self.backwardKeyPressed = False
                if event.key == K_LCTRL:
                    self.sprintKeyPressed = False
                if event.key == K_SPACE:
                    self.jumpKeyPressed = False

                # debug keys
                if event.key == K_u:
                    self.debugTrigger1 = False