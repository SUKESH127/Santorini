from move import Move
from board import Board

class Human(Player):
     def __init__(self, color: str):
        super().__init__(self, "Human", color)      
        
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