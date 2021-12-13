from player import Player
from move import Move
import random

class RandomPlayer(Player):
    def __init__(self, color: str):
        super().__init__("random", color)   

    def selectMove(self, currBoard):
        moveDir = self.getMoveAndWorker(currBoard)
        worker = self.selectedWorker
        buildDir = self.getBuild(currBoard, moveDir)
        print(f"{worker.name},{moveDir[0]},{buildDir}")
        return Move(worker, moveDir[0], buildDir)
        
    def getMoveAndWorker(self, board):
        validMoves = []
        for worker in {self.w1, self.w2}:
            for direction in worker.findAllMoves(board):
                validChoice = (worker, direction)
                validMoves.append(validChoice)
        randomMoveChoice = random.choice(validMoves)
        self.selectedWorker = randomMoveChoice[0]
        return randomMoveChoice[1]

    def getBuild(self, board, moveDir):
        validBuilds = self.selectedWorker.findAllBuilds(board, moveDir)
        directionToBuild = random.choice(validBuilds)
        return directionToBuild
    
    def playMove(self, currBoard):
        super().playMove(currBoard)