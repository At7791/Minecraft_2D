from entity_code import EntityClass
from hitbox_code import Hitboxes
from pygame import *
import pygame

class PlayerClass(EntityClass):
    def __init__(self):
        self.type = "player"
        super().__init__(self.type)
        self.hitbox = Hitboxes(0.6, 1.8)
        self.x, self.y = float(30), float(4.5)
        self.count = 0
        self.isSprinting = False
        self.isCrouching = False

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
            self.velocityY = 0.53

        # Makes the player sprint, crouch or walk normally
        if events.crouchKeyPressed == True:
            self.accelerationX *= 0.3
            self.hitbox.update(self.x, self.y)
            self.isSprinting = False
            self.isCrouching = True
        elif events.sprintKeyPressed == True:
            self.accelerationX *= 1.3
            if self.velocityX != 0:
                self.isSprinting = True
            self.isCrouching = False
        else:
            self.isSprinting = False
            self.isCrouching = False
        
        # if events.clicking == True:
        
        # Debug keys
        if events.debugTrigger1 == True:
            self.y = 10
            self.x = 7.5
            self.count = 0
        
        
        # if self.velocityY < -3.91990:
        #     print(self.count, self.velocityY)
        # else:
        #     print(self.velocityY)

    def getPlayerCoordinates(self):
        return (self.x, self.y)