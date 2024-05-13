from random import *

def world_generator(worldSizeX, worldSizeY):
    print("generates a world and returns a matrix filled with block IDs")

    worldMatrix = []


    for i in range(worldSizeY):
        intermediateArray = []
        for j in range(worldSizeX):
            intermediateArray.append(randint(0,2))
        worldMatrix.append(intermediateArray)

    for i in range(len(worldMatrix)):
        print(worldMatrix[i])

    return worldMatrix