from move import Move
from board import Board
from player import Player

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

    def getMove(self, board):
        validMoves = self.selectedWorker.findAllMoves(board)
        directionToMove = input("Select direction to move\n")
        while directionToMove not in validMoves:
            print("Not a valid direction\n") # e.g. "cannot move ne"
            directionToMove = input("Select direction to move\n")
        return directionToMove

    def getBuild(self, board):
        validBuilds = self.selectedWorker.findAllBuilds(board)
        directionToBuild = input("Select direction to build\n")
        while directionToBuild not in validBuilds:
            print("Not a valid direction\n") # e.g. "cannot build ne"
            directionToBuild = input("Select direction to build\n")
        return directionToBuild

    def selectMove(self, board):
        self.getWorker()
        moveDir = self.getMove(board)
        buildDir = self.getBuild(board)
        return Move(self.selectedWorker, moveDir, buildDir)

