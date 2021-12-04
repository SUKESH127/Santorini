
import sys

from board import Board
from player import Player

import sys
class ProcessInput():
    def __init__(self, args):
        self.args = args[1:]

        self.whitePlayer = "human"
        self.bluePlayer = "human"
        self.enableUndoRedo = "off"
        self.enableScore = "off"

        if not self.validateSetup():
            print("Invalid setup")
            sys.exit(1)
        else:
            Manager()._run()
    
    def validateSetup(self):
        return self.checkWhitePlayer() and self.checkBluePlayer() and self.checkEnableUndoRedo() and self.checkEnableScore()
    
    def checkWhitePlayer(self):
        if self.args[0] not in {"human", "heuristic", "random"}:
            return False
        else:
            self.whitePlayer = self.args[0]
            return True
    
    def checkBluePlayer(self):
        if self.args[1] not in {"human", "heuristic", "random"}:
            return False
        else:
            self.bluePlayer = self.args[1]
            return True
    
    def checkEnableUndoRedo(self):
        if self.args[2] not in {"on", "off"}:
            return False
        else:
            self.enableUndoRedo = self.args[2]
            return True
    
    def checkEnableScore(self):
        if self.args[3] not in {"on", "off"}:
            return False
        else:
            self.enableScore = self.args[3]
            return True


class Manager:
    def __init__(self):
        self._board = Board()
        self._p1 = Player()
        self._p2 = Player()

    def run(self):
        
        while True:
            break

if __name__ == "__main__":
    ProcessInput(sys.argv)