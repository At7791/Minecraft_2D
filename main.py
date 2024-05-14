from pygame import *
import sys
from display import Display
from random import *
from world_generator import world_generator
from player_code import PlayerClass

blocksID = {"air": ["air"], "stone": ["stone"], "dirt": ["dirt"], "grass_block": ["grass_block_side"], "bedrock": ["bedrock"]}

done = False
TPS = 30

sizeX, sizeY = 50,50

testWorld = world_generator(sizeX, sizeY, blocksID)

dis = Display("Faithful64x", blocksID)
player = PlayerClass(sizeX, sizeY)

while not done:

    dis.displayMain(testWorld, player)


quit()