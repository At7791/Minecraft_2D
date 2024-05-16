import pygame
from pygame import *
import sys
from display import Display
from random import *
from world_generator import world_generator
from player_code import PlayerClass
from event_controler import Events

blocksID = {"air": ["air"], "stone": ["stone"], "dirt": ["dirt"], "grass_block": ["grass_block_side"], "bedrock": ["bedrock"]}

done = False
TPS = 30



sizeX, sizeY = 10, 500

testWorld = world_generator(sizeX, sizeY, blocksID)

clock = pygame.time.Clock()
dis = Display("Faithful64x", blocksID) 
player = PlayerClass(sizeX, sizeY)
events = Events()

while not done:
    events.eventsMain()
    player.updates(events)
    dis.displayMain(testWorld, player)

    clock.tick(TPS)
quit()