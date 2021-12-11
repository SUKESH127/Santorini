from worker import Worker

class Move:
    def __init__(self, x, y):
        self.worker = Worker()
        self.moveType = None
        self.startPosition = None
        self.endPosition = [0, 0]

    def execute(self):
        move = [0,0]
        self.endPosition = self.startPosition + move
