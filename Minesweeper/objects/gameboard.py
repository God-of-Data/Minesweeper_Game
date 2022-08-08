
from tkinter import *
from classes.cell    import Cell

import settings.gameboard_settings as sets


def create_gameboard_root_frame(title: str, background_color: str, size_string: str) -> Frame:

   root_frame = Tk()

   root_frame.title(title)
   root_frame.resizable(width = False, height = False)
   root_frame.configure(bg = background_color)
   root_frame.geometry(size_string)

   return root_frame


def create_gameboard_frame(master_object, 
                           background_color: str, 
                           width:            float, 
                           height:           float) -> Frame:

   temp_frame = Frame(
                        master = master_object, 
                        bg     = background_color,
                        width  = width, 
                        height = height
                     )

   return temp_frame


def create_gameboard_lable(master_object,
                           background_color: str,
                           text_color:       str, 
                           text_font:        tuple, 
                           text:             str = "") -> Label:

   temp_lable = Label(
                        master = master_object,
                        bg     = background_color,
                        fg     = text_color,
                        font   = text_font,
                        text   = text
                     )

   return temp_lable


def create_button_grid_on_object(master_object, grid_width: int, grid_length: int):

   for col_index in range(grid_width):

     for row_index in range(grid_length):

       temp_cell = Cell(col_index = col_index,row_index = row_index)


       temp_cell.create_button_in_cell(master_frame = master_object)
       temp_cell.add_cell_button_to_grid(col = col_index, row = row_index)


def activate_gameboard_root_frame(root_frame: Frame):

   root_frame.mainloop()


def main():

   formatted_root_frame_size_str = f"{sets.BOARD_WIDTH}x{sets.BOARD_HEIGHT}"


   root_frame = create_gameboard_root_frame( 
                                             title            = sets.BOARD_TITLE,
                                             background_color = sets.BOARD_BACKGROUND_COLOR,
                                             size_string      = formatted_root_frame_size_str
                                           )


   top_frame = create_gameboard_frame(
                                          master_object    = root_frame,
                                          background_color = sets.TOP_FRAME_BACKGROUND_COLOR,  
                                          width            = sets.TOP_FRAME_WIDTH,  
                                          height           = sets.TOP_FRAME_HEIGHT
                                     )

   left_frame = create_gameboard_frame(
                                          master_object    = root_frame,
                                          background_color = sets.LEFT_FRAME_BACKGROUND_COLOR,  
                                          width            = sets.LEFT_FRAME_WIDTH,  
                                          height           = sets.LEFT_FRAME_HEIGHT
                                      )

   center_frame = create_gameboard_frame(
                                             master_object    = root_frame,
                                             background_color = sets.CENTER_FRAME_BACKGROUND_COLOR,  
                                             width            = sets.CENTER_FRAME_WIDTH,  
                                             height           = sets.CENTER_FRAME_HEIGHT
                                        )


   gameboard_title_lable = create_gameboard_lable(
                                                      master_object    = top_frame,
                                                      background_color = sets.GAMEBOARD_TITLE_LABLE_BACKGROUND_COLOR, 
                                                      text_color       = sets.GAMEBOARD_TITLE_LABLE_TEXT_COLOR,
                                                      text_font        = sets.GAMEBOARD_TITLE_LABLE_TEXT_FONT,
                                                      text             = sets.GAMEBOARD_TITLE_LABLE_TEXT
                                                 ) 

   mined_cell_quantity_lable = create_gameboard_lable(
                                                         master_object    = left_frame,
                                                         background_color = sets.MINED_CELL_QUANTITY_LABLE_BACKGROUND_COLOR, 
                                                         text_color       = sets.MINED_CELL_QUANTITY_LABLE_TEXT_COLOR,
                                                         text_font        = sets.MINED_CELL_QUANTITY_LABLE_TEXT_FONT,
                                                         text             = sets.MINED_CELL_QUANTITY_LABLE_TEXT
                                                     ) 

   unclicked_cell_quantity_lable = create_gameboard_lable(
                                                            master_object    = left_frame,
                                                            background_color = sets.UNCLICKED_CELL_QUANTITY_LABLE_BACKGROUND_COLOR, 
                                                            text_color       = sets.UNCLICKED_CELL_QUANTITY_LABLE_TEXT_COLOR,
                                                            text_font        = sets.UNCLICKED_CELL_COUNTER_LABLE_TEXT_FONT
                                                         ) 

   suspicious_cell_quantity_lable = create_gameboard_lable(
                                                            master_object    = left_frame,
                                                            background_color = sets.UNCLICKED_CELL_QUANTITY_LABLE_BACKGROUND_COLOR, 
                                                            text_color       = sets.UNCLICKED_CELL_QUANTITY_LABLE_TEXT_COLOR,
                                                            text_font        = sets.UNCLICKED_CELL_COUNTER_LABLE_TEXT_FONT
                                                         ) 


   left_frame.place(
                     x = sets.LEFT_FRAME_X_COORDINATE, 
                     y = sets.LEFT_FRAME_Y_COORDINATE
                   )

   top_frame.place(
                     x = sets.TOP_FRAME_X_COORDINATE, 
                     y = sets.TOP_FRAME_Y_COORDINATE
                  )

   center_frame.place(
                       x = sets.CENTER_FRAME_X_COORDINATE, 
                       y = sets.CENTER_FRAME_Y_COORDINATE
                     )

   gameboard_title_lable.place(
                                 x = sets.GAMEBOARD_TITLE_LABLE_X_COORDINATE,
                                 y = sets.GAMEBOARD_TITLE_LABLE_Y_COORDINATE
                              )

   mined_cell_quantity_lable.place(
                                     x = sets.MINED_CELL_QUANTITY_LABLE_X_COORDINATE,
                                     y = sets.MINED_CELL_QUANTITY_LABLE_Y_COORDINATE
                                  )

   unclicked_cell_quantity_lable.place(
                                           x = sets.UNCLICKED_CELL_COUNTER_LABLE_X_COORDINATE, 
                                           y = sets.UNCLICKED_CELL_COUNTER_LABLE_Y_COORDINATE
                                      )

   suspicious_cell_quantity_lable.place(
                                           x = sets.SUSPICIOUS_CELL_COUNTER_LABLE_X_COORDINATE, 
                                           y = sets.SUSPICIOUS_CELL_COUNTER_LABLE_Y_COORDINATE
                                       )


   Cell.define_clicked_cells_counter_object(
                                               object      = unclicked_cell_quantity_lable, 
                                               text_prefix = sets.UNCLICKED_CELL_COUNTER_LABLE_TEXT
                                           )

   Cell.define_suspicious_cells_counter_object(
                                                 object      = suspicious_cell_quantity_lable, 
                                                 text_prefix = sets.SUSPICIOUS_CELL_COUNTER_LABLE_TEXT
                                              )


   create_button_grid_on_object(
                                 master_object = center_frame,
                                 grid_width    = sets.GRID_SIZE, 
                                 grid_length   = sets.GRID_SIZE
                               )


   Cell.randomize_mines_in_all_cells(mine_quantity = sets.MINE_QUANTITY)


   activate_gameboard_root_frame(root_frame = root_frame)
