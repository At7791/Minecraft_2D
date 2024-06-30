import sys
from tkinter import *
import pygame
from pygame import *
import pygame.draw
import pygame.font
import pygame.image
import pygame.surface
import pygame.transform
import entity_code
from random import randint
from math import ceil, trunc
import os

class Display():
    def __init__(self, texturePackFileName, fontFile, blocksID, entities, zoom):    
        pygame.init()
        pygame.display.set_caption("Minecraft 2D")
        self.texturePackFileName = texturePackFileName
        self.windowSizeX = Tk().winfo_screenwidth()
        self.windowSizeY = Tk().winfo_screenheight() - 300
        self.backgroundColor = "#b3eeff"
        self.Screen = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))
        self.font = pygame.font.Font(f"fonts\minecraft-font\{fontFile}", 26)
        
        self.entities = entities
        self.player = self.entities["player"][0]

        self.renderDistanceX = 8
        self.renderDistanceY = 8

        self.F3DebugScreenActive = True

        self.zoom = zoom
        self.blocksID = blocksID
        self.spriteNumber = 0
        self.blockOutlineThickness = 2

        # generages the dictionary containing every block texture corresponding to the block ID
        self.blockImages = {}
        for i in self.blocksID.keys():
            if i != "air":
                self.path = f'textures/{self.texturePackFileName}/assets/minecraft/textures/block/{self.blocksID.get(i)[0]}.png'
                self.image = pygame.image.load(self.path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.zoom + 1, self.zoom + 1))
                self.blockImages[i] = self.image
        
        # generates the dictionary containing every sprite corresponding to the entity type
        self.entitySprites = {}
        for i in self.entities.keys():
            self.spritePath = f"entity_sprites/{i}"
            lst = os.listdir(self.spritePath)
            number_files = len(lst)     # how many files are there in the directory
            self.sprites = []
            for j in range(number_files):
                intermediateArray = []
                # generates a mirrored sprite in addition to the normal sprite
                for k in range(2):
                    if k == 0: 
                        self.sprite = pygame.image.load(f"{self.spritePath}/0{j + 1}.png").convert_alpha()
                        self.sprite = pygame.transform.scale(self.sprite, (self.zoom * 2, self.zoom * 2))
                    else:
                        self.sprite = pygame.image.load(f"{self.spritePath}/0{j + 1}.png").convert_alpha()
                        self.sprite = pygame.transform.scale(self.sprite, (self.zoom * 2, self.zoom * 2))
                        self.sprite = pygame.transform.flip(self.sprite, True, False)
                    intermediateArray.append(self.sprite)
                self.sprites.append(intermediateArray)
            self.entitySprites[i] = self.sprites
        
        # generates the list containing every block break animation image
        self.breakFrames = []
        for i in range(10):
            self.path = f"textures/{self.texturePackFileName}/assets/minecraft/textures/block/destroy_stage_{i}.png"
            self.image = pygame.image.load(self.path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.zoom + 1, self.zoom + 1))
            self.breakFrames.append(self.image)

    # generates the file path with the block ID
    def getFilePathFromDictionary(self, IDofCurrentBlock):
        self.path = f'textures/{self.texturePackFileName}/assets/minecraft/textures/block/{self.blocksID.get(IDofCurrentBlock)[0]}.png'
        return self.path 
    
    # Converts the minecraft coordinates into coordinates on Screen
    def XYonScreen(self, x, y):
        self.XonScreen = - self.player.getPlayerCoordinates()[0] * self.zoom + self.windowSizeX // 2 + self.zoom * x
        self.YonScreen = self.player.getPlayerCoordinates()[1] * self.zoom + self.windowSizeY // 2 - self.zoom * (y - 1.6)
        return self.XonScreen, self.YonScreen
    
    # Converts the coordinates on screen into coordinates in Minecraft
    def XYinWorld(self, x, y, resultTruncated):
        self.XinWorld = x / self.zoom + self.player.getPlayerCoordinates()[0] - self.windowSizeX / 2 / self.zoom
        self.YinWorld = - y / self.zoom + self.player.getPlayerCoordinates()[1] + self.windowSizeY / 2 / self.zoom + 1.6
        if resultTruncated == True:
            self.XinWorld, self.YinWorld = trunc(self.XinWorld), trunc(self.YinWorld)
        return self.XinWorld, self.YinWorld

    def displayMain(self, displayedWorld, entities):
        # Display background !
        self.Screen.fill(Color(self.backgroundColor))

        # Display Blocks !
        self.blockBreaking = None
        for chunk in displayedWorld:
            if chunk != [] and chunk[0] != None:
                blockX = chunk[1]
                for blockY in range(len(chunk[0])):
                    if chunk[0][blockY] != "air":
                        self.Screen.blit(self.blockImages[chunk[0][blockY]], (self.XYonScreen(blockX, blockY + 1), (self.zoom, self.zoom)))
                        if self.player.XYblockTargeting != None:
                            if self.player.XYblockTargeting == (blockX, blockY):
                                self.blockBreaking = (blockX, blockY)
                                pygame.draw.rect(self.Screen, Color("#000000"), (self.XYonScreen(self.player.XYblockTargeting[0], self.player.XYblockTargeting[1] + 1), (self.zoom, self.zoom)), self.blockOutlineThickness)

                    # Uncomment to see black outlines around blockborders
                    # pygame.draw.line(self.Screen, Color("black"), self.XYonScreen(blockX, blockY), self.XYonScreen(blockX, blockY + 1))
                    # pygame.draw.line(self.Screen, Color("black"), self.XYonScreen(blockX, blockY), self.XYonScreen(blockX + 1, blockY))

        if self.blockBreaking != None and self.player.breakTimer != None:
            self.Screen.blit(self.breakFrames[self.player.breakProgress - 1], (self.XYonScreen(self.blockBreaking[0], self.blockBreaking[1] + 1), (self.zoom, self.zoom)))

        # Display entities !
        for entityType in entities.keys():
            for entity in entities[entityType]:
                self.spriteNumber = 0

                if entity.velocityX != 0:
                    if entity.cycle in range(5, 10) or entity.cycle in range(15, 20):
                        self.spriteNumber = 0
                    elif entity.cycle in range(0, 5):
                        self.spriteNumber = 1
                    elif entity.cycle in range(10, 15):
                        self.spriteNumber = 2
                if entityType == "player":
                    if entity.isCrouching == True:
                        self.spriteNumber = 3

                if entity.facingPositive:
                    self.displayedSprite = self.entitySprites[entityType][self.spriteNumber][0]
                else:
                    self.displayedSprite = self.entitySprites[entityType][self.spriteNumber][1]
                
                self.Screen.blit(self.displayedSprite, (self.XYonScreen(entity.hitbox.x - ceil(entity.hitbox.lengthX), entity.hitbox.y + ceil(entity.hitbox.lengthY) - 0.0001)))
                # pygame.draw.rect(self.Screen, Color("green"), (self.XYonScreen(entity.hitbox.leftBorder, entity.hitbox.highBorder), (self.zoom * entity.hitbox.lengthX, self.zoom * entity.hitbox.lengthY)), 10)

    def displayOverlay(self, events, measuredFPS, measuredTPS, waitLoops):
        # ability to zoom in or out


        # Minecraft F3 Debug Screen
        if events.f3KeyPressed:
            self.F3DebugScreenActive = not self.F3DebugScreenActive
        
        
        if self.F3DebugScreenActive:
            textColor = "#000000"

            displayedStringLine1 = f"Facing positive: {self.player.facingPositive}     X: {float(self.player.x):9.3f}    Y: {float(self.player.y):9.3f}"
            displayedStringLine2 = f"Mouse: X: {float(self.XYinWorld(events.mouseX, events.mouseY, False)[0]):9.3f},  Y: {float(self.XYinWorld(events.mouseX, events.mouseY, False)[1]):9.3f}"
            displayedStringLine3 = f"FPS: {measuredFPS}    TPS: {measuredTPS}    Wait Loop: {waitLoops}"
            if self.player.XYblockTargeting != None:
                displayedStringLine4 = f"Targeted Block: X: {self.player.XYblockTargeting[0]}   Y: {self.player.XYblockTargeting[1]}"
            else:
                displayedStringLine4 = f"Targeted Block: X: None   Y: None"
            displayedStringLine5 = f"breakTimer: {self.player.breakProgress}"

            self.Screen.blit(self.font.render(displayedStringLine1, False, textColor), (10, 5))
            self.Screen.blit(self.font.render(displayedStringLine2, False, textColor), (10, 35))
            self.Screen.blit(self.font.render(displayedStringLine3, False, textColor), (10, 65))
            self.Screen.blit(self.font.render(displayedStringLine4, False, textColor), (10, 95))
            self.Screen.blit(self.font.render(displayedStringLine5, False, textColor), (10, 125))
