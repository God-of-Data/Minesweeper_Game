
import utils

import settings.game_settings as sets


GRID_SIZE     = sets.GRID_SIZE
MINE_QUANTITY = sets.MINE_QUANTITY

BOARD_WIDTH  = 680
BOARD_HEIGHT = 660


BOARD_TITLE = "Minesweeper"

BOARD_BACKGROUND_COLOR = "black"


TOP_FRAME_BACKGROUND_COLOR = "black"

TOP_FRAME_WIDTH        = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 100)
TOP_FRAME_HEIGHT       = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 25)
TOP_FRAME_X_COORDINATE = 0
TOP_FRAME_Y_COORDINATE = 0


LEFT_FRAME_BACKGROUND_COLOR = "black"

LEFT_FRAME_WIDTH        = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 27)
LEFT_FRAME_HEIGHT       = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 75)
LEFT_FRAME_X_COORDINATE = 0
LEFT_FRAME_Y_COORDINATE = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 25)


CENTER_FRAME_BACKGROUND_COLOR = "black"


CENTER_FRAME_WIDTH        = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 70)
CENTER_FRAME_HEIGHT       = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 75)
CENTER_FRAME_X_COORDINATE = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 25)
CENTER_FRAME_Y_COORDINATE = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 25)


GAMEBOARD_TITLE_LABLE_TEXT_COLOR       = "#F47174"
GAMEBOARD_TITLE_LABLE_BACKGROUND_COLOR = "black"

GAMEBOARD_TITLE_LABLE_TEXT  = "The Minesweeper"

GAMEBOARD_TITLE_LABLE_TEXT_FONT = ("",40)

GAMEBOARD_TITLE_LABLE_X_COORDINATE  = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 18)
GAMEBOARD_TITLE_LABLE_Y_COORDINATE  = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 5)


MINED_CELL_QUANTITY_LABLE_TEXT_COLOR       = "white"
MINED_CELL_QUANTITY_LABLE_BACKGROUND_COLOR = "black"

MINED_CELL_QUANTITY_LABLE_TEXT  = f"Mined Cells: {sets.MINE_QUANTITY}"

MINED_CELL_QUANTITY_LABLE_TEXT_FONT = ("",12)

MINED_CELL_QUANTITY_LABLE_X_COORDINATE  = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 2)
MINED_CELL_QUANTITY_LABLE_Y_COORDINATE  = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 1)


UNCLICKED_CELL_QUANTITY_LABLE_TEXT_COLOR       = "white"
UNCLICKED_CELL_QUANTITY_LABLE_BACKGROUND_COLOR = "black"

UNCLICKED_CELL_COUNTER_LABLE_TEXT  = "Unclicked Cells: " 

UNCLICKED_CELL_COUNTER_LABLE_TEXT_FONT = ("",12)

UNCLICKED_CELL_COUNTER_LABLE_X_COORDINATE  = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 2)
UNCLICKED_CELL_COUNTER_LABLE_Y_COORDINATE  = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 9)


SUSPICIOUS_CELL_QUANTITY_LABLE_TEXT_COLOR       = "white"
SUSPICIOUS_CELL_QUANTITY_LABLE_BACKGROUND_COLOR = "black"

SUSPICIOUS_CELL_COUNTER_LABLE_TEXT  = "Suspicious Cells: "

SUSPICIOUS_CELL_COUNTER_LABLE_TEXT_FONT = ("",12)

SUSPICIOUS_CELL_COUNTER_LABLE_X_COORDINATE  = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 2)
SUSPICIOUS_CELL_COUNTER_LABLE_Y_COORDINATE  = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 17)
