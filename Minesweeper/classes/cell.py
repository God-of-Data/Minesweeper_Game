from tkinter import Button,Frame

import random

import utils
import settings.cell_settings as sets


class Cell:

    CELL_QUANTITY        = sets.CELL_QUANTITY
    MINED_CELLS_QUANTITY = sets.MINED_CELLS_QUANTITY

    BUTTON_WIDTH  = sets.BUTTON_WIDTH
    BUTTON_HEIGHT = sets.BUTTON_HEIGHT

    MINED_CELL_COLOR      = sets.MINED_CELL_COLOR
    INITIAL_CELL_COLOR    = sets.INITIAL_CELL_COLOR
    CLICKED_CELL_COLOR    = sets.CLICKED_BUTTON_COLOR
    SUSPICIOUS_CELL_COLOR = sets.SUSPICIOUS_CELL_COLOR

    MINED_CELL_TEXT      = sets.MINED_CELL_TEXT
    INITIAL_CELL_TEXT    = sets.INITIAL_CELL_TEXT
    SUSPICIOUS_CELL_TEXT = sets.SUSPICIOUS_CELL_TEXT


    LEFT_CLICK_FLAG  = "<Button-3>"
    RIGHT_CLICK_FLAG = "<Button-1>"


    cell_container = []

    clicked_cells_counter    = 0 
    suspicious_cells_counter = 0 

    clicked_cells_counter_object           = None
    suspicious_cells_counter_object = None

    clicked_cells_counter_object_text_prefix    = ""
    suspicious_cells_counter_object_text_prefix = ""


    def __init__(self, col_index: int, row_index: int):

        self.set_is_clicked()
        self.set_is_marked_suspicious()
        self.set_is_mined()
        self.set_col_index(col_index)
        self.set_row_index(row_index)
        self.set_button()

        Cell.add_cell_to_cell_container(self)


    def set_is_clicked(self, is_clicked: bool = False): 

        self._is_clicked = is_clicked

        if(is_clicked):

            self.get_button().unbind(sequence = Cell.LEFT_CLICK_FLAG)
            self.get_button().unbind(sequence = Cell.RIGHT_CLICK_FLAG)

    def set_is_marked_suspicious(self,is_marked_suspicious: bool = False): 

        self._is_marked_suspicious = is_marked_suspicious

    def set_is_mined(self,is_mined: bool = False): 

        self._is_mined = is_mined

    def set_col_index(self, col_index: int): 

        self._col_index = col_index

    def set_row_index(self, row_index: int): 

        self._row_index = row_index

    def set_button(self, button: Button = None): 

        self._button = button


    def get_is_clicked(self) -> bool:

        return self._is_clicked

    def get_is_marked_suspicious(self) -> bool:

        return self._is_marked_suspicious

    def get_is_mined(self) -> bool:

        return self._is_mined

    def get_col_index(self) -> int:

        return self._col_index

    def get_row_index(self) -> int: 

        return self._row_index

    def get_button(self) -> Button: 

        return self._button


    is_clicked = property(
                            fget = get_is_clicked, 
                            fset = set_is_clicked
                         )

    is_marked_suspicious = property(
                                        fget = get_is_marked_suspicious, 
                                        fset = set_is_marked_suspicious
                                    )

    is_mined = property(
                         fget = get_is_mined, 
                         fset = set_is_mined
                       )

    col_index = property(
                            fget = get_col_index,
                            fset = set_col_index
                        )

    row_index = property(
                            fget = get_row_index,
                            fset = set_row_index
                        )

    is_button = property(
                            fget = get_button,
                            fset = set_button
                        )


    def create_button_in_cell(self, master_frame: Frame):


        temp_button = Button(
                                master = master_frame,
                                width  = Cell.BUTTON_WIDTH,
                                height = Cell.BUTTON_HEIGHT,
                                text   = Cell.INITIAL_CELL_TEXT,
                                bg     = Cell.INITIAL_CELL_COLOR
                            )


        temp_button.bind(
                            sequence = Cell.LEFT_CLICK_FLAG, 
                            func     = self.activate_left_click_actions
                        )

        temp_button.bind(
                            sequence = Cell.RIGHT_CLICK_FLAG,
                            func     = self.activate_right_click_actions
                        )


        self.set_button(temp_button)


    def add_cell_button_to_grid(self, col: int, row: int):

        self.get_button().grid(column = col, row = row)
        

    def activate_left_click_actions(self, event):

        if (not(self.get_is_clicked())):

            if(self.get_is_marked_suspicious()):

                self.unmark_cell_as_suspicious()
                self.set_is_marked_suspicious(False)

                Cell.suspicious_cells_counter -= 1

            else:

                self.mark_cell_as_suspicious()
                self.set_is_marked_suspicious(True)

                Cell.suspicious_cells_counter += 1

            Cell.update_suspicious_cells_counter_object()


    def activate_right_click_actions(self, event):

        cell_is_not_clicked_or_marked = not(self.get_is_marked_suspicious()) and not(self.get_is_clicked())


        if(cell_is_not_clicked_or_marked):

            Cell.clicked_cells_counter += 1

            self.set_is_clicked(True)

            Cell.update_clicked_cells_counter_object()

            
            if (self.get_is_mined()):

                self.mark_cell_as_mined()

                Cell.end_cells_activity_in_game(mined_cell_has_been_clicked = True)

            else:

                self.show_cell()


                adjacent_mined_cells_quantity = self.calculate_adjacent_mined_cells_quantity()


                if(adjacent_mined_cells_quantity == 0):

                    for cell in self.adjacent_cells:

                        cell_is_not_clicked_or_marked = not(cell.get_is_marked_suspicious()) and not(cell.get_is_clicked())

                        if(cell_is_not_clicked_or_marked):

                            Cell.clicked_cells_counter += 1

                            cell.show_cell()
                            cell.set_is_clicked(True)


                Cell.update_clicked_cells_counter_object()


                number_of_unclicked_cells_to_win = Cell.CELL_QUANTITY - Cell.MINED_CELLS_QUANTITY

                all_unmined_cells_are_open = Cell.clicked_cells_counter == number_of_unclicked_cells_to_win

                if(all_unmined_cells_are_open):

                    Cell.end_cells_activity_in_game(mined_cell_has_been_clicked = False)


    def show_cell(self):

        adjacent_mined_cells_quantity = self.calculate_adjacent_mined_cells_quantity()


        if (adjacent_mined_cells_quantity == 0):
       
            clicked_button_text = ""  
            
        else:
            
            clicked_button_text = f"{adjacent_mined_cells_quantity}"


        self.get_button().configure(
                                        text = clicked_button_text,
                                        bg   = Cell.CLICKED_CELL_COLOR
                                   )


    def mark_cell_as_mined(self):

        self.get_button().configure(
                                        text = Cell.MINED_CELL_TEXT,
                                        bg   = Cell.MINED_CELL_COLOR
                                   )


    def mark_cell_as_suspicious(self):

        self.get_button().configure(
                                        text = Cell.SUSPICIOUS_CELL_TEXT,
                                        bg   = Cell.SUSPICIOUS_CELL_COLOR
                                   )


    def unmark_cell_as_suspicious(self):

        self.get_button().configure(
                                        text = Cell.INITIAL_CELL_TEXT,
                                        bg   = Cell.INITIAL_CELL_COLOR
                                   )


    def calculate_adjacent_mined_cells_quantity(self) -> int:

        mined_cells_counter = 0

        for cell in self.adjacent_cells:

            mined_cells_counter += 1 if(cell.get_is_mined()) else 0


        return mined_cells_counter


    @property
    def adjacent_cells(self) -> list:

        cell_col = self.get_col_index()
        cell_row = self.get_row_index()


        adjacent_cells_list = [         
                                 Cell.find_cell_by_grid_coordinates(col = cell_col - 1, row = cell_row),
                                 Cell.find_cell_by_grid_coordinates(col = cell_col, row = cell_row - 1),
                                 Cell.find_cell_by_grid_coordinates(col = cell_col, row = cell_row + 1),
                                 Cell.find_cell_by_grid_coordinates(col = cell_col + 1, row = cell_row),
                                 Cell.find_cell_by_grid_coordinates(col = cell_col - 1, row = cell_row - 1),
                                 Cell.find_cell_by_grid_coordinates(col = cell_col - 1, row = cell_row + 1),
                                 Cell.find_cell_by_grid_coordinates(col = cell_col + 1, row = cell_row - 1),
                                 Cell.find_cell_by_grid_coordinates(col = cell_col + 1, row = cell_row + 1)
                              ]     

        adjacent_cells_list = [cell for cell in adjacent_cells_list if cell is not None]


        return adjacent_cells_list


    @staticmethod
    def add_cell_to_cell_container(cell):

        Cell.cell_container.append(cell)
    

    @staticmethod
    def find_cell_by_grid_coordinates(col: int, row: int):

        for cell in Cell.cell_container:

            cell_has_been_found_in_container = (cell.get_col_index() == col) and (cell.get_row_index() == row)

            if(cell_has_been_found_in_container):
        
                return cell
    

    @staticmethod
    def randomize_mines_in_all_cells(mine_quantity: int):

        randomly_picked_cells = random.sample(Cell.cell_container, mine_quantity)


        for cell in randomly_picked_cells:

            cell.set_is_mined(True)
        

    @staticmethod
    def define_clicked_cells_counter_object(object, text_prefix: str):

        Cell.clicked_cells_counter_object             = object
        Cell.clicked_cells_counter_object_text_prefix = text_prefix

        Cell.update_clicked_cells_counter_object()


    @staticmethod
    def define_suspicious_cells_counter_object(object, text_prefix: str):

        Cell.suspicious_cells_counter_object             = object
        Cell.suspicious_cells_counter_object_text_prefix = text_prefix

        Cell.update_suspicious_cells_counter_object()


    @staticmethod
    def update_clicked_cells_counter_object():

        unclicked_cells_quantity = Cell.CELL_QUANTITY - Cell.clicked_cells_counter

        label_text = f"{Cell.clicked_cells_counter_object_text_prefix} {unclicked_cells_quantity}"


        Cell.clicked_cells_counter_object.configure(text = label_text)
    

    @staticmethod
    def update_suspicious_cells_counter_object():

        label_text = Cell.suspicious_cells_counter_object_text_prefix + f"{Cell.suspicious_cells_counter}"


        Cell.suspicious_cells_counter_object.configure(text = label_text)


    @staticmethod
    def end_cells_activity_in_game(mined_cell_has_been_clicked: bool):

        game_has_been_won = not mined_cell_has_been_clicked

        utils.end_game(game_has_been_won)


    def __repr__(self) -> str:

        formatted_object_str  = f"Cell(col = {self.get_col_index()}, "
        formatted_object_str += f"row = {self.get_row_index()}, "
        formatted_object_str += f"is_mined = {self.get_is_mined()}, "
        formatted_object_str += f"is_marked_suspicious = {self.get_is_marked_suspicious()}, "
        formatted_object_str += f"is_clicked = {self.get_is_clicked()})"

        return formatted_object_str
