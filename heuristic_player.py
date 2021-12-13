from player import Player
from move import Move
import random

class HeuristicPlayer(Player):
    def __init__(self, color: str):
        super().__init__("heuristic", color)

    def selectMove(self, currBoardState):
        validMoves = self.generateValidMoves(currBoardState)
        if not validMoves:
            return None
        
        bestMove = self.pickBestMove(validMoves)
        moveScore, moveDir, self.selectedWorker = bestMove[0], bestMove[1], bestMove[2]
        buildDir = self.getBuild(currBoardState, moveDir)
        return Move(self.selectedWorker, moveDir, buildDir, currBoardState)
    
    def getBuild(self, boardState, moveDir):
        validBuilds = self.selectedWorker.findAllBuilds(boardState, moveDir)
        directionToBuild = random.choice(validBuilds)
        return directionToBuild
    
    def playMove(self, currBoardState):
        super().playMove(currBoardState)

    def generateValidMoves(self, currBoardState):
        moveCandidates = []
        currentPlayer = currBoardState.current_player
        opponent = currBoardState.players[1] if (currBoardState.current_player == currBoardState.players[0]) else currBoardState.players[0]
        # get all moves for current player's workers
        workers = [currentPlayer.w1, currentPlayer.w2]
        for w in workers:
            validMoves = w.findAllMoves(currBoardState)
            for moveDirection in validMoves:
                moveValue = self.convertCardinalDirection(moveDirection)
                finalX = w.position[0] + moveValue[0]
                finalY = w.position[1] + moveValue[1]
                finalPosition = [finalX, finalY]
                # compute move score
                totalMoveScore = self.computeMoveScore(currBoardState, finalPosition, currentPlayer, opponent)
                # add move candidate to list of moves
                moveCandidate = (newMoveScore, moveDirection, w)
                moveCandidates.append(moveCandidate)
        return moveCandidates
    
    def computeMoveScore(boardState, position, currentPlayer, opponent):
        height = self.computeHeightScore(boardState, position)
        center = self.computeCenterScore(boardState, position)
        distance = self.computeDistanceScore(currentPlayer, opponent, position)
        if height == 3:
                return float('inf')
        return (3 * height) + (2 * center) + (distance)

    def pickBestMove(self, possibleMoves):
        ties = []
        possibleMoves.sort(reverse=True)
        bestMoveScore = possibleMoves[0][0]
        for move in possibleMoves:
            if move[0] == bestMoveScore:
                ties.append(move)

        return random.choice(ties)

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
    
    def convertCardinalDirection(self, direction):
        convertedDirection = [0, 0]
        if direction == 'n':
            convertedDirection = [0, -1]
        elif direction == 's':
            convertedDirection = [0, 1]
        elif direction == 'e':
            convertedDirection = [1, 0]
        elif direction == 'w':
            convertedDirection = [-1, 0]
        elif direction == 'ne':
            convertedDirection = [1, -1]
        elif direction == 'nw':
            convertedDirection = [-1, -1]
        elif direction == 'se':
            convertedDirection = [1, 1]
        elif direction == 'sw':
            convertedDirection = [-1, 1]
        return convertedDirection