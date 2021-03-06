
class BoardState:
    def __init__(self, players):
        self.board = []
        self.players = players
        self.initialize_boardState()
        self.turnNumber = 1
        self.currentPlayer = self.players[0]

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

    def checkGameOver(self):
        for p in self.players:
            if p.w1.getHeightScore(self) == 3 or p.w2.getHeightScore(self) == 3:
                print(f'{p.color} has won')
                return True
        if not self.currentPlayer.hasMoves(self):
            otherPlayer = self.players[0] if self.currentPlayer == self.players[1] else self.players[1]
            print(f'{otherPlayer.color} has won')
            return True
        return False
    
    def printBoardState(self, enableScore):
        print("+--+--+--+--+--+")
        for i in range(5):
            for j in range(5):
                print(f'|{self.getSquare([j, i])}', end='')
            print("|\n+--+--+--+--+--+")
        turnString = f'Turn: {self.turnNumber}, {self.currentPlayer.color} ({self.currentPlayer.w1.name}{self.currentPlayer.w2.name})'
        if enableScore:
            turnString += self.currentPlayer.getCurrentScore(self)
        print(turnString)

    def switchPlayer(self):
        self.turnNumber += 1
        if self.currentPlayer == self.players[0]:
            self.currentPlayer = self.players[1]
        else:
            self.currentPlayer = self.players[0]

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
