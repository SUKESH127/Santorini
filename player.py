
from move import Move
from worker import Worker

class Player:

    def __init__(self, playerType, color: str):
        self.playerType = playerType
        self.color = color
        if color == "white":
            self.w1 = Worker(self.color, [1, 3])
            self.w2 = Worker(self.color, [3, 1])
        else:
            self.w1 = Worker(self.color, [1, 1])
            self.w2 = Worker(self.color, [3, 3])
        self.selectedWorker = None
        self.possibleWorkers = ["A", "B"] if color == "white" else ["A", "B"]
        self.possibleDirections = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        
    def playMove(self, currBoard):
        pass
        # m = self.selectMove(currBoard)
        # m.executeMove()

    def selectMove(self, currBoard):
        return None
    
    def getWorkersString(self):
        return "AB" if self.color == "white" else "YZ"
