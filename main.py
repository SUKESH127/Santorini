
import sys
from typing import List

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
        self.turnCount = 1
        self.history = History()
        self.boardState = BoardState(self.players, None)
        # save starting board state
        self.save()

    def undo(self):
        return self.history.moveBack()
    
    def redo(self):
        return self.history.moveForward()

    def save(self):
        self.history.backup(BoardState(self.players, self.boardState))
        print("$$$$$$$$$$$$$$$$$$")
        print("$$$$$$$$$$$$$$$$$$")
        for b in self.history.mementos:
            b.printBoardState()
        print("$$$$$$$$$$$$$$$$$$")
        print("$$$$$$$$$$$$$$$$$$")

    def switchPlayer(self):
        if self.turnCount % 2 == 1:
            self.currentPlayer = self.whitePlayer
        else:
            self.currentPlayer = self.bluePlayer

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
                    self.turnCount -= 1
                    self.switchPlayer()
            elif (moveType == 'redo'):
                if self.redo():
                    self.turnCount += 1
                    self.switchPlayer()
            elif (moveType == 'next'):
                if self.currentPlayer.playMove(self.boardState) is False:
                    # current player wasn't able to make a move --> current player loses
                    self.printLoser()
                    break
                self.turnCount += 1
                self.switchPlayer()
                self.save()
            else:
                continue
            # print to terminal
            self.boardState = self.history.getCurrentBoardState()
            self.history.updateWorkers(self.players)
            self.printTurn()
    
    def printTurn(self):
        self.boardState.printBoardState()
        turnString = f'Turn: {self.turnCount}, {self.currentPlayer.color} ({self.currentPlayer.w1.name}{self.currentPlayer.w2.name})'
        if self.enableScore:
            turnString += self.currentPlayer.getCurrentScore(self.boardState)
        print(turnString)
    
    def printLoser(self):
        if self.currentPlayer.color == 'white':
            print('blue has won')
        else:
            print('white has won')



if __name__ == "__main__":
    ProcessInput(sys.argv)