from random import *

def world_generator(sizeX, sizeY, blocksID):
    worldMatrix = []
    a = 2
    b = 10
    c = 15

    for i in range(sizeX):
        intermediateArray = []

        gamble = randrange(0, 3)
        if gamble == 1:
            b += 1 
            c += 1
        elif gamble == 2:
            b -= 1
            c -= 1
        elif gamble == 0:
            b = b
            c = c

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