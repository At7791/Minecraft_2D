import pygame
from pygame import *
import sys
from display import Display
from random import *
from world_generator import world_generator
from entity_code import EntityClass
from player_code import PlayerClass
from event_controler import Events 
import time

blocksID = {"air": ["air"], "stone": ["stone"], "dirt": ["dirt"], "grass_block": ["grass_block_side"], "bedrock": ["bedrock"]}

sizeX, sizeY = 3, 7
worldMatrix = world_generator(sizeX, sizeY, blocksID)
running = True

clock = pygame.time.Clock()
player = PlayerClass()
dis = Display("Faithful64x", blocksID, player)
events = Events()   
EntityClass.worldMatrix = worldMatrix

TPS = 20
FPS = 20

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

    while accumulatorTicks >= durationTick:
        events.eventsMain()
        accumulatorTicks -= durationTick
        numberOfTicks += 1

    while accumulatorFrames >= durationFrame:
        deltaTime = accumulatorFrames
        player.updatesPhysics(events, deltaTime * TPS)
        dis.displayMain(worldMatrix, player)
        accumulatorFrames -= durationFrame
        numberOfFrames += 1

    if time.time() - preivousSecond >= 1:
        print(numberOfFrames, numberOfTicks, count)
        numberOfFrames = 0
        numberOfTicks = 0
        count = 0
        preivousSecond = time.time()
    time.sleep(0.001)
quit()