from typing import List
from player import Player
from move import Move
import random

class HeuristicPlayer(Player):
    def __init__(self, color: str):
        super().__init__("heuristic", color)

    def selectMove(self, currBoardState):
        validMoves = self.generateValidMoves(currBoardState)
        bestMove = self.pickBestMove(validMoves)
        return bestMove
    
    def playMove(self, currBoardState):
        super().playMove(currBoardState)

    def generateValidMoves(self, currBoardState):
        def computeMoveScore(height, center, distance):
            if height == 3:
                return float('inf')
            return (3 * height) + (2 * center) + (distance)
        moveCandidates = []
        currentPlayer = currBoardState.current_player
        opponent = currBoardState.players[1] if (currBoardState.current_player == currBoardState.players[0]) else currBoardState.players[0]
        validMoves = self.selectedWorker.findAllMoves(currBoardState)
        for moveDirection in validMoves:
            # create move object and position associated with it
            newMove = Move(self.selectedWorker, moveDirection, "n", currBoardState)
            changeX, changeY = newMove.moveOperation[0], newMove.moveOperation[1]
            newMove.endPosition = [newMove.startPosition[0] + changeX, newMove.startPosition[1] + changeY]
            # compute height, distance, and center scores
            heightScore = self.computeHeightScore(currBoardState, newMove.endPosition)
            centerScore = self.computeCenterScore(currBoardState, newMove.endPosition)
            distanceScore = self.computeDistanceScore(currentPlayer, opponent, newMove.endPosition)
            # get move score
            newMoveScore = computeMoveScore(heightScore, centerScore, distanceScore)
            # add move candidate to list of moves
            moveCandidate = (newMoveScore, newMove)
            moveCandidates.append(moveCandidate)
        return moveCandidates
    
    def pickBestMove(self, possibleMoves: List[(float, Move)]):
        def breakTies(tiedMoves):
            if tiedMoves:
                return random.choice(tiedMoves)
            else:
                return None
        ties = []
        possibleMoves.sort(key=self.calculateMoveScore, reverse=True)
        bestMoveScore = possibleMoves[0][0]
        for move in possibleMoves:
            if move[0] == bestMoveScore:
                ties.append(move)
        return breakTies(ties)[1]

    def computeHeightScore(self, currBoardState, position):
        def getHeightScore(currBoardState, position):
            x, y = position[0], position[1]
            square = currBoardState.getSquare([x, y])
            return square.level
        # sum of the heights of the buildings a player's workers
        movedWorkerHeight = getHeightScore(currBoardState, position)
        otherWorker = self.possibleWorkers[0] if self.selectedWorker == self.possibleWorkers[1] else self.possibleWorkers[1]
        otherWorkerHeight = otherWorker.getHeightScore(currBoardState, position)
        return movedWorkerHeight + otherWorkerHeight

    def computeCenterScore(self, currBoardState, position):
        def getCenterScore(position):
            x, y = position[0], position[1]
            if x == 0 or x == 4 or y == 0 or y == 4:
                return 2
            elif x == 1 or x == 3 or y == 1 or y == 3:
                return 1
            else:
                return 0
        movedWorkerCenter = getCenterScore(currBoardState, position)
        otherWorker = self.possibleWorkers[0] if self.selectedWorker == self.possibleWorkers[1] else self.possibleWorkers[1]
        otherWorkerCenter = otherWorker.getCenterScore(currBoardState, position)
        return movedWorkerCenter + otherWorkerCenter

    def computeDistanceScore(self, currBoardState, currentPlayer, opponent, newMoveEndPosition):
        def distancePlayerToOpponent(currentPlayerPositions, opponentPositions):
            def getDistanceBetweenPlayers(worker1Position, worker2Position):
                x1, y1 = worker1Position[0], worker1Position[1]
                x2, y2 = worker2Position[0], worker2Position[1]
                 # distance between two workers
                return max(abs(x1 - x2), abs(y1 - y2))
            # compute min distances between currentPlayer's workers and Opponents workers
            distOpp1 = min(getDistanceBetweenPlayers(opponentPositions[0], currentPlayerPositions[0]), getDistanceBetweenPlayers(opponentPositions[0], currentPlayerPositions[0]))
            distOpp2 = min(getDistanceBetweenPlayers(opponentPositions[1], currentPlayerPositions[0]), getDistanceBetweenPlayers(opponentPositions[1], currentPlayerPositions[0]))
            return distOpp1 + distOpp2
        # get current Player and opponent 
        currentPlayer = currBoardState.current_player
        opponent = currBoardState.players[1] if (currBoardState.current_player == currBoardState.players[0]) else currBoardState.players[0]
        # get the moved worker for the current player
        currentPlayerMovedWorkerPosition = newMoveEndPosition
        # get the other worker for the current player
        currentPlayerOtherWorker = self.possibleWorkers[0] if self.selectedWorker == self.possibleWorkers[1] else self.possibleWorkers[1]
        # get positions of both workers of the current player
        currentPlayerOtherWorkerPosition = currentPlayerOtherWorker.position
        currentPlayerPositions = [currentPlayerMovedWorkerPosition, currentPlayerOtherWorkerPosition]
        # get the positions of the opponent's workers
        opponentPositions = [opponent.workers[0].position, opponent.workers[1].position]
        # compute distance score
        distanceScore = distancePlayerToOpponent(currentPlayerPositions, opponentPositions)
        return distanceScore

    def printCurrentScore(self):
        print(f"{self.heightScore}, {self.centerScore}, {self.distanceScore}")