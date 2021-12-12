
import sys
from typing import List

from board import Board
from player import Player

import sys
class ProcessInput():
    def __init__(self, args):
        self.args = args[1:]

        self.whitePlayer = "human"
        self.bluePlayer = "human"
        self.enableUndoRedo = False
        self.enableScoreHistory = False

        if not self.validateSetup():
            print("Invalid setup")
            sys.exit(1)
        else:
            playerList = [self.whitePlayer, self.bluePlayer]
            manager = Manager(playerList, self.enableUndoRedo, self.enableScoreHistory)
            manager.playGame()
    
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
    def __init__(self, playerTypes: List, undoRedo: bool, scoreHistory: bool):
        self.undoRedo = undoRedo
        self.scoreHistory = scoreHistory
        self.currentBoardState = Board()
        self.players = [Player(playerTypes[0], "white"), Player(playerTypes[1], "blue")]
        self.currentPlayer = self.players[0]

    def playGame(self):
        while not self.currentBoardState.checkGameOver():
            self.currentBoardState.printBoard()
            self.currentPlayer.playMove(self.currentBoardState)
            self._switchPlayers()
            break # remove later
    
    def _undo(self):
        pass
    
    def _redo(self):
        pass
    
    def _save(self):
        pass
    
    def _switchPlayers(self):
        self.currentPlayer = self.players[1] if self.currentPlayer == self.players[0] else self.players[0]

if __name__ == "__main__":
    p = ProcessInput(sys.argv)