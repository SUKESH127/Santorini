
class Board:
    def __init__(self, players):
        self.row = None
        self.cols = None
        self.board = []
        self.players = players
        self.current_player = players[0]
        self.whiteWorkers = []
        self.blueWorkers = []
        self.initialize_board()

    def initialize_board(self):
        self.board = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append(Square())
            self.board.append(row)
        
        # assign player 1's workers
        self.board[3][1].assign_worker('A')
        self.board[1][3].assign_worker('B')

        # assign player 2's workers
        self.board[1][1].assign_worker('Y')
        self.board[3][3].assign_worker('Z')

    def moveWorker(self, worker, row, col):
        # if worker in self.whiteWorkers:
        #     self.whiteWorkers.remove(worker)
        # elif worker in self.blueWorkers:
        #     self.blueWorkers.remove(worker)
        # self.board[row][col].assign_worker(worker)
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
        self._level = 0
        self._worker = ' '
        self.row = None
        self.cols = None
    
    def has_worker(self):
        if self._worker == ' ':
            return False
        return True
    
    def assign_worker(self, w):
        self._worker = w
    
    def can_build(self):
        return self._level != 4   

    def build(self):
        self._level += 1
    
    def __str__(self):
        return f'{self._level}{self._worker}'
