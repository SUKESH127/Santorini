class History:
    def __init__(self):
        self.mementos = []
        self.currBoardIndex = -1
        self.maxBoardIndex = -1
    
    def backup(self, boardState):
        self.mementos = self.mementos[:self.currBoardIndex+1]
        self.mementos.append(boardState)
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

    def updateWorkers(self, players):
        print(f'returning memento at index: {self.currBoardIndex}')
        b = self.getCurrentBoardState()
        for i in range(5):
            for j in range(5):
                pos = [j, i]
                w = b.getSquare(pos).worker
                if w == 'A':
                    players[0].w1.position = pos
                elif w == 'B':
                    players[0].w2.position = pos
                elif w == 'Y':
                    players[1].w1.position = pos
                elif w == 'Z':
                    players[1].w2.position = pos

    