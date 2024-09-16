from math import trunc

class Hitboxes():
    def __init__(self, lengthX, lengthY):
        self.lengthX, self.lengthY = lengthX, lengthY
        self.offsetWithX = self.lengthX / 2

        self.highBorder = 0
        self.lowBorder = 0
        self.leftBorder = 0
        self.rightBorder = 0

        self.blocksOverlapped = []

    # Updates the state and position of the hitbox relative to the entity
    def update(self, x, y):
        self.x = x
        self.y = y
        self.highBorder = y + self.lengthY
        self.lowBorder = y
        self.leftBorder = x - self.offsetWithX
        self.rightBorder = x + self.offsetWithX

        # generates a list of blocks with which the hitbox overlapps
        self.blocksOverlapped = []
        for i in range(trunc(self.leftBorder), trunc(self.rightBorder) + 1):
            intermediateArray = []
            for j in range(trunc(self.lowBorder), trunc(self.highBorder) + 1):
                intermediateArray.append((i, j))
            self.blocksOverlapped.append(intermediateArray)

    # Returns list of blocks containing the bottom border of the hitbox
    def lowBlocks(self):
        blocks = []
        for columns in self.blocksOverlapped:
            blocks.append(columns[0])
        return blocks

    # Returns list of blocks containing the high border of the hitbox
    def highBlocks(self):
        blocks = []
        for columns in self.blocksOverlapped:
            blocks.append(columns[len(self.blocksOverlapped[0]) - 1])
        return blocks
    
    # Returns list of blocks containing the left border of the hitbox
    def leftBlocks(self):
        return self.blocksOverlapped[0]
    
    # Returns list of blocks containing the right border of the hitbox
    def rightBlocks(self):
        return self.blocksOverlapped[len(self.blocksOverlapped) - 1]