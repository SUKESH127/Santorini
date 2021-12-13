from player import Player
from move import Move
import random

class Random(Player):
    def __init__(self, color: str):
        super().__init__(self, "random", color)   

    def selectMove(self):
        moveDir = self.getMoveAndWorker(self.board)
        worker = self.selectedWorker
        buildDir = self.getBuild(self.board)
        print(f"{worker.name},{moveDir},{buildDir}")
        return Move(worker, moveDir, buildDir)
        
    def getMoveAndWorker(self, board):
        validMoves = []
        for worker in {self.w1, self.w2}:
            for direction in worker.findAllMoves(board):
                validChoice = (worker, direction)
                validMoves.append(validChoice)
        randomMoveChoice = random.choice(validMoves)
        self.selectedWorker = randomMoveChoice[0]
        return randomMoveChoice[1]

    def getBuild(self, board):
        validBuilds = self.selectedWorker.findAllBuilds(board)
        directionToBuild = random.choice(validBuilds)
        return directionToBuild