import pygame
from pygame import *

class EntityClass():
    def __init__(self):
        self.x, self.y = float(2), float(2)
        self.velocityX, self.velocityY = float(0), float(0)
        self.accelerationX, self.accelerationY = float(0), float(0)
        self.onGround = True
        self.xOnScreen = 0
        self.yOnScreen = 0
    
    def updates(self, events, deltaTime, TPS):
        # movement related entity updates
        calibrationFPS = deltaTime * TPS

        self.velocityX = self.velocityX * 0.546 + self.accelerationX
        self.velocityY = (self.velocityY - 0.08) * 0.98

        self.x += self.velocityX * calibrationFPS
        self.y += self.velocityY * calibrationFPS
    
class PlayerClass(EntityClass):
    def __init__(self):
        super().__init__()

    def updates(self, events, deltaTime, TPS):
        super().updates(events, deltaTime, TPS)
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

    def draw(self, surface, zoom, windowSize):
        self.windowSizeX, self.windowSizeY = windowSize
        self.xOnScreen = self.windowSizeX // 2
        self.yOnScreen = self.windowSizeY // 2
        pygame.draw.circle(surface, Color("red"), (self.xOnScreen, self.yOnScreen), 10)

    def getPlayerCoordinates(self):
        return (self.x, self.y)
    
