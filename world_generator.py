from random import *

def world_generator(worldSizeX, worldSizeY, blocksID):
    worldMatrix = []

    
    # for i in range(worldSizeY):
    #     intermediateArray = []
    #     for j in range(worldSizeX):
    #         if j <2: 
    #             intermediateArray.append("bedrock")
    #         else:
    #             if i % 2 == 0:
    #                 intermediateArray.append("stone")
                
    #     worldMatrix.append(intermediateArray)

    # worldMatrix = [
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "stone", "stone"],
    # ["air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "stone", "stone", "air", "air", "stone", "stone", "stone", "stone"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "air", "stone"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "stone", "stone"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "air", "stone"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "stone", "stone"],
    # ["air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "stone", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "stone", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "stone", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "stone", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "stone", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "stone", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "stone", "stone", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "stone", "stone", "stone", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "stone", "stone", "stone", "stone", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "stone", "stone", "stone", "stone", "stone", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "stone", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ["bedrock", "bedrock", "stone", "air", "air", "air", "air", "air", "air", "air", "air", "air"],
    # ]

    worldMatrix = []
    for i in range(50):
        worldMatrix.append([ "bedrock", "bedrock", "stone", "air", "air", "air"])
        worldMatrix.append([ "air", "air", "air", "air", "air", "air"])
        worldMatrix.append([ "bedrock", "air", "stone", "air", "air", "air"])
        worldMatrix.append([ "bedrock", "air", "stone", "air", "air", "air"])
        worldMatrix.append([ "bedrock", "air", "stone", "air", "air", "air"])
    # worldMatrix = [
    # ["stone","stone","stone","stone","stone","stone","stone","stone","stone","stone","stone","stone",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ["stone", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air", "air",],
    # ]

    return worldMatrix