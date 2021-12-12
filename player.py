
from move import Move

class Player:
    def __init__(self, playerType, color: str):
        self.playerType = playerType
        self.color = color
        self.selectedWorker = None
        self.directionToMove = None
        self.directionToBuild = None
        self.possibleWhiteWorkers = ["A", "B"]
        self.possibleBlueWorkers = ["Y", "Z"]
        self.possibleWorkers = self.possibleWhiteWorkers if color == "white" else self.possibleBlueWorkers
        self.possibleMoves = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        self.possibleBuilds = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        
    def playMove(self, currBoard):
        self.getWorker()
        self.getMove()
        self.getBuild()

    def executeMove(self):
        pass

    def executeBuild(self):
        pass

    def getWorker(self):
        while self.selectedWorker not in self.possibleWorkers:
            self.selectedWorker = input("Select worker to move\n")
            if self.selectedWorker not in self.possibleWorkers:
                if self.selectedWorker in self.possibleWhiteWorkers or self.selectedWorker in self.possibleBlueWorkers:
                    print("That is not your worker\n")
                else:
                    print("Not a valid worker\n")
        #return self.selectedWorker

    def getMove(self):
        while self.directionToMove not in self.validMoves():
            self.directionToMove = input("Select direction to move\n")
            if self.directionToMove not in self.validMoves():
                print("Not a valid direction\n")
        #return self.directionToMove

    def getBuild(self):
        while self.directionToBuild not in self.validBuilds():
            self.directionToBuild = input("Select direction to build\n")
            if self.directionToBuild not in self.validBuilds():
                print("Not a valid direction\n")
        #return self.directionToBuild
    
    def validMoves(self):
        return [element for element in self.possibleMoves if element != "n"]

    def validBuilds(self):
        return [element for element in self.possibleBuilds if element != "n"]
    
    def getWorkersString(self):
        return "AB" if self.color == "white" else "YZ"
