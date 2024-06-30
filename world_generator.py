from random import *
from math import trunc

def world_generator(sizeX, sizeY, StartWorld, blocksID, HeightBedrockRight1, HeightDeepslate1, HeightStoneRight1, HeightDirtRight1):
    worldMatrix = []
    
    a = HeightBedrockRight1
    b = HeightDeepslate1
    c = HeightStoneRight1
    d = HeightDirtRight1

    for i in range(2*StartWorld + sizeX):
        intermediateArray = []
        if i == 1:
            for j in range(sizeY):
                intermediateArray.append("bedrock")
        elif i < StartWorld:
            pass
        elif i > StartWorld + sizeX:
            pass
        else:
            gamble = randrange(0, 4)
            if gamble < 2:
                pass
            elif gamble == 2 and c+1 != sizeY:
                b += 1 
                c += 1
                d += 1
            elif gamble == 3:
                b -= 1
                c -= 1
                d -= 1

            for j in range(sizeY):
                if j < a: 
                    intermediateArray.append("bedrock")
                elif a <= j < b:
                    intermediateArray.append("deepslate")
                elif b <= j < c:
                    t = randint(0,10)
                    if t <=5:
                        intermediateArray.append("stone")
                    if t == 6:
                        intermediateArray.append("andesite")
                    if t == 7:
                        intermediateArray.append("diorite")
                    if t == 8:
                        intermediateArray.append("granite")
                elif c <= j < d :
                    intermediateArray.append("dirt")
                elif d == j:
                    intermediateArray.append("grass_block")
                else:
                    intermediateArray.append("air")

                
        print(f"{intermediateArray}; {i}")  

        worldMatrix.append(intermediateArray)
    return worldMatrix, a, b, c ,d

def rendering(player.x, RenderDistance, worldMatrixGLOBAL, sizeY, HeightBedrockRight1, HeightDeepsRight1, HeightStoneRight1, HeightDirtRight1, HeightBedrockLeft1, HeightDeepslateLeft1, HeightStoneLeft1, HeightDirtLeft1):
    RenderCoordinateRight = player.x + RenderDistance
    RenderCoordinateLeft = player.x - RenderDistance
    IntermediateGeneration = []
    
    if worldMatrixGLOBAL[trunc(RenderCoordinateRight)] == []:
        gamble = randrange(0, 4)
        if gamble < 2:
            pass
        elif gamble == 2 and c+1 != sizeY:
            HeightBedrockRight1 += 1
            HeightDeepsRight1 += 1
            HeightStoneRight1 += 1
        elif gamble == 3:
            HeightBedrockRight1 -= 1
            HeightDeepsRight1 -= 1
            HeightStoneRight1 -= 1

        for j in range(sizeY):
            if j < a: 
                IntermediateGeneration.append("bedrock")
            elif a <= j < b:
                IntermediateGeneration.append("deepslate")
            elif b <= j < c:
                t = randint(0,10)
                if t <=5:
                    IntermediateGeneration.append("stone")
                if t == 6:
                    IntermediateGeneration.append("andesite")
                if t == 7:
                    IntermediateGeneration.append("diorite")
                if t == 8:
                    IntermediateGeneration.append("granite")
            elif c <= j < d :
                IntermediateGeneration.append("dirt")
            elif d == j:
                IntermediateGeneration.append("grass_block")
            else:
                IntermediateGeneration.append("air")

        print(f"{IntermediateGeneration}")  
        worldMatrixGLOBAL[trunc(RenderCoordinateRight)] = IntermediateGeneration
        worldMatrixGLOBAL[trunc(RenderCoordinateRight) + 1] = []
        return IntermediateGeneration, a ,b, c, d, e, f
    
    elif worldMatrixGLOBAL[trunc(RenderCoordinateLeft)] == []:
        for j in range(sizeY):
            if j < a: 
                IntermediateGeneration.append("bedrock")
            elif a <= j < b:
                IntermediateGeneration.append("deepslate")
            elif b <= j < c:
                t = randint(0,10)
                if t <=5:
                    IntermediateGeneration.append("stone")
                if t == 6:
                    IntermediateGeneration.append("andesite")
                if t == 7:
                    IntermediateGeneration.append("diorite")
                if t == 8:
                    IntermediateGeneration.append("granite")
            elif c <= j < d :
                IntermediateGeneration.append("dirt")
            elif d == j:
                IntermediateGeneration.append("grass_block")
            else:
                IntermediateGeneration.append("air")
        print(f"{IntermediateGeneration}")  
        
        worldMatrixGLOBAL[trunc(RenderCoordinateLeft)] = IntermediateGeneration
        return IntermediateGeneration, d, e, f, a ,b, c
    
    else:
        return IntermediateGeneration, d, e, f, a ,b, c
    
    
