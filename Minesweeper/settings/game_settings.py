
import math


GRID_SIZE     = 9
MINE_RATIO    = 0.25
CELL_QUANTITY = GRID_SIZE ** 2
MINE_QUANTITY = math.floor(CELL_QUANTITY * MINE_RATIO)


GAME_WIN_MESSAGE   = f"Well done! \n \n You've won the game!"
GAME_LOSE_MESSAGE  = "You've lost the game." 
GAME_MESSAGE_TITLE = "Minesweeper"
