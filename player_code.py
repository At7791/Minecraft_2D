import pygame
from pygame import *

class PlayerClass():
    def __init__(self, sizeX, sizeY):
        self.x, self.y = float(2), float(2)
        self.velocityX, self.velocityY = float(0), float(0)
        self.accelerationX, self.accelerationY = float(0), float(0)
        self.onGround = True


    def draw(self, surface, zoom, windowSize):
        self.windowSizeX, self.windowSizeY = windowSize
        self.xOnScreen = self.windowSizeX // 2
        self.yOnScreen = self.windowSizeY // 2
        pygame.draw.circle(surface, Color("red"), (self.xOnScreen, self.yOnScreen), 10)
    
    def updates(self, events, deltaTime, TPS):
        # movement related player updates
        calibrationFPS = deltaTime * TPS

        self.velocityX = self.velocityX * 0.546 + self.accelerationX
        self.velocityY = (self.velocityY - 0.08) * 0.98

        self.x += self.velocityX * calibrationFPS
        self.y += self.velocityY * calibrationFPS

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

    def getPlayerCoordinates(self):
        return (self.x, self.y)