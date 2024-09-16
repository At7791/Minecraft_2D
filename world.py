import numpy as np
from game_data_loader import load_file, save_to_file

class World:
    def __init__(self, directory_path) -> None:
        self.directory_path = directory_path
        self.world_path = f"{self.directory_path}\world.pkl"
        try:
            self.worldGLOBAL = load_file(self.world_path)
        except:
            self.worldGLOBAL = {}
            save_to_file(self.world_path, self.worldGLOBAL)
        
        # World parameters
        self.chunkWidth = 20

    def save(self, loadedWorld):
        for chunkX in loadedWorld.keys():
            self.worldGLOBAL[chunkX] = loadedWorld[chunkX]
        # save_to_file(self.world_path, self.worldGLOBAL)

    def chunk_X(self, position):
        return int(position // self.chunkWidth)

    def loader(self, world, worldLoadRadius, refferenceX):
        chunkPosition = self.chunk_X(refferenceX)
        
        # Determins the already loaded chunks
        chunks_already_loaded = np.array(list(world.keys()))

        # Determins which chunks need to be loaded
        chunks_to_be_loaded = np.array([])
        for i in range(chunkPosition - worldLoadRadius, chunkPosition + worldLoadRadius + 1):
            chunks_to_be_loaded = np.append(chunks_to_be_loaded, i)

        # loads chunks and generates those which need to
        for chunkX in (np.setdiff1d(chunks_to_be_loaded, chunks_already_loaded)):
            chunkX = int(chunkX)
            if chunkX in self.worldGLOBAL.keys():
                world[chunkX] = self.worldGLOBAL[chunkX]
            else:
                world[chunkX] = self.generator(chunkX)


        # unloads chunks and saves those which need to
        for chunkX in (np.setdiff1d(chunks_already_loaded, chunks_to_be_loaded)):
            self.worldGLOBAL[chunkX] = world.pop(chunkX)
 
        return world
    
    def generator(self, chunkX):
        chunk = []

        for j in range(self.chunkWidth):
            chunk.append(["bedrock", "stone", "dirt"])
            for k in range(abs(chunkX) + 1):
                chunk[j].append("grass_block")

        return chunk