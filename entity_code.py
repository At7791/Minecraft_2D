import pygame, math
from pygame import *
from math import *

class Hitboxes():
    def __init__(self, lengthX, lengthY):
        self.lengthX, self.lengthY = lengthX, lengthY
        self.offsetWithX = self.lengthX / 2
        self.offsetWithY = 0.5

        self.highBorder = 0
        self.lowBorder = 0
        self.leftBorder = 0
        self.rightBorder = 0

    def update(self, x, y):
        self.highBorder = y - self.offsetWithY + self.lengthY
        self.lowBorder = y - self.offsetWithY
        self.leftBorder = x - self.offsetWithX
        self.rightBorder = x + self.offsetWithX

class EntityClass():
    worldMatrix = []

    def __init__(self):
        self.x, self.y = float(0), float(0)
        self.velocityX, self.velocityY = float(0), float(-0.0000001)
        self.accelerationX, self.accelerationY = float(0), float(0)
        self.onGround = True
        self.xOnScreen = 0
        self.yOnScreen = 0
        self.hitbox = None
    
    def updates(self, deltaTime, TPS):
        # movement and collision related entity updates
        self.hitbox.update(self.x, self.y)
        calibrationFPS = deltaTime * TPS

        # if self.velocityY > 0:
        #     self.velocityY = (self.velocityY - 0.08) * 0.98

        print(f"{floor(self.hitbox.lowBorder) - 1} {floor(self.y)}")
        if self.velocityY < 0:
            if floor(self.hitbox.lowBorder - 1) in range(len(self.__class__.worldMatrix[floor(self.x)])):
                if self.__class__.worldMatrix[floor(self.x)][floor(self.hitbox.lowBorder) - 1] != "air":
                    self.velocityY = 0
                else:
                    self.velocityY = (self.velocityY - 0.02) * 0.98
            else:
                self.velocityY = (self.velocityY - 0.02) * 0.98



        self.velocityX = self.velocityX * 0.546 + self.accelerationX
        

        self.x += self.velocityX * calibrationFPS
        self.y += self.velocityY * calibrationFPS



class PlayerClass(EntityClass):
    def __init__(self):
        super().__init__()
        self.hitbox = Hitboxes(0.6, 1.8)
        self.x, self.y = float(3.5), float(15)
        

    def updates(self, events, deltaTime, TPS):
        super().updates(deltaTime, TPS)

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

    def draw(self, surface, zoom, windowSize):
        self.windowSizeX, self.windowSizeY = windowSize
        self.xOnScreen = self.windowSizeX // 2
        self.yOnScreen = self.windowSizeY // 2
        pygame.draw.circle(surface, Color("red"), (self.xOnScreen, self.yOnScreen), 10)

    def getPlayerCoordinates(self):
        return (self.x, self.y)