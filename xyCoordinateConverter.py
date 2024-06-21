class Converter():
    def __init__(self, worldLoadDistance, playerX):
        self.worldLoadDistance = worldLoadDistance
        self.playerX = int(playerX)
        self.convertedX = 0
    def XWMGToLoadedWM(self, x):     # Converts the X coordinate from the global world matrix coordinate system, to the loaded worldmatixe coordinate system
        self.convertedX = x - self.playerX + self.worldLoadDistance
        return self.convertedX