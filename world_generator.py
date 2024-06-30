from random import *

def world_generator(sizeX, sizeY, StartWorld, blocksID):
    worldMatrix = []
    
    a = 2
    b = 20
    c = 30

    for i in range(2*StartWorld + sizeX):
        intermediateArray = []

        if i < StartWorld:
            pass
        elif i > StartWorld + sizeX:
            pass
        else:
            gamble = randrange(0, 4)
            if gamble < 2:
                b = b
                c = c
            elif gamble == 2:
                b += 1 
                c += 1
            elif gamble == 3:
                b -= 1
                c -= 1

            for j in range(sizeY):
                if j < a: 
                    intermediateArray.append("bedrock")
                elif a <= j <= b:
                    intermediateArray.append("stone")
                elif b <= j <= c-1 :
                    intermediateArray.append("dirt")
                elif c == j:
                    intermediateArray.append("grass_block")
                else:
                    intermediateArray.append("air")
                
        print(intermediateArray)  

        worldMatrix.append(intermediateArray)
    return worldMatrix

def render_condition(sizeY, rendering):
    if rendering == False:       #change if to while and the game crashes at the world border, but with if it does nothing
        generated_world =[]
        for j in range(sizeY):
            generated_world.append("bedrock")
        sizeY += 1
        print (generated_world)
        return generated_world