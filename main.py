from pygame import *
import sys
from display import Display
from random import *
from world_generator import world_generator
from player_code import PlayerClass

done = False
TPS = 30

sizeX, sizeY = 5, 10

testWorld = world_generator(sizeX, sizeY)

dis = Display("Faithful64x")
player = PlayerClass()

while not done:

    dis.displayMain(testWorld, player)


quit()