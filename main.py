
import sys
from typing import List

from board import Board
from factory import Factory
from player import Player

import sys
class ProcessInput():
    def __init__(self, args: List[str]):
        self.args = ['human', 'human', 'off', 'off']
        for i in range(1, len(args)):
             self.args[i - 1] = args[i]

        self.whitePlayer = ""
        self.bluePlayer = ""
        self.enableUndoRedo = ""
        self.enableScore = ""

        if not self.validateSetup():
            print("Invalid setup")
            sys.exit(1)
        else:
            keepHistory = True if self.enableUndoRedo == "on" else False
            keepScore = True if self.enableScore == "on" else False
            m = Manager(self.whitePlayer, self.bluePlayer, keepHistory, keepScore)
            m.playGame()
    
    def validateSetup(self, ):
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
    def __init__(self, whitePlayerType: str, bluePlayerType: str, enableUndoRedo: bool, enableScore: bool):
        self.whitePlayer = Factory().createPlayer("white", whitePlayerType)
        self.bluePlayer = Factory().createPlayer("blue", bluePlayerType)
        self.players = [self.whitePlayer, self.bluePlayer]
        self.board = Board(self.players)
        self.currentPlayer = self.whitePlayer
        self.enableUndoRedo = enableUndoRedo
        self.enableScore = enableScore
    
    def printGameStatus(self):
        print("Game over")

    def undo(self):
        #self.board.undo()
        pass
    
    def redo(self):
        #self.board.redo()
        pass

    def save(self):
        pass

    def switchPlayer(self):
        self.board.switchPlayer()

    def playGame(self):
        while not self.board.checkGameOver():
            self.board.printBoard()
            if self.enableScore:
                self.board.printScore()
            self.currentPlayer.playMove(self.board)
            self.switchPlayer()
        self.printGameStatus()

if __name__ == "__main__":
    ProcessInput(sys.argv)