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

blocksID = {"air": ["air"], "stone": ["stone"], "dirt": ["dirt"], "grass_block": ["grass_block_side"], "bedrock": ["bedrock"]}

sizeX, sizeY = 3, 7
worldMatrixGLOBAL = world_generator(sizeX, sizeY, blocksID)
worldLoadDistance = 10
worldMatrix = world_loader(worldMatrixGLOBAL, worldLoadDistance, 0)


running = True

clock = pygame.time.Clock()
player = PlayerClass()
dis = Display("Faithful64x", blocksID, player)
events = Events()
EntityClass.worldMatrix = worldMatrix


TPS = 20
FPS = 60

durationTick = 1 / TPS
durationFrame = 1 / FPS
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
        events.eventsMain()
        accumulatorTicks -= durationTick
        numberOfTicks += 1

    # Frames and Physics Loop (as many times per second as there are Frames per second)
    while accumulatorFrames >= durationFrame:
        deltaTime = accumulatorFrames

        EntityClass.worldMatrix = worldMatrix
        EntityClass.worldLoadDistance = worldLoadDistance
        player.updatesPhysics(events, deltaTime * TPS)
        dis.displayMain(worldMatrix)
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