import pygame
from pygame import *
import sys

class Events():
    def __init__(self):
        self.backwardKeyPressed = False
        self.forwardKeyPressed = False
        self.sprintKeyPressed = False
        self.crouchKeyPressed = False
        self.jumpKeyPressed = False
        self.f3KeyPressed = False
        self.clicking = False

        self.mouseX = 0
        self.mouseY = 0

        # debug variables
        self.debugTrigger1 = False

    def eventsMain(self):
        
        
        self.f3KeyPressed = False

        for event in pygame.event.get():
            # Exit program through pressing the windows red cross
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse related events
            self.mouseX, self.mouseY = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONDOWN:
                self.clicking = True
            elif event.type == MOUSEBUTTONUP:
                self.clicking = False
            # Keys pressed
            if event.type == KEYDOWN:
                # Exit program through pressing tab
                if event.key == K_TAB:
                    pygame.quit()
                    sys.exit()

                # Player event related keys
                if event.key == K_d:
                    self.forwardKeyPressed = True
                elif event.key == K_a:
                    self.backwardKeyPressed = True
                elif event.key == K_LCTRL:
                    self.sprintKeyPressed = True
                elif event.key == K_SPACE:
                    self.jumpKeyPressed = True
                elif event.key == K_F3:
                    self.f3KeyPressed = True
                elif event.key == K_LSHIFT or event.key == K_RSHIFT:
                    self.crouchKeyPressed = True


                # debug keys
                if event.key == K_u:
                    self.debugTrigger1 = True

            # Keys unpressed
            if event.type == KEYUP:
                # Player movement related keys
                if event.key == K_d:
                    self.forwardKeyPressed = False
                elif event.key == K_a:
                    self.backwardKeyPressed = False
                elif event.key == K_LCTRL:
                    self.sprintKeyPressed = False
                elif event.key == K_SPACE:
                    self.jumpKeyPressed = False
                elif event.key == K_LSHIFT or event.key == K_RSHIFT:
                    self.crouchKeyPressed = False
                # debug keys
                elif event.key == K_u:
                    self.debugTrigger1 = False