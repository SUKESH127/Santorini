
class Board:
    def __init__(self, players):
        self.board = []
        self.players = players
        self.current_player = players[0]
        self.initialize_board()

    def initialize_board(self):
        self.board = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append(Square())
            self.board.append(row)
        
        # assign white player's workers
        self.board[3][1].assignworker('A')
        self.board[1][3].assignworker('B')

        # assign blue player's workers
        self.board[1][1].assignworker('Y')
        self.board[3][3].assignworker('Z')

    def moveWorker(self, worker, row, col):
        # if worker in self.whiteWorkers:
        #     self.whiteWorkers.remove(worker)
        # elif worker in self.blueWorkers:
        #     self.blueWorkers.remove(worker)
        # self.board[row][col].assignworker(worker)
        pass

    def updateBoard(self):
        pass

    def switchPlayer(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def checkGameOver(self):
        return False

    def printScore(self):
        #print(f'Player 1: {self.players[0].score}')
        print("score")
    
    def printBoard(self):
        print("+--+--+--+--+--+")
        for i in range(5):
            for j in range(5):
                print(f'|{self.board[i][j]}', end='')
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
