
import sys
from typing import List
import copy

from board_state import BoardState
from factory import Factory
from player import Player
from history import History

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
        self.currentPlayer = self.whitePlayer
        self.enableUndoRedo = enableUndoRedo
        self.enableScore = enableScore
        self.history = History()
        self.boardState = BoardState(self.players)
        # save starting board state
        self.save()

    def undo(self):
        return self.history.moveBack()
    
    def redo(self):
        return self.history.moveForward()

    def save(self):
        mementoCopy = copy.deepcopy(self.boardState)
        self.history.backup(mementoCopy)

    def switchPlayer(self):
        self.boardState.switchPlayer()

    def playGame(self):
        self.printTurn()
        while not self.boardState.checkGameOver():
            if self.enableUndoRedo:
                moveType = input("undo, redo, or next\n")
            else:
                moveType = "next"
            # execute move type otherwise reprompt for valid move type
            if (moveType == 'undo'):
                if self.undo():
                    self.boardState = self.history.getCurrentBoardState()
                    self.history.updateWorkers(self.players)
            elif (moveType == 'redo'):
                if self.redo():
                    self.boardState = self.history.getCurrentBoardState()
                    self.history.updateWorkers(self.players)
            elif (moveType == 'next'):
                self.boardState.currentPlayer.playMove(self.boardState)
                self.save()
            else:
                continue
            self.printTurn()
    
    def printTurn(self):
        self.boardState.printBoardState(self.enableScore)
    
    def printLoser(self):
        if self.currentPlayer.color == 'white':
            print('blue has won')
        else:
            print('white has won')



if __name__ == "__main__":
    ProcessInput(sys.argv)