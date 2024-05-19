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

    worldMatrix = [
    ["bedrock", "bedrock", "stone", "stone", "air", "air"],
    ["bedrock", "bedrock", "stone", "stone", "air", "air"],
    ["bedrock", "bedrock", "stone", "stone", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ["bedrock", "bedrock", "stone", "air", "air", "air"],
    ]

    return worldMatrix