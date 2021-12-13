from player import Player
import random

class HeuristicPlayer(Player):
    def __init__(self, color: str):
        super().__init__("heuristic", color)   
        self.heightScore
        self.centerScore
        self.distanceScore

    def selectMove(self):
        pass

    def computeHeightScore(self):
        pass

    def pickBestMove(self, possibleMoves):
        ties = []
        possibleMoves.sort(key=self.calculateMoveScore, reverse=True)
        bestMove = possibleMoves[0]
        for move in possibleMoves:
            if move.score == bestMove.score: # .score fix
                ties.append(move)
        return self.breakTies(ties)

    def breakTies(self, tiedMoves):
        return random.choice(tiedMoves)

    def calculateMoveScore(self):
        return (3 * self.heightScore) + (2 * self.centerScore) + (self.distanceScore)

    def printCurrentScore(self):
        print(f"{self.heightScore}, {self.centerScore}, {self.distanceScore}")