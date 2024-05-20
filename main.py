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
FPS = 240
durationTick = 1 / TPS
durationFrame = 1 / FPS
previousTickTime = time.time()
previousFrameTime = time.time()

while running:
    currentTime = time.time()

    if currentTime - previousTickTime >= durationTick:
        events.eventsMain()
        previousTickTime = time.time()

    if currentTime - previousFrameTime >= durationFrame:
        deltaTime = currentTime - previousFrameTime
        player.updatesPhysics(events, deltaTime * TPS)
        dis.displayMain(worldMatrix, player)
        previousFrameTime = time.time() 
quit()