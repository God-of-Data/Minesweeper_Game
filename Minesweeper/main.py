
from tkinter import *

import gameboard_settings as settings


root = Tk()

root.title(settings.BOARD_TITLE)
root.resizable(width = False, height = False)
root.configure(bg = settings.BOARD_BACKGROUND_COLOR)
root.geometry(f'{settings.BOARD_WIDTH}x{settings.BOARD_HEIGHT}')

top_frame = Frame(
                    master = root, 
                    bg = settings.TOP_FRAME_BACKGROUND_COLOR, 
                    width = settings.TOP_FRAME_WIDTH, 
                    height = settings.TOP_FRAME_HEIGHT
                 )

top_frame.place(x = settings.TOP_FRAME_X_AXIS_VALUE, y = settings.TOP_FRAME_Y_AXIS_VALUE)

left_frame = Frame(
                    master = root, 
                    bg = settings.LEFT_FRAME_BACKGROUND_COLOR, 
                    width = settings.LEFT_FRAME_WIDTH, 
                    height = settings.LEFT_FRAME_HEIGHT
                  )

left_frame.place(x = settings.LEFT_FRAME_X_AXIS_VALUE, y = settings.LEFT_FRAME_Y_AXIS_VALUE)

center_frame = Frame(
                        master = root, 
                        bg = settings.CENTER_FRAME_BACKGROUND_COLOR, 
                        width = settings.CENTER_FRAME_WIDTH, 
                        height = settings.CENTER_FRAME_HEIGHT
                    )

center_frame.place(x = settings.CENTER_FRAME_X_AXIS_VALUE, y = settings.CENTER_FRAME_Y_AXIS_VALUE)

root.mainloop()