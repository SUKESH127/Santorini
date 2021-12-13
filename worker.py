from typing import List

class Worker:
    def __init__(self, color: str, position: List, name: str):
        self.position = position
        self.color = color
        self.name = name

    def getHeightScore(self, boardState):
        x, y = self.position[0], self.position[1]
        startSquare = boardState.getSquare([x, y])
        return startSquare.level

    def getCenterScore(self, boardState):
        x, y = self.position[0], self.position[1]
        if x == 0 or x == 4 or y == 0 or y == 4:
            return 2
        elif x == 1 or x == 3 or y == 1 or y == 3:
            return 1
        else:
            return 0

    def validMove(self, boardState, intendedMove: List[int]):
        startX, startY = self.position[0], self.position[1]
        endX, endY = startX + intendedMove[0], startY + intendedMove[1]
        startSquare = boardState.getSquare([startX, startY])
        if endX < 0 or endX > 4 or endY < 0 or endY > 4:
            return False

        endSquare = boardState.getSquare([endX, endY])
        if endSquare.hasWorker():
            return False
        elif endSquare.level > 1 + startSquare.level:
            return False
        elif endSquare.canBuild():
            return True
        return False
        
    
    def findAllMoves(self, boardState):
        cardinal_dirs = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        validMoves = []
        for i in range(len(cardinal_dirs)):
            if self.validMove(boardState, self.convertCardinalDirection(cardinal_dirs[i])):
                validMoves.append(cardinal_dirs[i])
        return validMoves
    
    def validBuild(self, boardState, intendedMove: List[int], intendedBuild: List[int]):
        targetX = self.position[0] + intendedMove[0] + intendedBuild[0]
        targetY = self.position[1] + intendedMove[1] + intendedBuild[1]

        if targetX < 0 or targetX > 4 or targetY < 0 or targetY > 4:
            return False
        
        targetSquare = boardState.getSquare([targetX, targetY])
        if targetSquare.hasWorker() and targetSquare.worker != self.name:
            return False
        elif targetSquare.canBuild():
            return True
        
        return False

    def findAllBuilds(self, boardState, moveDir):
        cardinal_dirs = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        validCardinalBuilds = []
        for i in range(len(cardinal_dirs)):
            if self.validBuild(boardState, self.convertCardinalDirection(moveDir), self.convertCardinalDirection(cardinal_dirs[i])):
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
