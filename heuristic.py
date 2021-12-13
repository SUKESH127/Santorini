from player import Player

class Heuristic(Player):
    def __init__(self, color: str):
        super().__init__(self, "heuristic", color)   

    def selectMove(self):
        pass
    