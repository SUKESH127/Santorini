
from move import Move

class Player:

    def __init__(self, playerType, color: str):
        self.playerType = playerType
        self.color = color
        if color = "white":
            self.w1 = Worker("white", [1, 3])
            self.w1 = Worker("white", [3, 1])
        else:
            self.w1 = Worker("blue", [1, 1])
            self.w2 = Worker("blue", [3, 3])
        self.selectedWorker = None
        self.possibleWorkers = ["A", "B"] if color == "white" else ["A", "B"]
        self.possibleDirections = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        
    def playMove(self, currBoard):
        m = self.selectMove()
        m.executeMove()

    def selectMove(self, currBoard):
        return None
    
    def getWorkersString(self):
        return "AB" if self.color == "white" else "YZ"
