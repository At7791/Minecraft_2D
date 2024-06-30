from entity_code import EntityClass
from hitbox_code import Hitboxes
from pygame import *
import pygame
from math import ceil

class PlayerClass(EntityClass):
    def __init__(self, StartWorld, sizeX):
        self.type = "player"
        super().__init__(self.type)
        self.hitbox = Hitboxes(0.6, 1.8)
        self.x, self.y = float((StartWorld + sizeX)/2), float(50)
        self.count = 0
        self.isSprinting = False
        self.isCrouching = False

        self.XYblockTargeting = None
        self.lastXYblockTargeting = self.XYblockTargeting
        self.breakTimer = None
        self.breakBlock = False
        self.breakProgress = 0

    # Updates the variable cycling used to display the player sprites
    def updateCycle(self):
        if self.velocityX != 0:
            if self.isSprinting == True:
                if self.cycle >= 20:
                    self.cycle = 0
                else:
                    self.cycle += 2
            else:
                if self.cycle >= 20:
                    self.cycle = 0
                else:
                    self.cycle += 1
        else:
            self.cycle = 0

    def blockMiningTime(self, blockHardness):
        if blockHardness == 0:
            return 0
        
        speedMultiplier = 1
        blockDamage = speedMultiplier / blockHardness
        blockDamage /= 30
        
        # print(blockDamage, ceil(1 / blockDamage))
        if blockDamage > 1:
            return 0
        
        return ceil(1 / blockDamage)

    def blockInteractions(self, blockHardness):
        if self.lastXYblockTargeting != self.XYblockTargeting:
            self.breakTimer = None
        self.lastXYblockTargeting = self.XYblockTargeting
        
        if self.breakTimer == None:
            self.numberOfTicks = self.blockMiningTime(blockHardness)
            self.breakTimer = 0
            self.breakProgress = 0
            self.breakBlock = False
            # print(self.numberOfTicks)

        if self.breakTimer >= self.numberOfTicks and self.numberOfTicks >= 0:
            self.breakTimer = None
            self.breakBlock = True
            self.breakProgress = 0
        else:
            self.breakTimer += 1
            if self.numberOfTicks > 0:
                self.breakProgress = ceil(10 * (self.breakTimer / self.numberOfTicks))
            else:
                self.breakProgress = 1

    def updatesPhysics(self, events, calibrationFPS, convert):
        super().updatesPhysics(calibrationFPS, convert)
        self.count += 1


        # applies the effect to the player movement of the key presses
        if events.forwardKeyPressed == True:
            self.accelerationX = 0.1
        elif events.backwardKeyPressed == True:
            self.accelerationX = -0.1
        else:
            self.accelerationX = 0
                
        if events.jumpKeyPressed == True and self.onGround == True:
            self.velocityY = 2

        # Makes the player sprint, crouch or walk normally
        if events.crouchKeyPressed == True:
            self.accelerationX *= 0.3
            self.hitbox.update(self.x, self.y)
            self.isSprinting = False
            self.isCrouching = True
        elif events.sprintKeyPressed == True:
            self.accelerationX *= 1.3 * 5
            if self.velocityX != 0:
                self.isSprinting = True
            self.isCrouching = False
        else:
            self.isSprinting = False
            self.isCrouching = False
        

        if events.clickingLeft == True:
            self.XYblockTargeting = (events.mouseX, events.mouseY)
        else:
            self.XYblockTargeting = None


        # Debug keys
        if events.debugTrigger1 == True:
            self.y = 10
            self.x = 7.5
            self.count = 0

    def getPlayerCoordinates(self):
        return (self.x, self.y)