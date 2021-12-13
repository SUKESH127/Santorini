class History:
    def __init__(self, startingBoardState):
        self.mementos = []
        self.currBoardIndex = -1
        self.maxBoardIndex = -1
        self.backup(startingBoardState)
    
    def backup(self, currBoardState):
        self.mementos.append(currBoardState)
        self.currBoardIndex += 1
        self.maxBoardIndex = self.currBoardIndex

    def moveBack(self):
        if self.currBoardIndex > 0:
            self.currBoardIndex -= 1
            return True
        return False
    
    def moveForward(self):
        if self.currBoardIndex < self.maxBoardIndex:
            self.currBoardIndex += 1
            return True
        return False

    def getCurrentBoardState(self):
        return self.mementos[self.currBoardIndex]

    