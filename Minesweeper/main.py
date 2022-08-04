
from tkinter import *
from cell import Cell

import gameboard_settings as sets


root_frame_size_str = f'{sets.BOARD_WIDTH}x{sets.BOARD_HEIGHT}'


root = Tk()


root.title(sets.BOARD_TITLE)
root.resizable(width = False,height = False)
root.configure(bg = sets.BOARD_BACKGROUND_COLOR)
root.geometry(root_frame_size_str)


top_frame = Frame(
                    master = root, 
                    bg     = sets.TOP_FRAME_BACKGROUND_COLOR, 
                    width  = sets.TOP_FRAME_WIDTH, 
                    height = sets.TOP_FRAME_HEIGHT
                 )

left_frame = Frame(
                    master = root, 
                    bg     = sets.LEFT_FRAME_BACKGROUND_COLOR, 
                    width  = sets.LEFT_FRAME_WIDTH, 
                    height = sets.LEFT_FRAME_HEIGHT
                  )

center_frame = Frame(
                        master = root, 
                        bg     = sets.CENTER_FRAME_BACKGROUND_COLOR, 
                        width  = sets.CENTER_FRAME_WIDTH, 
                        height = sets.CENTER_FRAME_HEIGHT
                    )


left_frame.place(
                  x = sets.LEFT_FRAME_X_AXIS_VALUE, 
                  y = sets.LEFT_FRAME_Y_AXIS_VALUE
                )

top_frame.place(
                  x = sets.TOP_FRAME_X_AXIS_VALUE, 
                  y = sets.TOP_FRAME_Y_AXIS_VALUE
               )

center_frame.place(
                    x = sets.CENTER_FRAME_X_AXIS_VALUE, 
                    y = sets.CENTER_FRAME_Y_AXIS_VALUE
                  )


for col_index in range(sets.GRID_SIZE):

  for row_index in range(sets.GRID_SIZE):

    temp_cell = Cell(
                      row_index = row_index, 
                      col_index = col_index
                   )

    temp_cell.create_button_in_cell(master_frame = center_frame)
    temp_cell.add_cell_button_to_grid(col = col_index, row = row_index)

Cell.randomize_mines_in_all_cells(sets.MINES_AMOUNT)


root.mainloop()