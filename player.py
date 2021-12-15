
from move import Move
from worker import Worker

class Player:

    def __init__(self, playerType, color: str):
        self.playerType = playerType
        self.color = color
        if color == "white":
            self.w1 = Worker(self.color, [1, 3], "A")
            self.w2 = Worker(self.color, [3, 1], "B")
        else:
            self.w1 = Worker(self.color, [1, 1], "Y")
            self.w2 = Worker(self.color, [3, 3], "Z")
        self.selectedWorker = None
        self.possibleWorkers = ["A", "B"] if color == "white" else ["Y", "Z"]
        self.possibleDirections = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        self.heightScore = 0
        self.centerScore = 0
        self.distanceScore = 0
    
    def hasMoves(self, boardState):
        return self.w1.hasMoves(boardState) or self.w2.hasMoves(boardState)
        
    def playMove(self, boardState):
        m = self.selectMove(boardState)
        if not m:
            # no valid moves, this player loses
            return False
        m.execute()
        boardState.switchPlayer()
        return True

    def selectMove(self, boardState):
        return None
    
    def getTotalHeightScore(self, boardState):
        def getHeightScore(boardState, position):
            square = boardState.getSquare(position)
            return square.level

        # sum of the heights of the buildings a player's workers
        w1Position = self.w1.position
        w2Position = self.w2.position
        w1Height = getHeightScore(boardState, w1Position)
        w2Height = getHeightScore(boardState, w2Position)
        self.heightScore = w1Height + w2Height

    def getTotalCenterScore(self, boardState):
        def getCenterScore(position):
            x, y = position[0], position[1]
            if x == 0 or x == 4 or y == 0 or y == 4:
                return 0
            elif x == 1 or x == 3 or y == 1 or y == 3:
                return 1
            else:
                return 2
        # sum of the centers of the buildings a player's workers
        w1Position = self.w1.position
        w2Position = self.w2.position
        w1Center = getCenterScore(w1Position)
        w2Center = getCenterScore(w2Position)
        self.centerScore = w1Center + w2Center

    def getTotalDistanceScore(self, boardState):
        def distancePlayerToOpponent(currentPlayerPositions, opponentPositions):            
            def getDistanceBetweenPlayers(worker1Position, worker2Position):
                x1, y1 = worker1Position[0], worker1Position[1]
                x2, y2 = worker2Position[0], worker2Position[1]
                 # distance between two workers
                return max(abs(x1 - x2), abs(y1 - y2))
            distOpp1 = min(getDistanceBetweenPlayers(currentPlayerPositions[1], opponentPositions[0]), 
                            getDistanceBetweenPlayers(currentPlayerPositions[0], opponentPositions[0]))
            
            distOpp2 = min(getDistanceBetweenPlayers(currentPlayerPositions[1], opponentPositions[1]), 
                            getDistanceBetweenPlayers(currentPlayerPositions[0], opponentPositions[1]))
            return 8 - (distOpp1 + distOpp2)

        currentPlayerPositions = [self.w1.position, self.w2.position] # [[x, y], [x, y]]
        opponent = boardState.players[1] if (self == boardState.players[0]) else boardState.players[0]
        opponentPositions = [opponent.w1.position, opponent.w2.position] # [[x, y], [x, y]]
        self.distanceScore = distancePlayerToOpponent(currentPlayerPositions, opponentPositions)

    def getCurrentScore(self, boardState):
        self.getTotalHeightScore(boardState)
        self.getTotalCenterScore(boardState)
        self.getTotalDistanceScore(boardState)
        return f", ({self.heightScore}, {self.centerScore}, {self.distanceScore})"