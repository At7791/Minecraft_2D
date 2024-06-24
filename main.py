import pygame
from pygame import *
import sys
from display import Display
from random import *
from world_generator import world_generator
from entity_code import EntityClass
from player_code import PlayerClass
from event_controler import Events 
from world_loader import world_loader
import time
from xyCoordinateConverter import Converter

blocksID = {"air": ["air"], "stone": ["stone"], "dirt": ["dirt"], "grass_block": ["grass_block_side"], "bedrock": ["bedrock"]}

sizeX, sizeY = 3, 7
worldMatrixGLOBAL = world_generator(sizeX, sizeY, blocksID)
worldLoadDistance = 15
worldMatrix = world_loader(worldMatrixGLOBAL, worldLoadDistance, 0)
zoom = 90

running = True

entities = {"player": []}
player = PlayerClass()
entities["player"].append(player)
clock = pygame.time.Clock()
dis = Display("Faithful64x", blocksID, entities, zoom)
events = Events()
EntityClass.worldMatrix = worldMatrix
convert = Converter(worldLoadDistance, player.getPlayerCoordinates()[0])

TPS = 20
FPS = 60

durationTick = 1 / TPS
durationFrame = 1 / FPS

ticks = 0

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

while running:
    count += 1
    currentTime = time.time()

    elapsedTimeTicks = currentTime - previousTickTime
    elapsedTimeFrames = currentTime - previousFrameTime

    previousFrameTime = currentTime
    previousTickTime = currentTime
    
    accumulatorTicks += elapsedTimeTicks
    accumulatorFrames += elapsedTimeFrames


    # Event Tick Loop (20 times per second)
    while accumulatorTicks >= durationTick:
        worldMatrix = world_loader(worldMatrixGLOBAL, worldLoadDistance, player.x)
        convert = Converter(worldLoadDistance, player.getPlayerCoordinates()[0])
        events.eventsMain()

        # Executes code on every entity in the loaded world
        for entityType in entities.keys():
            for entity in entities[entityType]:
                entity.updateCycle()

        accumulatorTicks -= durationTick
        numberOfTicks += 1
        ticks += 1

    # Frames and Physics Loop (as many times per second as there are Frames per second)
    while accumulatorFrames >= durationFrame:
        deltaTime = accumulatorFrames

        EntityClass.worldMatrix = worldMatrix
        EntityClass.worldLoadDistance = worldLoadDistance
        player.updatesPhysics(events, deltaTime * TPS, convert, dis)
        dis.displayMain(worldMatrix, entities)
        dis.displayOverlay(events)
        pygame.display.update()

        accumulatorFrames -= durationFrame
        numberOfFrames += 1

    # Displays the number of measured FPS and TPS (DEBUG)
    if time.time() - preivousSecond >= 1:
        print(numberOfFrames, numberOfTicks, count)
        numberOfFrames = 0
        numberOfTicks = 0
        count = 0
        preivousSecond = time.time()
    time.sleep(0.001)

    
quit() 