from player import Player

class Random(Player):
    def __init__(self, color: str):
        super().__init__(self, "Random", color)   

    def selectMoves(self):
        pass