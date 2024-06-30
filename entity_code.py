import pygame, math, hitbox_code
from pygame import *
from math import trunc, pow, ceil
from hitbox_code import Hitboxes
from random import randint


        
class EntityClass():
    worldMatrix = []        # Class Variable, contains the World Matrix
    gravity = - 0.08        # Class Variable, every entity has the same gravity
    worldLoadDistance = 0   # Class Variable, world load distance

    def __init__(self, type):
        self.type = type
        self.x, self.y = float(0), float(0)
        self.nextX, self.nextY = self.x, self.y
        self.velocityX, self.velocityY = float(0), float(-0.0000001)
        self.nextVelocityX, self.nextVelocityY = self.velocityX, self.velocityY
        self.accelerationX, self.accelerationY = float(0), float(0)
        self.onGround = True
        self.xOnScreen = 0
        self.yOnScreen = 0
        self.hitbox = None
        self.onGround = False
        self.facingPositive = True
        self.cycle = 0

    def isBlockInWorld(self, x = int, y = int): # Returns a boolean which is true or false if the given corrdinate is inside the worldmatrix or not
        if x >= 0 and y >= 0:
            if x in range(self.__class__.worldMatrix[0][1], self.__class__.worldMatrix[-1][1] + 1) and y in range(len(self.__class__.worldMatrix[0][0]) + 1):
                # if self.__class__.worldMatrix[x]
                return True
            else:
                return False
        return False
    
    def updateCycle(self): # Updates the variable cycling used to display the entity sprites
        if self.velocityX != 0:
            if self.cycle == 20:
                self.cycle = 0
            else:
                self.cycle += 1
        else:
            self.cycle = 0

    def updatesPhysics(self, calibrationFPS, convert):   # movement and collision related entity updates
        self.hitbox.update(self.x, self.y)

        # Calculates the next velocity that the entity will have on each axis
        self.nextVelocityX = (self.velocityX * 0.546 + self.accelerationX)
        if -0.0003 < self.nextVelocityX < 0.0003:
            self.nextVelocityX = 0
        
        
        self.nextVelocityY = (self.velocityY - (0.08 * calibrationFPS)) * pow(0.98, calibrationFPS)
        if abs(self.nextVelocityY) < 0.003:
            self.nextVelocityY = 0
        
        # Calculates the next position the entity will be on regardless of the collisions
        self.nextX = self.x + self.nextVelocityX * calibrationFPS
        self.nextY = self.y + self.nextVelocityY * calibrationFPS

        
        # Tests for collisions in the path of the entity
        # The Y axis
        self.lowAir = True
        self.highAir = True
        self.lowBlockBorder = False
        self.highBlockBorder = False
        self.onGround = False

        if self.nextVelocityY <= 0: # if the entity is going down
            i = 0
            for block in self.hitbox.lowBlocks():
                if self.isBlockInWorld(block[0] + 1, block[1] + 1):
                    if self.__class__.worldMatrix[trunc(convert.XWMGToLoadedWM(block[0]))][0][block[1] - 1] != "air":
                        self.lowAir = False         # is there an air block below the entity
                    if self.nextY <= block[1]:
                        self.lowBlockBorder = True  # will the entity cross the blockborder of the block below in the next iteration
                i += 1
        if self.nextVelocityY >= 0: # if the entity is going up
            i = 0
            for block in self.hitbox.highBlocks():
                if self.isBlockInWorld(block[0] + 1, block[1] + 1):
                    if self.__class__.worldMatrix[trunc(convert.XWMGToLoadedWM(block[0]))][0][block[1]] != "air":
                        self.highAir = False        # is there an air block above the entity
                    if self.nextY <= block[1]:  
                        self.highBlockBorder = True # will the entity cross the blockborder of the block above in the next iteration
                i += 1
        
        # applies or not the effect of a collision of the entity with a block on the Y axis
        if self.lowAir and self.highAir:
            self.y = self.nextY
            self.velocityY = self.nextVelocityY
        else:
            if self.lowBlockBorder:
                self.velocityY = 0
                self.y = trunc(self.y)
                self.onGround = True
            elif self.highBlockBorder:
                self.velocityY = 0
                self.y = trunc(self.hitbox.highBorder) - self.hitbox.lengthY
            else:
                self.y = self.nextY
                self.velocityY = self.nextVelocityY


        # The X axis
        self.rightAir = True
        self.leftAir = True
        self.leftBlockBorder = False
        self.rightBlockBorder = False

        if self.velocityX <= 0:
            i = 0
            for block in self.hitbox.leftBlocks():
                if self.isBlockInWorld(block[0] + 1, block[1] + 1): 
                    if self.__class__.worldMatrix[trunc(self.worldLoadDistance - 1.001 - self.hitbox.offsetWithX)][0][block[1]] != "air":
                        self.leftAir = False            # is there an air block to the left of the entity
                    if self.nextX - self.hitbox.offsetWithX <= block[0]:  
                        self.leftBlockBorder = True     # will the entity cross the blockborder of the block to the left in the next iteration
                i += 1
        if self.velocityX >= 0:
            i = 0
            for block in self.hitbox.rightBlocks():
                if self.isBlockInWorld(block[0] + 1, block[1] + 1):
                    if self.__class__.worldMatrix[trunc(self.worldLoadDistance + self.hitbox.offsetWithX)][0][block[1]] != "air":
                        self.rightAir = False           # is there an air block to the right of the entity
                    if self.nextX + self.hitbox.offsetWithX >= block[0] + 1:
                        self.rightBlockBorder = True    # will the entity cross the blockborder of the block to the right in the next iteration
                i += 1

        # applies or not the effect of a collision of the entity with a block on the X axis
        if self.rightAir and self.leftAir:
            self.x = self.nextX
            self.velocityX = self.nextVelocityX
            if self.velocityX < 0: # Defines the way that the entity faces
                self.facingPositive = False
            elif self.velocityX > 0:
                self.facingPositive = True
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
                if self.velocityX < 0: # Defines the way that the entity faces
                    self.facingPositive = False
                elif self.velocityX > 0:
                    self.facingPositive = True