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

    def update(self, x, y):
        self.highBorder = y + self.lengthY
        self.lowBorder = y
        self.leftBorder = x - self.offsetWithX
        self.rightBorder = x + self.offsetWithX

        self.thighBorder = trunc(self.highBorder)
        self.tlowBorder = trunc(self.lowBorder)
        self.tleftBorder = trunc(self.leftBorder)
        self.trightBorder = trunc(self.rightBorder)

        self.blocksOverlapped = []
        for i in range(self.tleftBorder, self.trightBorder + 1):
            intermediateArray = []
            for j in range(self.tlowBorder, self.thighBorder + 1):
                intermediateArray.append((i, j))
            self.blocksOverlapped.append(intermediateArray)

    def lowBlocks(self):
        blocks = []
        for columns in self.blocksOverlapped:
            blocks.append(columns[0])
        return blocks
    
    def highBlocks(self):
        blocks = []
        for columns in self.blocksOverlapped:
            blocks.append(columns[len(self.blocksOverlapped[0]) - 1])
        return blocks
    
    def leftBlocks(self):
        return self.blocksOverlapped[0]
    
    def rightBlocks(self):
        return self.blocksOverlapped[len(self.blocksOverlapped) - 1]