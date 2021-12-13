from typing import List

class Worker:
    def __init__(self, color: str, position: List, name: str):
        self.position = position
        self.color = color
        self.name = name

    def validMove(self, board, intendedMove: List[int]):
        startX, startY = self.position[0], self.position[1]
        endX, endY = startX + intendedMove[0], startY + intendedMove[1]
        if endX < 0 or endX > 4 or endY < 0 or endY > 4:
            return False
        if board.getSquare([endX, endY]).hasWorker():
            return False
        if board.getSquare([endX, endY]).level > 1 + board.getSquare([startX, startY]).level:
            return False
        if board.getSquare([endX, endY]).canBuild():
            return True
        return False

    def findAllMoves(self, board):
        cardinal_directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        numerical_directions = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        validMoves = []
        for i in range(len(cardinal_directions)):
            if self.validMove(board, numerical_directions[i]):
                validMoves.append([cardinal_directions[i], numerical_directions[i]])
        return validMoves
    
    def validBuild(self, board, intendedMove: List[int], intendedBuild: List[int]):
        startX, startY = self.position[0], self.position[1]
        endX = startX + intendedMove[0] + intendedBuild[0]
        endY = startY + intendedMove[1] + intendedBuild[1]
        if endX < 0 or endX > 4 or endY < 0 or endY > 4:
            return False
        if board.getSquare([endX, endY]).hasWorker():
            return False
        if board.getSquare([endX, endY]).canBuild():
            return True
        return False

    def findAllBuilds(self, board, moveDir):
        cardinal_directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        numerical_directions = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        validCardinalBuilds = []
        for i in range(len(cardinal_directions)):
            if self.validBuild(board, moveDir, numerical_directions[i]):
                validCardinalBuilds.append(cardinal_directions[i])
        return validCardinalBuilds
