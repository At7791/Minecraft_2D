import pygame
from pygame import *

class PlayerClass():
    def __init__(self, sizeX, sizeY):
        self.x, self.y = float(2), float(2)
        self.velocityX, self.velocityY = float(0), float(0)
        self.accelerationX, self.accelerationY = float(0.1), float(0)
        self.friction = 0.001



    
    def draw(self, surface, zoom, windowSize):
        self.windowSizeX, self.windowSizeY = windowSize
        self.xOnScreen = self.windowSizeX // 2
        self.yOnScreen = self.windowSizeY // 2
        pygame.draw.circle(surface, Color("red"), (self.xOnScreen, self.yOnScreen), 10)
    
    def updates(self, events):
        # movement related player updates
        if self.velocityX >= 0:
            self.accelerationX -= self.friction
        # if self.velocityY >= 0:
        #     self.accelerationY -= self.friction

        self.velocityX += self.accelerationX
        self.velocityY += self.accelerationY

        self.x += self.velocityX
        self.y += self.velocityY



        if events.forwardKeyPressed == True:
            print("Go foreward (in the direction the player is facing)")

        if events.backwardKeyPressed == True:
            print("Go backward (in the direction the player is facing)")

    def getPlayerCoordinates(self):
        return (self.x, self.y)