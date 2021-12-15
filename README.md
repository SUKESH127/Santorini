# Santorini
Santorini is an abstract strategy game (think checkers/chess) designed by Dr. Gordan Hamilton.  

# Board representation

The physical game has lovely pieces designed to mimic the iconic architecture of the real island of Santorini, this is an ASCII representation so that the game can be played through a command line interface (CLI). We are only concerned with the 5x5 grid, and the workers are in default starting positions (shown below), so that the players do not have to pick where to start.

+--+--+--+--+--+
|0 |0 |0 |0 |0 |
+--+--+--+--+--+
|0 |0Y|0 |0B|0 |
+--+--+--+--+--+
|0 |0 |0 |0 |0 |
+--+--+--+--+--+
|0 |0A|0 |0Z|0 |
+--+--+--+--+--+
|0 |0 |0 |0 |0 |
+--+--+--+--+--+

This is the starting setup. The 5x5 board is viewed top down. A number in each space represents the level of the building. They all start unbuilt at level 0. A complete tower with a blue dome on top is shown as level 4. Next to the level number there is either a space, or the symbol for one of the 4 workers. The white player controls the A and B workers, while the blue player controls Y and Z.

# Move representation

On a player's turn they indicate through the CLI which worker they wish to move, which cardinal direction they wish to move, and which cardinal direction they wish to build (from the new space). For example, the white player chooses to move worker A north, then build in the space they just left.

Select a worker to move
A
Select a direction to move (n, ne, e, se, s, sw, w, nw)
n
Select a direction to build (n, ne, e, se, s, sw, w, nw)
s
+--+--+--+--+--+
|0 |0 |0 |0 |0 |
+--+--+--+--+--+
|0 |0Y|0 |0B|0 |
+--+--+--+--+--+
|0 |0A|0 |0 |0 |
+--+--+--+--+--+
|0 |1 |0 |0Z|0 |
+--+--+--+--+--+
|0 |0 |0 |0 |0 |
+--+--+--+--+--+

# Options
There are two types of basic computer opponents to play against. There is a Random computer player that will randomly choose a move from the set of allowed moves. Two bots are able to play against each other, in which case it will run through all the turns without prompting for additional input, until the game ends. The computer players print the move they took, so you can see what they did. This includes the worker that moves, the move direction, and the build direction. For example, the move shown earlier should be printed as A,n,s.

The Heuristic computer player that will assess the available moves and choose the one it thinks is best based on a few criteria. This player does not need to look multiple turns ahead to make this decision.

# Undo/Redo

There is also undo/redo functionality. When enabled with the history command line argument, the game gives the options undo, redo, or next before every turn (including AI turns). Undo rolls back to the previous game state. Redo reverses the most recent undo. Therefore, you can undo and redo multiple times. Undo does nothing if at turn 1 and redo does nothing if it is already the latest turn. After using undo, taking any new turn should invalidate any turns that could have been redone. To continue taking turns as usual, the user should enter next.

# How to Play

Thee code takes in arguments from the command line to configure the types of players and whether undo/redo and score display should be enabled or not. Note that you will want history off when running two computers against each other so that you don't have to type next every turn. Up to four arguments may be passed in to main.py from the command line and you cannot give an argument without supplying the ones before it. The arguments that are omitted from the end will have the default values. Therefore "python3 main.py random" is equivalent to "python3 main.py random human off off".

# How to Win

If a player has a worker on a level 3 building, they win. 
