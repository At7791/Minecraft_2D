from random import *

def world_generator(worldSizeX, worldSizeY, blocksID):
    print("generates a world and returns a matrix filled with block IDs")

    worldMatrix = []

    
    for i in range(worldSizeY):
        intermediateArray = []
        for j in range(worldSizeX):
            if j <2: 
                intermediateArray.append("bedrock")
            else:
                intermediateArray.append("stone")
                
        worldMatrix.append(intermediateArray)

    for i in range(len(worldMatrix)):
        print(worldMatrix[i])

    return worldMatrix