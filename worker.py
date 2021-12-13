from typing import List

class Worker:
    def __init__(self, color: str, position: List, name: str):
        self.position = position
        self.color = color
        self.name = name

    def validMove(self, board, intendedMove: List[int]):
        startX, startY = self.position[0], self.position[1]
        endX, endY = startX + intendedMove[0], startY + intendedMove[1]
        startSquare = board.getSquare([startX, startY])
        endSquare = board.getSquare([endX, endY])
        if endX < 0 or endX > 4 or endY < 0 or endY > 4:
            return False
        if endSquare.hasWorker():
            return False
        if endSquare.level > 1 + startSquare.level:
            return False
        if endSquare.canBuild():
            return True
        return False
        
    
    def findAllMoves(self, board):
        cardinal_dirs = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        validMoves = []
        for i in range(len(cardinal_dirs)):
            if self.validMove(board, self.convertCardinalDirection(cardinal_dirs[i])):
                validMoves.append(cardinal_dirs[i])
        return validMoves
    
    def validBuild(self, board, intendedMove: List[int], intendedBuild: List[int]):
        startX, startY = self.position[0], self.position[1]
        targetX = startX + intendedMove[0] + intendedBuild[0]
        targetY = startY + intendedMove[1] + intendedBuild[1]
        targetSquare = board.getSquare([targetX, targetY])
        if targetX < 0 or targetX > 4 or targetY < 0 or targetY > 4:
            return False
        if targetSquare.hasWorker() and targetSquare.worker != self.name:
            return False
        if targetSquare.canBuild():
            return True
        return False

    def findAllBuilds(self, board, moveDir):
        cardinal_dirs = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        validCardinalBuilds = []
        for i in range(len(cardinal_dirs)):
            if self.validBuild(board, self.convertCardinalDirection(moveDir), self.convertCardinalDirection(cardinal_dirs[i])):
                validCardinalBuilds.append(cardinal_dirs[i])
        return validCardinalBuilds
    
    def convertCardinalDirection(self, direction):
        convertedDirection = [0, 0]
        if direction == 'n':
            convertedDirection = [0, -1]
        elif direction == 's':
            convertedDirection = [0, 1]
        elif direction == 'e':
            convertedDirection = [1, 0]
        elif direction == 'w':
            convertedDirection = [-1, 0]
        elif direction == 'ne':
            convertedDirection = [1, -1]
        elif direction == 'nw':
            convertedDirection = [-1, -1]
        elif direction == 'se':
            convertedDirection = [1, 1]
        elif direction == 'sw':
            convertedDirection = [-1, 1]
        return convertedDirection
