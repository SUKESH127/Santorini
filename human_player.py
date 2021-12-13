from move import Move
from board import Board
from player import Player

class HumanPlayer(Player):
    def __init__(self, color: str):
        super().__init__("human", color)      
        
    def getWorker(self):
        w = input("Select worker to move\n")
        while w not in self.possibleWorkers:
            if w in ['A', 'B'] or w in ['Y', 'Z']:
                print("That is not your worker")
            else:
                print("Not a valid worker")
            w = input("Select worker to move\n")
        if w == 'A' or w == 'Y':
            self.selectedWorker = self.w1
        else:
            self.selectedWorker = self.w2


    def getMove(self, board):
        validMoves = self.selectedWorker.findAllMoves(board)
        directionToMove = input("Select direction to move\n")
        while directionToMove not in validMoves:
            if directionToMove not in self.possibleDirections:
                print("Not a valid direction")
            else:
                print(f'Cannot move {directionToMove}')
            directionToMove = input("Select direction to move\n")
        return directionToMove

    def getBuild(self, board, moveDir):
        validBuilds = self.selectedWorker.findAllBuilds(board, moveDir)
        directionToBuild = input("Select direction to build\n")
        while directionToBuild not in validBuilds:
            if directionToBuild not in self.possibleDirections:
                print("Not a valid direction")
            else:
                print(f'Cannot build {directionToBuild}')
            directionToBuild = input("Select direction to build\n")
        return directionToBuild

    def selectMove(self, currBoard):
        self.getWorker()
        moveDir = self.getMove(currBoard)
        buildDir = self.getBuild(currBoard, moveDir)
        return Move(self.selectedWorker, moveDir, buildDir, currBoard)
    
    def playMove(self, currBoard):
        super().playMove(currBoard)

