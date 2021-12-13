from worker import Worker
from board_state import BoardState

class Move:
    def __init__(self, worker: Worker, moveDirection: str, buildDirection: str, boardState: BoardState):
        self.worker = worker
        self.boardState = boardState
        self.moveOperation = self.convertCardinalDirection(moveDirection)
        self.buildOperation = self.convertCardinalDirection(buildDirection)
        self.startPosition = self.worker.position
        self.endPosition = [0, 0]

    def execute(self):
        self.updateLocation()
        self.updateBuild()

    def updateLocation(self):
        # remove worker from old position
        x, y = self.startPosition[0], self.startPosition[1]
        self.boardState.getSquare([x, y]).removeWorker()
        # add worker to new position
        changeX, changeY = self.moveOperation[0], self.moveOperation[1]
        self.endPosition = [x + changeX, y + changeY]
        self.boardState.getSquare(self.endPosition).assignWorker(self.worker.name)
        # update worker position
        self.worker.position = self.endPosition
    
    def updateBuild(self):
        # get location to build
        x, y = self.endPosition[0], self.endPosition[1]
        changeX, changeY = self.buildOperation[0], self.buildOperation[1]
        # build new tile
        self.boardState.getSquare([x + changeX, y + changeY]).build()
    
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




