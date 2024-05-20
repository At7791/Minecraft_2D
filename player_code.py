from entity_code import EntityClass
from hitbox_code import Hitboxes
from pygame import *
import pygame

class PlayerClass(EntityClass):
    def __init__(self):
        super().__init__()
        self.hitbox = Hitboxes(0.6, 1.8)
        self.x, self.y = float(2.5), float(1)
        

    def updatesPhysics(self, events, calibrationFPS):
        super().updatesPhysics(calibrationFPS)

        # applies the effect to the player movement of the keypresses
        if events.forwardKeyPressed == True:
            self.accelerationX = 0.1
        elif events.backwardKeyPressed == True:
            self.accelerationX = -0.1
        else:
            self.accelerationX = 0
        if events.sprintKeyPressed == True:
            self.accelerationX *= 1.3
        if events.jumpKeyPressed == True and self.onGround == True:
            self.velocityY = 0.42

        if events.debugTrigger1 == True:
            self.y = 0
            self.x = 0

    def draw(self, surface, zoom, windowSize):
        self.windowSizeX, self.windowSizeY = windowSize
        self.xOnScreen = self.windowSizeX // 2
        self.yOnScreen = self.windowSizeY // 2
        pygame.draw.circle(surface, Color("red"), (self.xOnScreen, self.yOnScreen), 10)

    def getPlayerCoordinates(self):
        return (self.x, self.y)