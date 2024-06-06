import sys
from tkinter import *
import pygame
from pygame import *
import pygame.draw
import pygame.image
import pygame.surface
import pygame.transform
import entity_code
from random import randint
from math import trunc

class Display():
    def __init__(self, texturePackFileName, blocksID, player):
        pygame.init()
        pygame.display.set_caption("Minecraft 2D")
        self.texturePackFileName = texturePackFileName
        self.windowSizeY = Tk().winfo_screenheight()
        self.windowSizeX = Tk().winfo_screenwidth()
        self.backgroundColor = "#b3eeff"
        self.Screen = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))
        self.player = player
        self.renderDistanceX = 8
        self.renderDistanceY = 8

        self.zoom = 90
        self.blocksID = blocksID

        self.blockImages = {}
        for i in self.blocksID.keys():
            if i != "air":
                self.path = f'{self.texturePackFileName}/assets/minecraft/textures/block/{self.blocksID.get(i)[0]}.png'
                self.image = pygame.image.load(self.path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.zoom, self.zoom))
                self.blockImages[i] = self.image

    
    def getFilePathFromDictionary(self, IDofCurrentBlock):
        self.path = f'{self.texturePackFileName}/assets/minecraft/textures/block/{self.blocksID.get(IDofCurrentBlock)[0]}.png'
        return self.path 

    def XYonScreen(self, x, y):
        self.XonScreen = - self.player.getPlayerCoordinates()[0] * self.zoom + self.windowSizeX // 2 + self.zoom * x
        # self.YonScreen = self.player.getPlayerCoordinates()[1] * self.zoom + self.windowSizeY // 2 - self.zoom * y
        self.YonScreen = self.player.getPlayerCoordinates()[1] * self.zoom + self.windowSizeY // 2 - self.zoom * (y - 1.6)
        return self.XonScreen, self.YonScreen

    def displayMain(self, displayedWorld):
        self.Screen.fill(Color(self.backgroundColor))
        for chunk in displayedWorld:
            blockX = chunk[1]
            # if x > round(self.player.x - self.renderDistance)  and x < round(self.player.x + self.renderDistance):
            for blockY in range(len(chunk[0])):
                blockY
                if chunk[0][blockX][blockY] != "air":
                    self.Screen.blit(self.blockImages[chunk[0][blockX][blockY]], (self.XYonScreen(blockX, blockY + 1), (self.zoom, self.zoom)))
                    # pygame.draw.rect(self.Screen, Color(randint(1,255), randint(1,255), randint(1,255)), (self.XYonScreen(x, y + 1), (self.zoom, self.zoom)))
        

        # debug displayed onjects
        pygame.draw.rect(self.Screen, Color("green"), (self.XYonScreen(self.player.hitbox.leftBorder, self.player.hitbox.highBorder), (self.zoom * self.player.hitbox.lengthX, self.zoom * self.player.hitbox.lengthY)), 10)
        pygame.draw.circle(self.Screen, Color("pink"), (self.XYonScreen(0, 2)), 10)

        pygame.draw.circle(self.Screen, Color("yellow"), (self.XYonScreen(self.player.x, self.player.y)), self.zoom // 6)
        pygame.draw.circle(self.Screen, Color("red"), (self.windowSizeX // 2, self.windowSizeY // 2), 5)

        pygame.display.update()