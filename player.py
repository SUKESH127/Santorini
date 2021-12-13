
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
        
    def playMove(self, currBoardState):
        m = self.selectMove(currBoardState)
        if not m:
            # no valid moves, this player loses
            return False
        m.execute()
        return True

    def selectMove(self, currBoard):
        return None
    
    def getTotalHeightScore(self, currBoardState):
        def getHeightScore(currBoardState, position):
            square = currBoardState.getSquare(position)
            return square.level

        # sum of the heights of the buildings a player's workers
        w1Position = self.w1.position
        w2Position = self.w2.position
        w1Height = getHeightScore(currBoardState, w1Position)
        w2Height = getHeightScore(currBoardState, w2Position)
        self.heightScore = w1Height + w2Height

    def getTotalCenterScore(self, currBoardState):
        def getCenterScore(position):
            x, y = position[0], position[1]
            if x == 0 or x == 4 or y == 0 or y == 4:
                return 2
            elif x == 1 or x == 3 or y == 1 or y == 3:
                return 1
            else:
                return 0
        # sum of the centers of the buildings a player's workers
        w1Position = self.w1.position
        w2Position = self.w2.position
        w1Center = getCenterScore(w1Position)
        w2Center = getCenterScore(w2Position)
        self.centerScore = w1Center + w2Center

    def getTotalDistanceScore(self, currBoardState):
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

        # get current Player positions 
        currentPlayerPositions = [self.w1.position, self.w2.position]
        # get opponent positions
        opponent = currBoardState.players[1] if (currBoardState.current_player == currBoardState.players[0]) else currBoardState.players[0]
        # get the positions of the opponent's workers
        opponentPositions = [opponent.w1.position, opponent.w2.position]
        # compute distance score
        self.distanceScore = distancePlayerToOpponent(currentPlayerPositions, opponentPositions)

    def getCurrentScore(self, currBoardState):
        self.getTotalHeightScore(currBoardState)
        self.getTotalCenterScore(currBoardState)
        self.getTotalDistanceScore(currBoardState)
        #print("height: ", self.heightScore, "center: ", self.centerScore, "distance: ", self.distanceScore)
        return f", ({self.heightScore}, {self.centerScore}, {self.distanceScore})"