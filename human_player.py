from move import Move
from board_state import BoardState
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


    def getMove(self, boardState):
        validMoves = self.selectedWorker.findAllMoves(boardState)
        directionToMove = input("Select direction to move\n")
        while directionToMove not in validMoves:
            if directionToMove not in self.possibleDirections:
                print("Not a valid direction")
            else:
                print(f'Cannot move {directionToMove}')
            directionToMove = input("Select direction to move\n")
        return directionToMove

    def getBuild(self, boardState, moveDir):
        validBuilds = self.selectedWorker.findAllBuilds(boardState, moveDir)
        directionToBuild = input("Select direction to build\n")
        while directionToBuild not in validBuilds:
            if directionToBuild not in self.possibleDirections:
                print("Not a valid direction")
            else:
                print(f'Cannot build {directionToBuild}')
            directionToBuild = input("Select direction to build\n")
        return directionToBuild

    def selectMove(self, boardState):
        self.getWorker()
        moveDir = self.getMove(boardState)
        buildDir = self.getBuild(boardState, moveDir)
        return Move(self.selectedWorker, moveDir, buildDir, boardState)
    
    def playMove(self, boardState):
        return super().playMove(boardState)
    
    def getCurrentScore(self, boardState):
        return super().getCurrentScore(boardState)

