from human_player import HumanPlayer
from heuristic_player import HeuristicPlayer
from random_player import RandomPlayer

class Factory:
    def __init__(self):
        pass
    
    def createPlayer(self, color, playerType):
        if playerType == 'human':
            return HumanPlayer(color)
        elif playerType == 'heuristic':
            return HeuristicPlayer(color)
        elif playerType == 'random':
            return RandomPlayer(color)
        return None