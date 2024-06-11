from random import *

def world_generator(worldSizeX, worldSizeY, blocksID):
    worldMatrix = []

    
    for i in range(worldSizeX):
        intermediateArray = []
        for j in range(worldSizeY):
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