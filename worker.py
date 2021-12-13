from typing import List

class Worker:
    def __init__(self, color: str, position: List):
        self.position = position
        self.color = color
        self.moves = []

    def validMove(self, board, intendedMove: List[int]):
        startX, startY = self.position[0], self.position[1]
        endX, endY = startX + intendedMove[0], startY + intendedMove[1]
        if endX < 0 or endX > 4 or endY < 0 or endY > 4:
            return False
        if board.getSquare(endX, endY).hasWorker():
            return False
        if board.getSquare(endX, endY).level > 1 + board.getSquare(startX, startY).level:
            return False
        if board.getSquare(endX, endY).canBuild():
            return True
        return False

    def findAllMoves(self, board):
        cardinal_directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        numerical_directions = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        validCardinalMoves = []
        for i in range(len(cardinal_directions)):
            if self.validMove(board, numerical_directions[i]):
                validCardinalMoves.append(cardinal_directions[i])
        return validCardinalMoves
    
    def validBuild(self, board, intendedMove: List[int]):
        startX, startY = self.position[0], self.position[1]
        endX, endY = startX + intendedMove[0], startY + intendedMove[1]
        if endX < 0 or endX > 4 or endY < 0 or endY > 4:
            return False
        if board.getSquare(endX, endY).hasWorker():
            return False
        if board.getSquare(endX, endY).canBuild():
            return True
        return False

    def findAllBuilds(self, board):
        cardinal_directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        numerical_directions = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        validCardinalBuilds = []
        for i in range(len(cardinal_directions)):
            if self.validBuild(board, numerical_directions[i]):
                validCardinalBuilds.append(cardinal_directions[i])
        return validCardinalBuilds
