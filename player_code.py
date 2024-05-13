import pygame
from pygame import *

class PlayerClass():
    def __init__(self):
        self.x, self.y = float(4), float(2)
    
    def draw(self, surface, sizeOfBlock, windowSize):
        self.windowSizeX, self.windowSizeY = windowSize
        self.xOnScreen = self.windowSizeX // 2
        self.yOnScreen = self.windowSizeY // 2
        pygame.draw.circle(surface, Color("red"), (self.xOnScreen, self.yOnScreen), 30)
    
    def updates(self):
        print("does all the calculations")

    def getPlayerCoordinates(self):
        return (self.x, self.y)