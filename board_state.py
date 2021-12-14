
class BoardState:
    def __init__(self, players, template):
        self.board = []
        self.players = players
        self.currentPlayer = players[0]
        self.initialize_boardState(template)

    def initialize_boardState(self, template):
        self.board = []
        for i in range(5):
            row = []
            for j in range(5):
                s = Square()
                if template is not None:
                    s.level = template.board[i][j].level
                row.append(s)
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
        for worker in self.currentPlayer.possibleWorkers:
            workerData = (worker.name, worker.position)
            positions.append(workerData)
        return positions

    def moveWorker(self, worker, row, col):
        pass

    def updateBoard(self):
        pass

    def switchPlayer(self):
        self.currentPlayer = self.players[1] if self.currentPlayer == self.players[0] else self.players[0]

    def checkGameOver(self):
        w1 = self.currentPlayer.w1
        w2 = self.currentPlayer.w2
        if w1.getHeightScore(self) == 3 or w2.getHeightScore(self) == 3:
            print(f'{self.currentPlayer.color} has won')
            return True
        return False

    def printScore(self, currentPlayer):
        if currentPlayer.playerType == "heuristic":
            currentPlayer.printCurrentScore()
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
