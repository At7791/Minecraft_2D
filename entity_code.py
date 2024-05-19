import pygame, math
from pygame import *
from math import trunc

class Hitboxes():
    def __init__(self, lengthX, lengthY):
        self.lengthX, self.lengthY = lengthX, lengthY
        self.offsetWithX = self.lengthX / 2

        self.highBorder = 0
        self.lowBorder = 0
        self.leftBorder = 0
        self.rightBorder = 0

        self.blocksOverlapped = []

    def update(self, x, y, worldMatrix):
        self.highBorder = y + self.lengthY
        self.lowBorder = y
        self.leftBorder = x - self.offsetWithX
        self.rightBorder = x + self.offsetWithX

        self.thighBorder = trunc(self.highBorder)
        self.tlowBorder = trunc(self.lowBorder)
        self.tleftBorder = trunc(self.leftBorder)
        self.trightBorder = trunc(self.rightBorder)

        self.blocksOverlapped = []
        for i in range(self.tleftBorder, self.trightBorder + 1):
            intermediateArray = []
            for j in range(self.tlowBorder, self.thighBorder + 1):
                intermediateArray.append((i, j))
            self.blocksOverlapped.append(intermediateArray)
        # print(y, self.blocksOverlapped)

class EntityClass():
    worldMatrix = []

    def __init__(self):
        self.x, self.y = float(0), float(0)
        self.xRounded, self.yRounded = round(self.x), round(self.y)
        self.velocityX, self.velocityY = float(0), float(-0.0000001)
        self.accelerationX, self.accelerationY = float(0), float(0)
        self.onGround = True
        self.xOnScreen = 0
        self.yOnScreen = 0
        self.hitbox = None
    
    def updatesPhysics(self, calibrationFPS):
        # movement and collision related entity updates
        self.tx, self.ty = trunc(self.x), trunc(self.y)
        self.hitbox.update(self.x, self.y, self.__class__.worldMatrix)
        
        # if trunc(self.y) in range(len(self.__class__.worldMatrix[0])): # test if entity is inside the map
        #     if self.y == trunc(self.y) and self.__class__.worldMatrix[trunc(self.x)][trunc(self.y) - 1] != "air":
        #         self.onGround == True
        #     else: self.onGround == False
        # else: self.onGround == False

        self.nextVelocityX = self.velocityX * 0.546 + self.accelerationX
        self.nextVelocityY = (self.velocityY - 0.02) * 0.98
        self.nextX = self.x + (self.nextVelocityX * calibrationFPS)
        self.nextY = self.y + (self.nextVelocityY * calibrationFPS)

        # tous les blocks de hitbox hors de la map
        # au moins un block de hitbox dans la map


        for i in range(len(self.hitbox.blocksOverlapped)):
            for j in self.hitbox.blocksOverlapped[i]:
                if j[0] in range(len(self.__class__.worldMatrix)) and j[1] in range(len(self.__class__.worldMatrix[0])):
        #                 if self.velocityX < 0:
        #                 elif self.velocityX > 0:
        #                 else:

                    if self.velocityY <= 0:
                        if j[1] == self.ty:
                            if self.__class__.worldMatrix[j[0]][j[1] - 1] != "air":
                                # print("hello")
                                if trunc(self.nextY) < self.ty:
                                    self.velocityY = 0
                                    self.y = self.ty
                                    print(self.ty, self.y)
                            else:
                                self.y = self.nextY
                                self.velocityY = self.nextVelocityY
                else:
                    self.y = self.nextY
                    self.velocityY = self.nextVelocityY

        self.velocityX = self.nextVelocityX
        # self.velocityY = self.nextVelocityY
        # self.y = self.nextY
        self.x = self.nextX
        #                 elif self.velocityY > 0:
        #                 else:

            # un ou deux coin croise la bordure d'un block avec le prochain step
                # snap le y du joueur avec le haut du block
                # self.onGround = True
            # deux coins ne croise pas la bordure d'un block avec le prochain step
                # calcul classic pour la hauteur
        
        # if self.onGround == False:
        #     self.velocityY = (self.velocityY - 0.02) * 0.98
        # else:
        #     self.velocityY = 0

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
        self.x, self.y = float(2.5), float(8)
        

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