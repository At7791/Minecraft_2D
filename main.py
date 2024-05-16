import pygame
from pygame import *
import sys
from display import Display
from random import *
from world_generator import world_generator
from entity_code import EntityClass, PlayerClass
from event_controler import Events 
import time

blocksID = {"air": ["air"], "stone": ["stone"], "dirt": ["dirt"], "grass_block": ["grass_block_side"], "bedrock": ["bedrock"]}

done = False
TPS = 20
FPS = 60


previousTime = time.time()
sizeX, sizeY = 3, 7

worldMatrix = world_generator(sizeX, sizeY, blocksID)
  
clock = pygame.time.Clock()
dis = Display("Faithful64x", blocksID) 
player = PlayerClass()
events = Events()
EntityClass.worldMatrix = worldMatrix

while not done:
    # Calculate delta time
    nowTime = time.time()
    deltaTime = nowTime - previousTime
    previousTime = nowTime

    events.eventsMain()
    player.updates(events, deltaTime, TPS)
    dis.displayMain(worldMatrix, player)

    clock.tick(FPS)
quit()