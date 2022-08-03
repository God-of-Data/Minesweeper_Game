
def calculate_size_by_precentage(size, prcnt):

    size_portion = (prcnt / 100) * size

    return size_portion


BOARD_TITLE = "Minesweeper"

BOARD_WIDTH = 1440
BOARD_HEIGHT = 720

BOARD_BACKGROUND_COLOR = "black"

TOP_FRAME_WIDTH = calculate_size_by_precentage(size = BOARD_WIDTH, prcnt = 100)
TOP_FRAME_HEIGHT = calculate_size_by_precentage(size = BOARD_HEIGHT, prcnt = 25)
TOP_FRAME_X_AXIS_VALUE = calculate_size_by_precentage(size = BOARD_WIDTH, prcnt = 0)
TOP_FRAME_Y_AXIS_VALUE = calculate_size_by_precentage(size = BOARD_HEIGHT, prcnt = 0)

TOP_FRAME_BACKGROUND_COLOR = "red"

LEFT_FRAME_WIDTH = calculate_size_by_precentage(size = BOARD_WIDTH, prcnt = 25)
LEFT_FRAME_HEIGHT = calculate_size_by_precentage(size = BOARD_WIDTH, prcnt = 75)
LEFT_FRAME_X_AXIS_VALUE = calculate_size_by_precentage(size = BOARD_WIDTH, prcnt = 0)
LEFT_FRAME_Y_AXIS_VALUE = calculate_size_by_precentage(size = BOARD_HEIGHT, prcnt = 25)

LEFT_FRAME_BACKGROUND_COLOR = "blue"

CENTER_FRAME_WIDTH = calculate_size_by_precentage(size = BOARD_WIDTH, prcnt = 75)
CENTER_FRAME_HEIGHT = calculate_size_by_precentage(size = BOARD_WIDTH, prcnt = 75)
CENTER_FRAME_X_AXIS_VALUE = calculate_size_by_precentage(size = BOARD_WIDTH, prcnt = 25)
CENTER_FRAME_Y_AXIS_VALUE = calculate_size_by_precentage(size = BOARD_HEIGHT, prcnt = 25)

CENTER_FRAME_BACKGROUND_COLOR = "yellow"


