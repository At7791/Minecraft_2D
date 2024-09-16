from math import floor, ceil, trunc

class Converter():
    def __init__(self, worldLoadRadius, chunkWidth, loadedWorld, zoom, windowSizeX, windowSizeY, player):
        self.worldLoadRadius = worldLoadRadius
        self.chunkWidth = chunkWidth
        self.loadedWorld = loadedWorld
        self.zoom = zoom
        self.windowSizeX, self.windowSizeY = windowSizeX, windowSizeY

        self.player = player


    def to_block_X(self, position):
        if position < 0:
            position = floor(position)
        return int(position)
    
    def to_block_Y(self, position):
        position -= 0.0000001
        if position < 0:
            position = floor(position)
        return int(position + 1)
    
    def chunk_X(self, position):
        return int(position // self.chunkWidth)
    
    def in_chunk_X(self, position):
        if position < 0:
            position = floor(position)
        return int(position % self.chunkWidth)
    
    def blockNature(self, position):
        x, y = position

        if self.is_block_in_world((x, y)):
            block = self.loadedWorld[self.chunk_X(x)][self.in_chunk_X(x)][self.to_block_Y(y)]
        else:
            block = None

        return block
    
    def is_block_in_world(self, position):
        x, y = position
        result = False

        if self.chunk_X(x) in self.loadedWorld.keys():
            if self.to_block_Y(y) in range(0, len(self.loadedWorld[self.chunk_X(x)][self.in_chunk_X(x)])):
                result = True

        return result
    # Converts the minecraft coordinates into coordinates on Screen
    def XYonScreen(self, x, y):
        XonScreen = - self.player.getPlayerCoordinates()[0] * self.zoom + self.windowSizeX // 2 + self.zoom * x
        YonScreen = self.player.getPlayerCoordinates()[1] * self.zoom + self.windowSizeY // 2 - self.zoom * (y - 1.6)
        return XonScreen, YonScreen
    
    # Converts the coordinates on screen into coordinates in Minecraft
    def XYinWorld(self, x, y, blockAlignment = False):
        XinWorld = x / self.zoom + self.player.getPlayerCoordinates()[0] - self.windowSizeX / 2 / self.zoom
        YinWorld = - y / self.zoom + self.player.getPlayerCoordinates()[1] + self.windowSizeY / 2 / self.zoom + 1.6

        if blockAlignment == True:
            XinWorld, YinWorld = self.to_block_X(XinWorld), self.to_block_Y(YinWorld)

        return XinWorld, YinWorld
