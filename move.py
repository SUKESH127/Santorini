from worker import Worker
from board import Board

class Move:
    def __init__(self, worker: Worker, moveDirection: str, buildDirection: str, board: Board):
        self.worker = worker
        self.board = board
        self.moveOperation = self.convertMoveDirection(moveDirection)
        self.buildOperation = self.convertMoveDirection(buildDirection)
        self.startPosition = self.worker.position
        self.endPosition = [0, 0]

    def execute(self):
        self.updateLocation()
        self.updateBuild()

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
        return convertedDirection

    def updateLocation(self):
        # remove worker from old position
        x, y = self.startPosition[0], self.startPosition[1]
        self.board.getSquare([x, y]).removeWorker()
        # add worker to new position
        changeX, changeY = self.moveOperation[0], self.moveOperation[1]
        self.endPosition = [x + changeX, y + changeY]
        endX, endY = self.endPosition[0], self.endPosition[1]
        self.board.getSquare([endX, endY]).assign_worker(self.worker)
    
    def updateBuild(self):
        # get location to build
        x, y = self.endPosition[0], self.endPosition[1]
        changeX, changeY = self.buildOperation[0], self.buildOperation[1]
        buildX, buildY = x + changeX, y + changeY
        # build new tile
        self.board.getSquare([buildX, buildY]).build()




