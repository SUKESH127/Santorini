class History:
    def __init__(self, startingBoardState):
        mementos = []
        currBoardIndex = -1
        maxBoardIndex = -1
        mementos.backup(startingBoardState)
    
    def backup(self, currBoardState):
        mementos.append(currBoardState)
        currBoardIndex += 1
        maxBoardIndex = currBoardIndex

    def moveBack(self):
        if currBoardIndex > 0:
            currBoardIndex -= 1
            return True
        return False
    
    def moveForward(self):
        if currBoardIndex < maxBoardIndex:
            currBoardIndex += 1
            return True
        return False

    def getCurrentBoardState(self):
        return self.mementos[self.currBoardIndex]

    