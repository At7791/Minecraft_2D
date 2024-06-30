import json
import os

file = open("block_data/blocksIDs.json", "r")
preExistingData = json.load(file)
file.close()

running = True
addedData = {}

while running == True:
    print("Here are the infomation that you need to fill to create a new block. (type 'escape' to quit)")
    while True:
        blockID = str(input(" - Block ID: "))
        
        if blockID == "escape":
            break

        validBlockID = True
        for existingBlockID in preExistingData.keys():
            if blockID == existingBlockID:
                validBlockID = False
        
        if validBlockID:
            print("   OK!", end = "")
            break
        else:
            print("Invalid Block ID!")

    if blockID == "escape":
        break

    while True:
        blockTextureName = str(input("\n - Block Texture Name: "))
        
        if os.path.exists(f"textures/minecraft_regular_versionfile/assets/minecraft/textures/block/{blockTextureName}.png"):
            alreadyUsedTexture = False
            for existingBlockID in preExistingData.keys():
                if preExistingData[existingBlockID][0] == blockTextureName:
                    alreadyUsedTexture = True
            
            if alreadyUsedTexture == True:
                print("   OK!     !!! Warning !!! This texture is already shared with another block.", end = "")
                break
            else:
                print("   OK!", end = "")
                break

        else:
            print("Invalid Block Texture Name!")

    blockHardness = float(input("\n - Block Hardness: "))

    print(f"Block ID: {blockID}   Name of the Texture: {blockTextureName}    Block Hardness: {blockHardness}")
    addedData[blockID] = [blockTextureName, blockHardness]
if addedData != {}:
    print("\n\nThese are the blocks you have created.")

    for addedBlockIDs in addedData.keys():
        print(f"\nID: {addedBlockIDs}")
        print(f"Texture Name: {addedData[addedBlockIDs][0]}")
        print(f"Block Hardness: {addedData[addedBlockIDs][1]}")
    print()

    while True:
        addingTheBlocks = str(input("Do you want do add all these blocks to the block data file? (y/n)"))
        if addingTheBlocks == "y":
            preExistingData.update(addedData)
            print(preExistingData)
        else:
            print("No data added!")

file = open("block_data/blocksIDs.json", "w")
preExistingData = json.dump(preExistingData, file)
file.close()