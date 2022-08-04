from tkinter import Button

import random


class Cell:

    BUTTON_WIDTH  = 12
    BUTTON_HEIGHT = 4

    LEFT_MOUSE_CLICK_TKINTER_FLAG  = "<Button-3>"
    RIGHT_MOUSE_CLICK_TKINTER_FLAG = "<Button-1>"


    all_cells_container = []


    def __init__(self,row_index,col_index):

        self.set_is_mine()
        self.set_col_index(col_index)
        self.set_row_index(row_index)
        self.set_button()

        Cell.add_cell_to_cell_container(self)


    def set_is_mine(self,is_mine = False): 

        self.__is_mine = is_mine

    def set_col_index(self,col_index): 

        self.__col_index = col_index

    def set_row_index(self,row_index): 

        self.__row_index = row_index

    def set_button(self,button = None): 

        self.__button = button


    def get_is_mine(self) -> bool:

        return self.__is_mine

    def get_col_index(self) -> int:

        return self.__col_index

    def get_row_index(self) -> int: 

        return self.__row_index

    def get_button(self) -> Button: 

        return self.__button


    def create_button_in_cell(self,master_frame):

        temp_button = Button(
                                master = master_frame,
                                width  = Cell.BUTTON_WIDTH,
                                height = Cell.BUTTON_HEIGHT,
                                text   = f"{self.get_col_index()},{self.get_row_index()}"
                            )

        temp_button.bind(Cell.LEFT_MOUSE_CLICK_TKINTER_FLAG,self.activate_left_click_actions)
        temp_button.bind(Cell.RIGHT_MOUSE_CLICK_TKINTER_FLAG,self.activate_right_click_actions)

        self.set_button(temp_button)


    def add_cell_button_to_grid(self,col,row):

        temp_button = self.get_button().grid(column = col, row = row)
        
        self.set_button(temp_button)


    def activate_left_click_actions(self, event):
                
        print(event)


    def activate_right_click_actions(self, event):

        print(event)


    @staticmethod
    def add_cell_to_cell_container(cell):

        Cell.all_cells_container.append(cell)
    
    
    @staticmethod
    def randomize_mines_in_all_cells(mines_amount):


        randomly_picked_cells = random.sample(Cell.all_cells_container, mines_amount)


        for cell in randomly_picked_cells:

            cell.set_is_mine(True)
        

        print(randomly_picked_cells)


    def __repr__(self) -> str:
        
        return f"Cell({self.get_col_index()},{self.get_row_index()})"
