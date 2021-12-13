
class BoardState:
    def __init__(self, players):
        self.board = []
        self.players = players
        self.current_player = players[0]
        self.initialize_boardState()

    def initialize_boardState(self):
        self.board = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append(Square())
            self.board.append(row)
        
        # assign both players' workers
        workers = [self.players[0].w1, self.players[0].w2, self.players[1].w1, self.players[1].w2]
        for w in workers:
            self.getSquare(w.position).assignWorker(w.name)
    
    def getSquare(self, position):
        x, y = position[0], position[1]
        return self.board[y][x]

    def getWorkerPositions(self):
        positions = []
        for worker in self.current_player.possibleWorkers:
            workerData = (worker.name, worker.position)
            positions.append(workerData)
        return positions

    def moveWorker(self, worker, row, col):
        pass

    def updateBoard(self):
        pass

    def switchPlayer(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def checkGameOver(self):
        w1 = self.current_player.w1
        w2 = self.current_player.w2
        if w1.getHeightScore(self) == 3 or w2.getHeightScore(self) == 3:
            print(f'{self.current_player.color} has won')
            return True
        return False

    def printScore(self, current_player):
        if current_player.playerType == "heuristic":
            current_player.printCurrentScore()
        else:
            return
    
    def printBoardState(self):
        print("+--+--+--+--+--+")
        for i in range(5):
            for j in range(5):
                print(f'|{self.getSquare([j, i])}', end='')
            print("|\n+--+--+--+--+--+")

class Square:
    def __init__(self):
        self.level = 0
        self.worker = ' '
        self.row = None
        self.cols = None
    
    def hasWorker(self):
        if self.worker == ' ':
            return False
        return True
    
    def assignWorker(self, w):
        self.worker = w

    def removeWorker(self):
        self.worker = ' '
    
    def canBuild(self):
        return self.level != 4   

    def build(self):
        self.level += 1
    
    def __str__(self):
        return f'{self.level}{self.worker}'
