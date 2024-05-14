import pygame
from pygame import *

class PlayerClass():
    def __init__(self, sizeX, sizeY):
        self.x, self.y = float(2), float(2)
    
    def draw(self, surface, zoom, windowSize):
        self.windowSizeX, self.windowSizeY = windowSize
        self.xOnScreen = self.windowSizeX // 2
        self.yOnScreen = self.windowSizeY // 2
        pygame.draw.circle(surface, Color("red"), (self.xOnScreen, self.yOnScreen), 10)
    
    def updates(self, events):
        if events.forwardKeyPressed == True:
            print("Go foreward (in the direction the player is facing)")
        if events.backwardKeyPressed == True:
            print("Go backward (in the direction the player is facing)")

    def getPlayerCoordinates(self):
        return (self.x, self.y)