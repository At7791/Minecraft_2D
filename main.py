import pygame
from pygame import *
import sys
from display import Display
from random import *
from world_generator import world_generator
from player_code import PlayerClass
from event_controler import Events
import time

blocksID = {"air": ["air"], "stone": ["stone"], "dirt": ["dirt"], "grass_block": ["grass_block_side"], "bedrock": ["bedrock"]}

done = False
TPS = 20
FPS = 240


previousTime = time.time()
sizeX, sizeY = 10, 500

testWorld = world_generator(sizeX, sizeY, blocksID)

clock = pygame.time.Clock()
dis = Display("Faithful64x", blocksID) 
player = PlayerClass(sizeX, sizeY)
events = Events()

while not done:
    # Calculate delta time
    nowTime = time.time()
    deltaTime = nowTime - previousTime
    previousTime = nowTime

    events.eventsMain()
    player.updates(events, deltaTime, TPS)
    dis.displayMain(testWorld, player)

    clock.tick(FPS)
quit()