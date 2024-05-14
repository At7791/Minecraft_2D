import sys
from tkinter import *
import pygame
from pygame import *
import pygame.draw
import pygame.image
import pygame.surface
import pygame.transform
import player_code

class Display():
    def __init__(self, texturePackFileName, blocksID):
        pygame.init()
        pygame.display.set_caption("Minecraft 2D")
        self.texturePackFileName = texturePackFileName
        self.windowSizeY = Tk().winfo_screenheight() - 200
        self.windowSizeX = Tk().winfo_screenwidth()
        self.backgroundColor = "#b3eeff"
        self.Screen = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))

        self.zoom = 60
        self.blocksID = blocksID

    def getBlockImage(self, IDofCurrentBlock):
        self.filePath = self.getFilePathFromDictionary(IDofCurrentBlock)
        self.image = pygame.image.load(self.filePath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.zoom, self.zoom))
        return self.image
    
    def getFilePathFromDictionary(self, IDofCurrentBlock):
        self.path = f'{self.texturePackFileName}/assets/minecraft/textures/block/{self.blocksID.get(IDofCurrentBlock)[0]}.png'
        return self.path 

    def displayMain(self, displayedWorld, player):
        self.Screen.fill(Color(self.backgroundColor))
        for x in range(len(displayedWorld)):
            for y in range(len(displayedWorld[x])):
                if displayedWorld[x][y] != 0:

                    self.xBlock = - player.getPlayerCoordinates()[0] * self.zoom + self.windowSizeX // 2 + self.zoom * x
                    self.yBlock = player.getPlayerCoordinates()[1] * self.zoom + self.windowSizeY // 2 - self.zoom * (y + 1)
                    self.Screen.blit(self.getBlockImage(displayedWorld[x][y]), (self.xBlock, self.yBlock, self.zoom, self.zoom))

        player.draw(self.Screen, self.zoom, (self.windowSizeX, self.windowSizeY))
                
        pygame.display.update()