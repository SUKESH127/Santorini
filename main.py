
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
        self.history = History(BoardState(self.players))
        self.currentBoardState = self.history.getCurrentBoardState()
        self.turnCount = 1

    def undo(self):
        return self.history.moveBack()
    
    def redo(self):
        return self.history.moveForward()

    def save(self):
        self.history.backup(self.currentBoardState)

    def switchPlayer(self):
        self.currentBoardState.switchPlayer()
        self.currentPlayer = self.currentBoardState.current_player

    def playGame(self):
        moveType = "next"
        while not self.currentBoardState.checkGameOver():
            # execute move type otherwise reprompt for valid move type
            if (moveType == 'undo'):
                if self.undo():
                    self.currentBoardState.printBoardState()
                    self.turnCount -= 1
            elif (moveType == 'redo'):
                if self.redo():
                    self.currentBoardState.printBoardState()
                    self.turnCount += 1
            elif (moveType == 'next'):
                self.currentBoardState.printBoardState()
                print(f'Turn: {self.turnCount}, {self.currentPlayer.color} ({self.currentPlayer.w1.name}{self.currentPlayer.w2.name})')
                self.turnCount += 1

                if self.enableScore:
                    self.currentBoardState.printScore(self.currentPlayer)
                if self.currentPlayer.playMove(self.currentBoardState) is False:
                    # current player wasn't able to make a move --> current player loses
                    if self.currentPlayer.color == 'white':
                        print('blue has won')
                    else:
                        print('white has won')
                    break
                self.switchPlayer()
                self.save()
            # get next move type for player
            if self.enableUndoRedo:
                moveType = input("undo, redo, or next\n")

if __name__ == "__main__":
    ProcessInput(sys.argv)