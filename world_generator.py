from random import *
from math import trunc

def world_generator(sizeX, sizeY, StartWorld, blocksID, HeightBedrockRight1, HeightStoneRight1, HeightDirtRight1):
    worldMatrix = []
    
    a = HeightBedrockRight1
    b = HeightStoneRight1
    c = HeightDirtRight1

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
            elif gamble == 3:
                b -= 1
                c -= 1

            for j in range(sizeY):
                if j < a: 
                    intermediateArray.append("bedrock")
                elif a <= j < b:
                    intermediateArray.append("stone")
                elif b <= j < c :
                    intermediateArray.append("dirt")
                elif c == j:
                    intermediateArray.append("grass_block")
                else:
                    intermediateArray.append("air")

                
        print(f"{intermediateArray}; {i}")  

        worldMatrix.append(intermediateArray)
    return worldMatrix, a, b, c

def rendering(playerX, RenderDistance, worldMatrixGLOBAL, sizeY, d, e, f, a, b, c):
    RenderCoordinateRight = playerX + RenderDistance
    RenderCoordinateLeft = playerX - RenderDistance
    IntermediateGeneration = []

    for i in range (6):
        if worldMatrixGLOBAL[trunc(RenderCoordinateRight- i)] == []:
            
            gamble = randrange(0, 4)
            if gamble < 2:
                pass
            elif gamble == 2 and c+1 != sizeY:
                b += 1 
                c += 1
            elif gamble == 3:
                b -= 1
                c -= 1

            for j in range(sizeY):
                    if j < a: 
                        IntermediateGeneration.append("bedrock")
                    elif a <= j < b:
                        IntermediateGeneration.append("stone")
                    elif b <= j < c :
                        IntermediateGeneration.append("dirt")
                    elif c == j:
                        IntermediateGeneration.append("grass_block")
                    else:
                        IntermediateGeneration.append("air")
            worldMatrixGLOBAL[trunc(RenderCoordinateRight)] = IntermediateGeneration
            worldMatrixGLOBAL[trunc(RenderCoordinateRight) + 1] = []
            return IntermediateGeneration, a ,b, c, d, e, f
        
        if worldMatrixGLOBAL[trunc(RenderCoordinateLeft + i)] == []:
            gamble = randrange(0, 4)
            if gamble < 2:
                pass
            elif gamble == 2 and c+1 != sizeY:
                e += 1 
                f += 1
            elif gamble == 3:
                e -= 1
                f -= 1

            for j in range(sizeY):
                    if j < d: 
                        IntermediateGeneration.append("bedrock")
                    elif d <= j < e:
                        IntermediateGeneration.append("stone")
                    elif e <= j < f :
                        IntermediateGeneration.append("dirt")
                    elif f == j:
                        IntermediateGeneration.append("grass_block")
                    else:
                        IntermediateGeneration.append("air")
            worldMatrixGLOBAL[trunc(RenderCoordinateLeft)] = IntermediateGeneration
            return IntermediateGeneration, d, e, f, a ,b, c
        
        else:
            return IntermediateGeneration, d, e, f, a ,b, c
    
    
