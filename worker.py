
class Worker:
    def __init__(self, color, position):
        self.position = position
        self.color = color
        self.moves = []

    def validMove(self, board, direction):
        x = self.position[0] + direction[0]
        y = self.position[1] + direction[1]
        if x < 0 or x > 4 or y < 0 or y > 4:
            return False
        if board.board[x][y].hasWorker():
            return False
        if board.board[x][y].canBuild():
            return True
        return False

    def findAllMoves(self, board):
        cardinal_directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        numerical_directions = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        validCardinalMoves = []
        for i in range(len(cardinal_directions)):
            if (self.validMove, board, numerical_directions[i]):
                validCardinalMoves.append(cardinal_directions[i])
        return validCardinalMoves
