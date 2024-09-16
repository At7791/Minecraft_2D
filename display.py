from tkinter import *
import pygame
from math import ceil, trunc
import os

class Display():
    def __init__(self, data, blocksID, entities, particles_data):    
        pygame.init()
        pygame.display.set_caption("Minecraft 2D")
        
        self.texturePackFileName = data["active_texture_pack"]
        self.textureFilePath = f'assets/ressources/textures/{self.texturePackFileName}/assets/minecraft/textures/'
        self.blockOutlineThickness = data["block_outline_thickness"]
        self.zoom = data["zoom"]
        self.backgroundColor = data["bg_color"]
        
        fontpath = data["font_path"]
        self.font = pygame.font.Font(f"fonts\minecraft-font\{fontpath}", data["font_size"])


        self.windowSizeX = Tk().winfo_screenwidth()
        self.windowSizeY = data["window_size_y"]

        self.Screen = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))
        
        self.entities = entities
        self.player = self.entities["player"][0]
        self.blocksID = blocksID

        self.F3DebugScreenActive = True
        self.spriteNumber = 0

        # generages the dictionary containing every block texture corresponding to the block ID
        self.blockImages = {}
        for i in self.blocksID.keys():
            if i != "air":
                self.path =  self.textureFilePath + f'block/{self.blocksID.get(i)[0]}.png'
                self.image = pygame.image.load(self.path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.zoom + 1, self.zoom + 1))
                self.blockImages[i] = self.image
        
        # generates the dictionary containing every sprite corresponding to the entity type
        self.entitySprites = {}
        for i in self.entities.keys():
            self.spritePath = f"assets/ressources/entity_sprites/{i}"
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
            self.path = self.textureFilePath + f"block/destroy_stage_{i}.png"
            self.image = pygame.image.load(self.path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.zoom + 1, self.zoom + 1))
            self.breakFrames.append(self.image)

        # generates the dictionary containing every particle texture
        paths = {}
        for particle_type in particles_data.keys():
            paths[particle_type] = []
            if particles_data[particle_type][1] > 1:
                for i in range(particles_data[particle_type][1]):
                    paths[particle_type].append(self.textureFilePath + f"particle/{particles_data[particle_type][0]}_{i}.png")
            elif particles_data[particle_type][1] == 1:
                paths[particle_type].append(self.textureFilePath + f"particle/{particles_data[particle_type][0]}.png")
            elif particles_data[particle_type][1] == 0:
                paths[particle_type].append(particles_data[particle_type][0])

        self.particle_textures = {}
        for particle_type in particles_data.keys():
            self.particle_textures[particle_type] = []
            for path in paths[particle_type]:
                if path == "block_particle":
                    pass
                else:
                    self.image = pygame.image.load(path).convert()
                    self.image = pygame.transform.scale(self.image, (particles_data[particle_type][2], particles_data[particle_type][2]))
                    self.image.fill(particles_data[particle_type][3], special_flags=pygame.BLEND_RGBA_MULT)
                    self.particle_textures[particle_type].append(self.image)

    def displayMain(self, displayedWorld, entities, particles, convert):
        # Display background !
        self.Screen.fill(self.backgroundColor)

        # Display Blocks !
        for chunkX in displayedWorld.keys():
            chunk = displayedWorld[chunkX]
            chunkWidth = len(chunk)
            sliceX = 0
            for slice in chunk:
                blockX = chunkX * chunkWidth + sliceX
                blockY = 0
                for block in slice:
                    if block != "air":
                        self.Screen.blit(self.blockImages[block], (convert.XYonScreen(blockX, blockY), (self.zoom, self.zoom)))
                    blockY += 1
                sliceX += 1

        # Display Breaking Overlay
        if self.player.breakTimer != None:
            self.Screen.blit(self.breakFrames[self.player.breakProgress], (convert.XYonScreen(self.player.blockTargetedX, self.player.blockTargetedY), (self.zoom, self.zoom)))

        # Display targeted Block Outline
        if self.player.minableTargeted:
            pygame.draw.rect(self.Screen, "#000000", (convert.XYonScreen(self.player.blockTargetedX, self.player.blockTargetedY), (self.zoom, self.zoom)), self.blockOutlineThickness)

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
                
                self.Screen.blit(self.displayedSprite, (convert.XYonScreen(entity.hitbox.x - ceil(entity.hitbox.lengthX), entity.hitbox.y + ceil(entity.hitbox.lengthY) - 0.0001)))
                # pygame.draw.rect(self.Screen, "#00ff00", (convert.XYonScreen(entity.hitbox.leftBorder, entity.hitbox.highBorder), (self.zoom * entity.hitbox.lengthX, self.zoom * entity.hitbox.lengthY)), 10)

        # Display Particles !
        for particle_type in particles.active_particles.keys():
            for particle in particles.active_particles[particle_type]:
                if particle_type == "block_particle":
                    self.Screen.blit(self.blockImages[particle.blockType], (convert.XYonScreen(particle.x, particle.y)), tuple(i * self.zoom for i in particle.positionOnBlockTexture)) # tuple(i * self.zoom for i in particle.positionOnBlockTexture)
                else:
                    self.Screen.blit(self.particle_textures[particle_type][particle.cycle_texture], (convert.XYonScreen(particle.x, particle.y)))

    def displayOverlay(self, events, measuredFPS, measuredTPS, waitLoops, convert):
        # Minecraft F3 Debug Screen
        if events.f3KeyPressed:
            self.F3DebugScreenActive = not self.F3DebugScreenActive
        
        
        if self.F3DebugScreenActive:
            textColor = "#000000"

            displayedStringLine1 = f"Facing positive: {self.player.facingPositive}     X: {float(self.player.x):9.3f}    Y: {float(self.player.y):9.3f}"
            displayedStringLine2 = f"Mouse: X: {float(convert.XYinWorld(self.player.blockTargetedX, self.player.blockTargetedY)[0]):9.3f},  Y: {float(convert.XYinWorld(events.mouseX, events.mouseY, False)[1]):9.3f}"
            displayedStringLine3 = f"FPS: {measuredFPS}    TPS: {measuredTPS}    Wait Loop: {waitLoops}"
            displayedStringLine4 = f"Targeted Block: {convert.blockNature((self.player.blockTargetedX, self.player.blockTargetedY))}"
            displayedStringLine5 = f"breakProgress: {self.player.breakProgress}"

            self.Screen.blit(self.font.render(displayedStringLine1, False, textColor), (10, 5))
            self.Screen.blit(self.font.render(displayedStringLine2, False, textColor), (10, 35))
            self.Screen.blit(self.font.render(displayedStringLine3, False, textColor), (10, 65))
            self.Screen.blit(self.font.render(displayedStringLine4, False, textColor), (10, 95))
            self.Screen.blit(self.font.render(displayedStringLine5, False, textColor), (10, 125))

    def displayUpdate(self):
        pygame.display.update()
    
    def close(self):
        pygame.quit()

    # generates the file path with the block ID
    def getFilePathFromDictionary(self, IDofCurrentBlock):
        self.path = f'textures/{self.texturePackFileName}/assets/minecraft/textures/block/{self.blocksID.get(IDofCurrentBlock)[0]}.png'
        return self.path
