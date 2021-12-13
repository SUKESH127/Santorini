class History:
    def __init__(self, startingBoardState):
        mementos = []
        currBoardIndex = -1
        maxBoardIndex = -1
        mementos.backup(startingBoardState)
    
    def backup(self, currBoardState):
        mementos.append(currBoardState)
        currBoardIndex += 1
        maxBoardIndex += 1

    def moveBack(self):
        if currBoardIndex > 0:
            currBoardIndex -= 1
    
    def moveForward(self):
        if currBoardIndex < maxBoardIndex:
            currBoardIndex += 1

    def getCurrentBoardState(self):
        return self.mementos[self.currBoardIndex]

    