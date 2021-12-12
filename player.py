
from move import Move

class Player:
    def __init__(self, playerType, color: str):
        self.playerType = playerType
        self.color = color
        self.selectedWorker = None
    
    def playMove(self, currBoard):
        pass

    def getMoves(self, currBoard):
        pass

    def getBuilds(self, currBoard):
        pass

    def executeMove(self, move: Move):
        pass
