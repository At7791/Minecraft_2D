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

class Display():
    def __init__(self, texturePackFileName, blocksID, player):
        pygame.init()
        pygame.display.set_caption("Minecraft 2D")
        self.texturePackFileName = texturePackFileName
        self.windowSizeY = Tk().winfo_screenheight() - 300
        self.windowSizeX = Tk().winfo_screenwidth()
        self.backgroundColor = "#b3eeff"
        self.Screen = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))
        self.player = player

        self.zoom = 60
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

    def displayMain(self, displayedWorld, player):

        self.Screen.fill(Color(self.backgroundColor))
        for x in range(len(displayedWorld)):
            for y in range(len(displayedWorld[x])):
                if displayedWorld[x][y] != "air":
                    self.Screen.blit(self.blockImages[displayedWorld[x][y]], (self.XYonScreen(x, y + 1), (self.zoom, self.zoom)))
                # pygame.draw.rect(self.Screen, Color(randint(1,255), randint(1,255), randint(1,255)), (self.XYonScreen(x, y), (self.zoom, self.zoom)))
        

        # debug displayed onjects
        pygame.draw.rect(self.Screen, Color("green"), (self.XYonScreen(self.player.hitbox.leftBorder, self.player.hitbox.highBorder), (self.zoom * self.player.hitbox.lengthX, self.zoom * self.player.hitbox.lengthY)))
        pygame.draw.circle(self.Screen, Color("pink"), (self.XYonScreen(2, 2)), 10)

        pygame.draw.circle(self.Screen, Color("yellow"), (self.XYonScreen(self.player.x, self.player.y)), self.zoom // 6)
        pygame.draw.circle(self.Screen, Color("red"), (self.windowSizeX // 2, self.windowSizeY // 2), 5)

        pygame.display.update()