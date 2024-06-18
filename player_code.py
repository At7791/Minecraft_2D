from entity_code import EntityClass
from hitbox_code import Hitboxes
from pygame import *
import pygame

class PlayerClass(EntityClass):
    def __init__(self):
        super().__init__()
        self.hitbox = Hitboxes(0.6, 1.8)
        self.x, self.y = float(49), float(4)
        self.count = 0
        

    def updatesPhysics(self, events, calibrationFPS):
        super().updatesPhysics(calibrationFPS)
        self.accelerationY = 0
        if abs(self.velocityY) < 0.003:
            self.velocityY = 0
        self.count += 1
        # applies the effect to the player movement of the keypresses
        if events.forwardKeyPressed == True:
            self.accelerationX = 0.1
        elif events.backwardKeyPressed == True:
            self.accelerationX = -0.1
        else:
            self.accelerationX = 0
        if events.shiftKeyPressed == True:
            self.accelerationX *= 0.3
            print("hello")
        elif events.sprintKeyPressed == True:
            self.accelerationX *= 1.3 * 5
        if events.jumpKeyPressed == True and self.onGround == True:
            self.velocityY = 0.7

        if events.debugTrigger1 == True:
            self.y = 10
            self.x = 7.5
            self.count = 0
        
        
        # if self.velocityY < -3.91990:
        #     print(self.count, self.velocityY)
        # else:
        #     print(self.velocityY)

    def draw(self, surface, zoom, windowSize):
        self.windowSizeX, self.windowSizeY = windowSize
        self.xOnScreen = self.windowSizeX // 2
        self.yOnScreen = self.windowSizeY // 2
        pygame.draw.circle(surface, Color("red"), (self.xOnScreen, self.yOnScreen), 10)

    def getPlayerCoordinates(self):
        return (self.x, self.y)