


class Square:

    def __init__(self):
        self.level = 0
        self.worker is None
    
    def has_worker(self):
        if self.worker is None:
            return False
        return True
    
    def assign_worker(self, w):
        self.worker = w
    
    def can_build(self):
        return self.level != 4

    def build(self):
        self.level += 1


class Board:

    def __init__(self):
        self._grid = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append(Square())
            grid.append(row)

        # assign player 1 workers
        self._grid[2][2].assign_worker()

        # assign player 2 workers

