
import utils


GRID_SIZE = 6 

MINES_AMOUNT = int((GRID_SIZE ** 2) // 4)


BOARD_WIDTH  = 1440
BOARD_HEIGHT = 720


BOARD_TITLE = "Minesweeper"

BOARD_BACKGROUND_COLOR = "black"


TOP_FRAME_BACKGROUND_COLOR = "black"

TOP_FRAME_WIDTH        = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 100)
TOP_FRAME_HEIGHT       = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 25)
TOP_FRAME_X_AXIS_VALUE = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 0)
TOP_FRAME_Y_AXIS_VALUE = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 0)


LEFT_FRAME_BACKGROUND_COLOR = "black"

LEFT_FRAME_WIDTH        = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 25)
LEFT_FRAME_HEIGHT       = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 75)
LEFT_FRAME_X_AXIS_VALUE = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 0)
LEFT_FRAME_Y_AXIS_VALUE = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 25)


CENTER_FRAME_BACKGROUND_COLOR = "black"


CENTER_FRAME_WIDTH        = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 75)
CENTER_FRAME_HEIGHT       = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 75)
CENTER_FRAME_X_AXIS_VALUE = utils.calculate_size_by_precentage(size = BOARD_WIDTH,prcnt = 25)
CENTER_FRAME_Y_AXIS_VALUE = utils.calculate_size_by_precentage(size = BOARD_HEIGHT,prcnt = 25)
