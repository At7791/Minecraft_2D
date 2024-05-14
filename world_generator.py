from random import *

def world_generator(worldSizeX, worldSizeY, blocksID):
    worldMatrix = []

    
    for i in range(worldSizeY):
        intermediateArray = []
        for j in range(worldSizeX):
            if j <2: 
                intermediateArray.append("bedrock")
            else:
                intermediateArray.append("stone")
                
        worldMatrix.append(intermediateArray)

    return worldMatrix