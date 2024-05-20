import pygame, math, hitbox_code
from pygame import *
from math import trunc
from hitbox_code import Hitboxes
        
class EntityClass():
    worldMatrix = []
    def __init__(self):
        self.x, self.y = float(0), float(0)
        self.nextX, self.nextY = self.x, self.y
        self.velocityX, self.velocityY = float(0), float(-0.0000001)
        self.nextVelocityX, self.nextVelocityY = self.velocityX, self.velocityY
        self.accelerationX, self.accelerationY = float(0), float(0)
        self.onGround = True
        self.xOnScreen = 0
        self.yOnScreen = 0
        self.hitbox = None
        self.updateY = True
        
    def isBlockInWorld(self, x = int, y = int):
        if x >= 0 and y >= 0:
            if x in range(len(self.__class__.worldMatrix)) and y in range(len(self.__class__.worldMatrix[0]) + 1):
                return True
            else:
                return False
        return False

    def updatesPhysics(self, calibrationFPS):
        # movement and collision related entity updates
        self.tx, self.ty = trunc(self.x), trunc(self.y)
        self.hitbox.update(self.x, self.y)

        self.nextVelocityX = (self.velocityX * 0.546 + self.accelerationX)
        self.nextVelocityY = ((self.velocityY - 0.02) * 0.98)
        self.nextX = self.x + self.nextVelocityX * calibrationFPS
        self.nextY = self.y + self.nextVelocityY * calibrationFPS

        self.lowAir = True
        self.highAir = True
        self.lowBlockBorder = False
        self.highBlockBorder = False

        if self.nextVelocityY <= 0:
            for block in self.hitbox.lowBlocks():
                if self.isBlockInWorld(block[0], block[1]):
                # if block[0] in range(len(self.__class__.worldMatrix)) and block[1] in range(len(self.__class__.worldMatrix[0]) + 1):
                    if self.__class__.worldMatrix[block[0]][block[1] - 1] != "air":
                        self.lowAir = False
                    if self.nextY <= block[1]:
                        self.lowBlockBorder = True
        if self.nextVelocityY >= 0:
            for block in self.hitbox.highBlocks():
                if self.isBlockInWorld(block[0], block[1]):
                    if self.__class__.worldMatrix[block[0]][block[1]] != "air":
                        self.highAir = False
                    if self.nextY <= block[1]:  
                        self.highBlockBorder = True
#
        if self.lowAir and self.highAir:
            self.y = self.nextY
            self.velocityY = self.nextVelocityY
        else:
            if self.lowBlockBorder:
                self.velocityY = 0
                self.y = trunc(self.y)
            elif self.highBlockBorder:
                self.velocityY = 0
                self.y = trunc(self.hitbox.highBorder) - self.hitbox.lengthY
            else:
                self.y = self.nextY
                self.velocityY = self.nextVelocityY

        self.rightAir = True
        self.leftAir = True
        self.leftBlockBorder = False
        self.rightBlockBorder = False

        # if self.velocityX <= 0:
        if self.velocityX >= 0:
            for block in self.hitbox.rightBlocks():
                if self.isBlockInWorld(block[0], block[1]):
                    if self.__class__.worldMatrix[block[0]][block[1]] != "air":
                        self.rightAir = False
                    if self.nextX + self.hitbox.offsetWithX >= block[0]:  
                        self.rightBlockBorder = True


        
        print(f" air to the right: {self.rightAir} override blocksize {self.rightBlockBorder}")
        # print(trunc(self.hitbox.rightBorder), self.x)
        if self.rightAir:
            self.x = self.nextX
            self.velocityX = self.nextVelocityX
        else:
            if self.rightBlockBorder:
                self.velocityX = 0
                self.x = trunc(self.nextX + 1) - self.hitbox.offsetWithX

        # for columns in self.hitbox.blocksOverlapped:
        #     for j in self.hitbox.blocksOverlapped[i]:
        #         if j[0] in range(len(self.__class__.worldMatrix)) and j[1] in range(len(self.__class__.worldMatrix[0])):


        #             if self.velocityY == 0:
        #                 if self.__class__.worldMatrix[j[0]][j[1] - 1] != "air":
        #                     if j[1] != self.y:
                            
        #                         # print(j, self.__class__.worldMatrix[j[0]][j[1]], j[1], self.y)
        #                         if self.nextY <= j[1]:
        #                             self.velocityY = 0
        #                             self.y = j[1]
        #                 else:
        #                     self.updateY = True
        #         else:
        #             self.updateY = True

        # if self.updateY:
        #     self.updateXY(True, True)
        # self.updateY = False
        # self.updateXY(True, False)

        #                 elif self.velocityY > 0:
        #                 else:

        # if floor(self.hitbox.lowBorder) in range(len(self.__class__.worldMatrix[self.xRounded])):
        #     if self.__class__.worldMatrix[trunc(self.x)][floor(self.hitbox.lowBorder)] != "air":
        #         self.velocityY = 0
        #     else:
        #         self.velocityY = (self.velocityY - 0.02) * 0.98
        # else:
        #     self.velocityY = (self.velocityY - 0.02) * 0.98

        # self.velocityX = self.velocityX * 0.546 + self.accelerationX

        # self.x += self.velocityX * calibrationFPS
        # self.y += self.velocityY * calibrationFPS

class PlayerClass(EntityClass):
    def __init__(self):
        super().__init__()
        self.hitbox = Hitboxes(0.6, 1.8)
        self.x, self.y = float(2.5), float(5)
        

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
        if events.tpPlayer == True:
            self.y = 0
            self.x = 0

    def draw(self, surface, zoom, windowSize):
        self.windowSizeX, self.windowSizeY = windowSize
        self.xOnScreen = self.windowSizeX // 2
        self.yOnScreen = self.windowSizeY // 2
        pygame.draw.circle(surface, Color("red"), (self.xOnScreen, self.yOnScreen), 10)

    def getPlayerCoordinates(self):
        return (self.x, self.y)