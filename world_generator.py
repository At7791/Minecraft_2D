from random import *
from main import rendering

def world_generator(sizeX, sizeY, blocksID):
    worldMatrix = []

    for i in range(sizeX):
        intermediateArray = []
        for j in range(sizeY):
            if j <2: 
                intermediateArray.append("bedrock")
            elif 2 <= j <= 10:
                intermediateArray.append("stone")
            elif 10 <= j <= 14:
                intermediateArray.append("dirt")
            elif 15 == j:
                intermediateArray.append("grass_block")

                
        worldMatrix.append(intermediateArray)
        print (worldMatrix)

    return worldMatrix

def render_condition(sizeY, rendering):
    while rendering == False:
        generated_world =[]
        for j in range(sizeY):
            if j <2: 
                generated_world.append("bedrock")
            elif 2 <= j <= 10:
                generated_world.append("stone")
            elif 10 <= j <= 14:
                generated_world.append("dirt")
            elif 15 == j:
                generated_world.append("grass_block")
