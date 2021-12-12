
from move import Move

class Player:

    def __init__(self, playerType, color: str):
        self.playerType = playerType
        self.color = color
        self.selectedWorker = None
        self.possibleWorkers = ["A", "B"] if color == "white" else ["A", "B"]
        self.possibleDirections = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        
    def playMove(self, currBoard):
        self.getWorker()
        self.getMoves()
        self.getBuild()
        self.executeMove()


    def executeMove(self):
        pass

    def getWorker(self):
        pass

    def getMove(self):
        pass

    def getBuild(self):
        pass
    
    def validMoves(self, worker):
        moves = []
        for i in range(-1, 1):
            for j in range(-1, 1):
                if ()
        return [element for element in self.possibleMoves if element != "n"]

    def validBuilds(self):
        return [element for element in self.possibleBuilds if element != "n"]
    
    def getWorkersString(self):
        return "AB" if self.color == "white" else "YZ"
