class Converter():
    def __init__(self, worldLoadDistance, playerX):
        self.worldLoadDistance = worldLoadDistance
        self.playerX = int(playerX)
        self.convertedX = 0

    # Converts the X coordinate from the global world matrix coordinate system, to the loaded worldmatixe coordinate system
    def XWMGToLoadedWM(self, x):
        self.convertedX = x - self.playerX + self.worldLoadDistance - 1
        return self.convertedX