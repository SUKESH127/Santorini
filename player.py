
from move import Move
from worker import Worker

class Player:

    def __init__(self, playerType, color: str):
        self.playerType = playerType
        self.color = color
        if color == "white":
            self.w1 = Worker(self.color, [1, 3], "A")
            self.w2 = Worker(self.color, [3, 1], "B")
        else:
            self.w1 = Worker(self.color, [1, 1], "Y")
            self.w2 = Worker(self.color, [3, 3], "Z")
        self.selectedWorker = None
        self.possibleWorkers = ["A", "B"] if color == "white" else ["Y", "Z"]
        self.possibleDirections = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        
    def playMove(self, currBoard):
        pass
        # m = self.selectMove(currBoard)
        # m.execute()

    def selectMove(self, currBoard):
        return None
    
    def getWorkersString(self):
        return "AB" if self.color == "white" else "YZ"
