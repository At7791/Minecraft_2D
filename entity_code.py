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
                    if self.__class__.worldMatrix[block[0]][block[1] - 1] != "air":
                        self.lowAir = False
                    if self.nextY <= block[1]:
                        self.lowBlockBorder = True
        if self.nextVelocityY >= 0:
            for block in self.hitbox.highBlocks():
                if self.isBlockInWorld(block[0], block[1] + 1):
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

        if self.velocityX <= 0:
            for block in self.hitbox.leftBlocks():
                if self.isBlockInWorld(block[0] - 1, block[1] + 1):
                    if self.__class__.worldMatrix[block[0] - 1][block[1]] != "air":
                        self.leftAir = False
                    if self.nextX - self.hitbox.offsetWithX <= block[0]:  
                        self.leftBlockBorder = True
        if self.velocityX >= 0:
            for block in self.hitbox.rightBlocks():
                print(block)
                if self.isBlockInWorld(block[0] + 1, block[1] + 1):
                
                    if self.__class__.worldMatrix[block[0] + 1][block[1]] != "air":
                        self.rightAir = False
                    if self.nextX + self.hitbox.offsetWithX >= block[0] + 1:  
                        self.rightBlockBorder = True


        
        if self.rightAir and self.leftAir:
            self.x = self.nextX
            self.velocityX = self.nextVelocityX
        else:
            if self.rightBlockBorder:
                self.velocityX = 0
                self.x = trunc(self.hitbox.rightBorder) - self.hitbox.offsetWithX - 0.000001 + 1
            elif self.leftBlockBorder:
                self.velocityX = 0
                self.x = trunc(self.hitbox.leftBorder) + self.hitbox.offsetWithX
            else:
                self.x = self.nextX
                self.velocityX = self.nextVelocityX
