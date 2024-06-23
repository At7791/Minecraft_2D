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
from math import ceil
import os

class Display():
    def __init__(self, texturePackFileName, blocksID, entities, zoom):    
        pygame.init()
        pygame.display.set_caption("Minecraft 2D")
        self.texturePackFileName = texturePackFileName
        self.windowSizeX = Tk().winfo_screenwidth()
        self.windowSizeY = Tk().winfo_screenheight() - 200
        self.backgroundColor = "#b3eeff"
        self.Screen = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))
        self.font = pygame.font.SysFont("Minecraft Regular", 30)
        
        self.entities = entities
        self.player = entities["player"][0]

        self.renderDistanceX = 8
        self.renderDistanceY = 8

        self.F3DebugScreenActive = True

        self.zoom = zoom
        self.blocksID = blocksID

        self.blockImages = {}
        for i in self.blocksID.keys():
            if i != "air":
                self.path = f'{self.texturePackFileName}/assets/minecraft/textures/block/{self.blocksID.get(i)[0]}.png'
                self.image = pygame.image.load(self.path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.zoom + 1, self.zoom + 1))
                self.blockImages[i] = self.image

        self.entitySprites = {}
        for i in self.entities.keys():
            self.spritePath = f"entity_sprites/{i}"
            lst = os.listdir(self.spritePath) # your directory path
            number_files = len(lst)
            self.sprites = []
            for j in range(number_files):
                for k in range(2):
                    if k == 0: 
                        self.sprite = pygame.image.load(f"{self.spritePath}/0{j + 1}.png").convert_alpha()
                        self.sprite = pygame.transform.scale(self.sprite, (self.zoom * 2, self.zoom * 2))
                    else:
                        self.sprite = pygame.image.load(f"{self.spritePath}/0{j + 1}.png").convert_alpha()
                        self.sprite = pygame.transform.scale(self.sprite, (self.zoom * 2, self.zoom * 2))
                        self.sprite = pygame.transform.flip(self.sprite, True, False)
                    self.sprites.append(self.sprite)
            self.entitySprites[i] = self.sprites
        print(self.entitySprites)
    
    def getFilePathFromDictionary(self, IDofCurrentBlock):
        self.path = f'{self.texturePackFileName}/assets/minecraft/textures/block/{self.blocksID.get(IDofCurrentBlock)[0]}.png'
        return self.path 

    def XYonScreen(self, x, y):
        self.XonScreen = - self.player.getPlayerCoordinates()[0] * self.zoom + self.windowSizeX // 2 + self.zoom * x
        # self.YonScreen = self.player.getPlayerCoordinates()[1] * self.zoom + self.windowSizeY // 2 - self.zoom * y
        self.YonScreen = self.player.getPlayerCoordinates()[1] * self.zoom + self.windowSizeY // 2 - self.zoom * (y - 1.6)
        return self.XonScreen, self.YonScreen

    def displayMain(self, displayedWorld, entities):
        self.Screen.fill(Color(self.backgroundColor))
        for chunk in displayedWorld:
            blockX = chunk[1]
            # if x > round(self.player.x - self.renderDistance)  and x < round(self.player.x + self.renderDistance):
            for blockY in range(len(chunk[0])):
                if chunk[0][blockY] != "air":
                    self.Screen.blit(self.blockImages[chunk[0][blockY]], (self.XYonScreen(blockX, blockY + 1), (self.zoom, self.zoom)))
                    # pygame.draw.rect(self.Screen, Color(randint(1,255), randint(1,255), randint(1,255)), (self.XYonScreen(x, y + 1), (self.zoom, self.zoom)))
                pygame.draw.line(self.Screen, Color("black"), self.XYonScreen(blockX, blockY), self.XYonScreen(blockX, blockY + 1))
                pygame.draw.line(self.Screen, Color("black"), self.XYonScreen(blockX, blockY), self.XYonScreen(blockX + 1, blockY))

        # Display entities !
        for entityType in entities.keys():
            for entity in entities[entityType]:
                if entity.facingPositive:
                    self.displayedSprite = self.entitySprites[entityType][0]

                else:
                    self.displayedSprite = self.entitySprites[entityType][1]
                pygame.draw.rect(self.Screen, Color("green"), (self.XYonScreen(entity.hitbox.leftBorder, entity.hitbox.highBorder), (self.zoom * entity.hitbox.lengthX, self.zoom * entity.hitbox.lengthY)), 10)
                self.Screen.blit(self.displayedSprite, (self.XYonScreen(entity.hitbox.x - ceil(entity.hitbox.lengthX), entity.hitbox.y + ceil(entity.hitbox.lengthY))))

        # debug displayed onjects
        pygame.draw.circle(self.Screen, Color("pink"), (self.XYonScreen(0, 2)), 10)

        # pygame.draw.circle(self.Screen, Color("yellow"), (self.XYonScreen(self.player.x, self.player.y)), self.zoom // 6)
        # pygame.draw.circle(self.Screen, Color("red"), (self.windowSizeX // 2, self.windowSizeY // 2), 5)
    
    def displayOverlay(self, events):
        # Minecraft F3 Debug Screen
        if events.f3KeyPressed:
            self.F3DebugScreenActive = not self.F3DebugScreenActive
        
        if self.F3DebugScreenActive:
            displayedString = f"X: {float(self.player.x):9.3f}    Y: {float(self.player.y):9.3f}    Facing positive: {self.player.facingPositive}"
            textColor = "#000000"
            self.Screen.blit(self.font.render(displayedString, False, textColor), (10, 10))