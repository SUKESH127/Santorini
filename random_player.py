from player import Player
from move import Move
import random

class RandomPlayer(Player):
    def __init__(self, color: str):
        super().__init__("random", color)   

    def selectMove(self, currBoardState):
        moveDir = self.getMoveAndWorker(currBoardState)
        if not moveDir:
            # no valid moves, this player loses
            return None
        worker = self.selectedWorker
        buildDir = self.getBuild(currBoardState, moveDir)
        print(f"{worker.name},{moveDir},{buildDir}")
        return Move(worker, moveDir, buildDir, currBoardState)
        
    def getMoveAndWorker(self, boardState):
        validMoves = []
        for worker in {self.w1, self.w2}:
            for direction in worker.findAllMoves(boardState):
                validChoice = (worker, direction)
                validMoves.append(validChoice)
        if not validMoves:
            # no valid moves, this player loses
            return None
        randomMoveChoice = random.choice(validMoves)
        self.selectedWorker = randomMoveChoice[0]
        return randomMoveChoice[1]

    def getBuild(self, boardState, moveDir):
        validBuilds = self.selectedWorker.findAllBuilds(boardState, moveDir)
        directionToBuild = random.choice(validBuilds)
        return directionToBuild

    def playMove(self, currBoardState):
        super().playMove(currBoardState)
    
    def getCurrentScore(self, currBoardState):
        super().getCurrentScore(currBoardState)