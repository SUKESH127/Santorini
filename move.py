from worker import Worker
import numpy as np

class Move:
    def __init__(self, worker, moveDirection, buildDirection):
        self.worker = worker
        self.directionToMove = self.convertDirection(moveDirection)
        self.directionToBuild = self.convertDirection(buildDirection)
        self.startPosition = self.worker.position
        self.endPosition = [0, 0]

    def execute(self):
        self.updateLocation()
        self.build()

    def convertMoveDirection(self, direction):
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
        else:
            print('Invalid move direction')
        return convertedDirection

    def canMove(self)->bool:
        pass

    def canBuild(self)->bool:
        pass

    def updateLocation(self):
        move = [0,0]
        x, y = self.startPosition[0], self.startPosition[1]
        self.board[x][y].remove_worker()
        self.board[x + move[0]][y + move[1]].assign_worker(self.worker)
    
    def build(self):
        pass



