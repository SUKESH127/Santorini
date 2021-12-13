from player import Player
from move import Move
import random

class Random(Player):
    def __init__(self, color: str):
        super().__init__(self, "random", color)   

    def selectMove(self):
        moveDir = self.getMoveAndWorker(self.board)
        worker = self.selectedWorker
        buildDir = self.getBuild(self.board, moveDir[1])
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