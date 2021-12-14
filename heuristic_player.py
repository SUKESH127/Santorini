from player import Player
from move import Move
import random

class HeuristicPlayer(Player):
    def __init__(self, color: str):
        super().__init__("heuristic", color)

    def selectMove(self, boardState):
        validMoves = self.generateValidMoves(boardState)
        if not validMoves:
            return None
        
        bestMove = self.pickBestMove(validMoves)
        moveScore, moveDir, self.selectedWorker = bestMove[0], bestMove[1], bestMove[2]
        buildDir = self.getBuild(boardState, moveDir)
        return Move(self.selectedWorker, moveDir, buildDir, boardState)
    
    def getBuild(self, boardState, moveDir):
        validBuilds = self.selectedWorker.findAllBuilds(boardState, moveDir)
        directionToBuild = random.choice(validBuilds)
        return directionToBuild

    def generateValidMoves(self, boardState):
        moveCandidates = []
        opponent = boardState.players[1] if (self == boardState.players[0]) else boardState.players[0]
        # get all moves for current player's workers
        workers = [self.w1, self.w2]
        for w in workers:
            validMoves = w.findAllMoves(boardState)
            for moveDirection in validMoves:
                moveValue = self.convertCardinalDirection(moveDirection)
                finalX = w.position[0] + moveValue[0]
                finalY = w.position[1] + moveValue[1]
                finalPosition = [finalX, finalY]
                # compute move score
                totalMoveScore = self.computeMoveScore(boardState, w, finalPosition, opponent)
                # add move candidate to list of moves
                moveCandidate = (totalMoveScore, moveDirection, w)
                moveCandidates.append(moveCandidate)
        return moveCandidates
    
    def computeMoveScore(self, boardState, currentWorker, position, opponent):
        self.selectedWorker = currentWorker
        height = self.computeHeightScore(boardState, position)
        center = self.computeCenterScore(boardState, position)
        distance = self.computeDistanceScore(boardState, opponent, position)
        if height == 3:
                return float('inf')
        return (3 * height) + (2 * center) + (distance)

    def pickBestMove(self, possibleMoves):
        ties = []
        possibleMoves.sort(key=lambda y: y[0], reverse=True)
        bestMoveScore = possibleMoves[0][0]
        for move in possibleMoves:
            if move[0] == bestMoveScore:
                ties.append(move)

        return random.choice(ties)

    def computeHeightScore(self, boardState, position):
        def getSquareHeight(boardState, position):
            return boardState.getSquare(position).level

        # sum of the heights of the buildings a player's workers
        movedWorkerHeight = getSquareHeight(boardState, position)
        otherWorker = self.w1 if self.selectedWorker == self.w2 else self.w1
        otherWorkerHeight = getSquareHeight(boardState, otherWorker.position)
        return movedWorkerHeight + otherWorkerHeight

    def computeCenterScore(self, boardState, position):
        def getCenterScore(boardState, position):
            x, y = position[0], position[1]
            if x == 0 or x == 4 or y == 0 or y == 4:
                return 0
            elif x == 1 or x == 3 or y == 1 or y == 3:
                return 1
            else:
                return 2

        movedWorkerCenter = getCenterScore(boardState, position)
        otherWorker = self.w1 if self.selectedWorker == self.w2 else self.w1
        otherWorkerCenter = getCenterScore(boardState, otherWorker.position)
        return movedWorkerCenter + otherWorkerCenter

    def computeDistanceScore(self, boardState, opponent, newMoveEndPosition):
        def distancePlayerToOpponent(currentPlayerPositions, opponentPositions):
            def getDistanceBetweenPlayers(worker1Position, worker2Position):
                x1, y1 = worker1Position[0], worker1Position[1]
                x2, y2 = worker2Position[0], worker2Position[1]
                 # distance between two workers
                return max(abs(x1 - x2), abs(y1 - y2))

            # compute min distances between currentPlayer's workers and Opponents workers
            distOpp1 = min(getDistanceBetweenPlayers(opponentPositions[0], currentPlayerPositions[0]), getDistanceBetweenPlayers(opponentPositions[0], currentPlayerPositions[0]))
            distOpp2 = min(getDistanceBetweenPlayers(opponentPositions[1], currentPlayerPositions[0]), getDistanceBetweenPlayers(opponentPositions[1], currentPlayerPositions[0]))
            return 8 - (distOpp1 + distOpp2)

        # get current Player and opponent 
        opponent = boardState.players[1] if (self == boardState.players[0]) else boardState.players[0]
        # get the moved worker for the current player
        currentPlayerMovedWorkerPosition = newMoveEndPosition
        # get the other worker for the current player
        currentPlayerOtherWorker = self.w2 if self.selectedWorker == self.w1 else self.w1
        # get positions of both workers of the current player
        currentPlayerOtherWorkerPosition = currentPlayerOtherWorker.position
        currentPlayerPositions = [currentPlayerMovedWorkerPosition, currentPlayerOtherWorkerPosition]
        # get the positions of the opponent's workers
        opponentPositions = [opponent.w1.position, opponent.w2.position]
        # compute distance score
        distanceScore = distancePlayerToOpponent(currentPlayerPositions, opponentPositions)
        return distanceScore
    
    def playMove(self, boardState):
        return super().playMove(boardState)
    
    def getCurrentScore(self, boardState):
        return super().getCurrentScore(boardState)
    
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