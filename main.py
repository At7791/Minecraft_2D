import pygame
from pygame import *
import sys
from display import Display
from random import *
from world_generator import world_generator
from world_generator import rendering
from entity_code import EntityClass
from player_code import PlayerClass
from event_controler import Events 
from world_loader import world_loader
import time
from xyCoordinateConverter import Converter
import json

# Block data gets loaded
blocksID = {}
file = open("block_data/blocksIDs.json", "r")
blocksID = json.load(file)
file.close()

# World setup and generation
sizeX, sizeY = 200, 50
StartWorld = 1500
HeightBedrockLeft1 = 2
HeightStoneLeft1 = 20
HeightDirtLeft1 = 30
worldMatrixGLOBAL, HeightBedrockRight1, HeightStoneRight1, HeightDirtRight1 = world_generator(sizeX, sizeY, StartWorld, blocksID, HeightBedrockLeft1, HeightStoneLeft1, HeightDirtLeft1)
worldLoadDistance = 30
RenderDistance = worldLoadDistance + 5
worldMatrix = world_loader(worldMatrixGLOBAL, worldLoadDistance, 0)

# Class initialisations
entities = {"player": []}
player = PlayerClass(StartWorld, sizeX)
entities["player"].append(player)
EntityClass.worldMatrix = worldMatrix

zoom = 90
dis = Display("minecraft_regular_versionfile", "MinecraftRegular.ttf", blocksID, entities, zoom)

events = Events()
convert = Converter(worldLoadDistance, player.getPlayerCoordinates()[0])

# Variables used in the time management
TPS = 20
FPS = 60

durationTick = 1 / TPS
durationFrame = 1 / FPS

ticks = 0

measuredFPS = 0
measuredTPS = 0
waitLoops = 0

currentTime = time.time()
previousTickTime = currentTime
previousFrameTime = currentTime

numberOfFrames = 0
numberOfTicks = 0
preivousSecond = currentTime

accumulatorTicks = 0
elapsedTimeTicks = 0

accumulatorFrames = 0
elapsedTimeFrames = 0

count = 0

running = True

while running:
    # Time calculations
    count += 1
    currentTime = time.time()

    elapsedTimeTicks = currentTime - previousTickTime
    elapsedTimeFrames = currentTime - previousFrameTime

    previousFrameTime = currentTime
    previousTickTime = currentTime
    
    accumulatorTicks += elapsedTimeTicks
    accumulatorFrames += elapsedTimeFrames


    # Game Tick Loop (20 times per second)
    while accumulatorTicks >= durationTick:
        # world loading into the worldMatrix variable
        worldMatrix = world_loader(worldMatrixGLOBAL, worldLoadDistance, player.x)

        convert = Converter(worldLoadDistance, player.getPlayerCoordinates()[0])

        # Breaking blocks as the player
        if player.XYblockTargeting != None:
            targetedBlockNatrue = worldMatrix[convert.XWMGToLoadedWM(player.XYblockTargeting[0])][0][player.XYblockTargeting[1]]
            if targetedBlockNatrue != "air":
                player.blockInteractions(blocksID[targetedBlockNatrue][1])
            else:
                player.breakTimer = None
            if player.breakBlock == True:
                worldMatrix[convert.XWMGToLoadedWM(player.XYblockTargeting[0])][0][player.XYblockTargeting[1]] = "air"
        else:
            player.breakTimer = None


        # Executes code on every entity in the loaded world
        for entityType in entities.keys():
            for entity in entities[entityType]:
                entity.updateCycle()

                if entityType != "player":
                    entity.updatesPhysics(deltaTime * TPS, convert)

        accumulatorTicks -= durationTick
        numberOfTicks += 1
        ticks += 1


    # Frames and Player physics Loop (as many times per second as there are FPS)
    while accumulatorFrames >= durationFrame:
        deltaTime = accumulatorFrames

        # world generation updates
        events.eventsMain()
        worldMatrixGLOBAL.append(rendering(player.x, RenderDistance, worldMatrixGLOBAL, sizeY, HeightBedrockLeft1, HeightStoneLeft1, HeightDirtLeft1, HeightBedrockRight1, HeightStoneRight1, HeightDirtRight1))
        var1, HeightBedrockLeft1, HeightStoneLeft1, HeightDirtLeft1, HeightBedrockRight1, HeightStoneRight1, HeightDirtRight1 = rendering(player.x, RenderDistance, worldMatrixGLOBAL, sizeY, HeightBedrockLeft1, HeightStoneLeft1, HeightDirtLeft1, HeightBedrockRight1, HeightStoneRight1, HeightDirtRight1)
        
        # Player and Entity Class updates
        EntityClass.worldMatrix = worldMatrix
        EntityClass.worldLoadDistance = worldLoadDistance
        player.updatesPhysics(events, deltaTime * TPS, convert)
        if player.XYblockTargeting != None:
            player.XYblockTargeting = dis.XYinWorld(player.XYblockTargeting[0], player.XYblockTargeting[1], True)

        # Display Updates
        dis.displayMain(worldMatrix, entities)
        dis.displayOverlay(events, measuredFPS, measuredTPS, waitLoops)
        pygame.display.update()

        accumulatorFrames -= durationFrame
        numberOfFrames += 1


    # Displays the number of measured FPS and TPS (DEBUG)
    if time.time() - preivousSecond >= 1:
        measuredFPS = numberOfFrames
        measuredTPS = numberOfTicks
        waitLoops = count
        numberOfFrames = 0
        numberOfTicks = 0
        count = 0
        preivousSecond = time.time()
    time.sleep(0.001)
quit()