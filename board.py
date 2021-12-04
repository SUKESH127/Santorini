


class Square:

    def __init__(self):
        self._level = 0
        self._worker = ' '
    
    def has_worker(self):
        if self._worker == ' ':
            return False
        return True
    
    def assign_worker(self, w):
        self._worker = w
    
    def can_build(self):
        return self._level != 4   

    def build(self):
        self._level += 1
    
    def __str__(self):
        return f'{self._level}{self._worker}'


class Board:

    def __init__(self):
        self.grid = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append(Square())
            self.grid.append(row)
        
        # assign player 1's workers
        self.grid[3][1].assign_worker('A')
        self.grid[1][3].assign_worker('B')

        # assign player 2's workers
        self.grid[1][1].assign_worker('Y')
        self.grid[3][3].assign_worker('Z')

    def __str__(self):
        print("+--+--+--+--+--+")
        for i in range(5):
            for j in range(5):
                print(f'|{self.grid[i][j]}', end='')
            print("|\n+--+--+--+--+--+")
