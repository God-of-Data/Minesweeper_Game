
import sys

from tkinter import messagebox

import settings.game_settings as sets


def calculate_size_by_precentage(size: float, prcnt: float) -> float:

    size_portion = (prcnt / 100) * size

    return size_portion


def end_game(game_has_been_won: bool):

    if(game_has_been_won):

        announce_win()

    else:

        announce_lose()

    close_gameboard()


def announce_win():

    messagebox.showinfo(
                            title   = sets.GAME_MESSAGE_TITLE,
                            message = sets.GAME_WIN_MESSAGE
                       )


def announce_lose():

    messagebox.showerror(
                            title   = sets.GAME_MESSAGE_TITLE,
                            message = sets.GAME_LOSE_MESSAGE   
                        )


def close_gameboard():

    sys.exit()

