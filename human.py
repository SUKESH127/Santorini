from move import Move
from board import Board
from player import Player

class Human(Player):
    def __init__(self, color: str):
        super().__init__("human", color)      
        
    def getWorker(self):
        while self.selectedWorker not in self.possibleWorkers:
            self.selectedWorker = input("Select worker to move\n")
            if self.selectedWorker not in self.possibleWorkers:
                if self.selectedWorker in ['A', 'B'] or self.selectedWorker in ['Y', 'Z']:
                    print("That is not your worker")
                else:
                    print("Not a valid worker")

    def getMove(self, board):
        validMoves = self.selectedWorker.findAllMoves(board)
        directionToMove = input("Select direction to move\n")
        while directionToMove not in validMoves:
            print(f'Cannot move {directionToMove}')
            directionToMove = input("Select direction to move\n")
        return directionToMove

    def getBuild(self, board):
        validBuilds = self.selectedWorker.findAllBuilds(board)
        directionToBuild = input("Select direction to build\n")
        while directionToBuild not in validBuilds:
            print(f'Cannot build {directionToMove}')
            directionToBuild = input("Select direction to build\n")
        return directionToBuild

    def selectMove(self, currBoard):
        self.getWorker()
        moveDir = self.getMove(currBoard)
        buildDir = self.getBuild(currBoard)
        return Move(self.selectedWorker, moveDir, buildDir, currBoard)
    
    def playMove(self, currBoard):
        m = self.selectMove(currBoard)
        m.executeMove()

