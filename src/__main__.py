"""The entry point to this game."""

from typing import List

from blessed import Terminal

board = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "d"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["w", "w", "w", "w", ".", "w", "w", "w"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["p", ".", ".", ".", ".", ".", ".", "."],
]

term = Terminal()

COLORPLAYER = term.blue_on_blue
COLORWALL = term.chartreuse4_on_chartreuse4
COLOREND = term.yellow_on_yellow
COLORAIR = term.white_on_white
COLORTERMINAL = term.on_white


def draw_board(board: List[List[str]]) -> None:
    """
    Draws the game board.

    :param board: 2D list of strings that represent the game state.
    """
    print(term.home + COLORTERMINAL + term.clear)
    for line in board:
        currentcolor = None
        accum = ""

        for char in line:
            if char == "." and currentcolor is not COLORAIR:
                currentcolor = COLORAIR
                accum += COLORAIR
            elif char == "p" and currentcolor is not COLORPLAYER:
                currentcolor = COLORPLAYER
                accum += COLORPLAYER
            elif char == "w" and currentcolor is not COLORWALL:
                currentcolor = COLORWALL
                accum += COLORWALL
            elif char == "d" and currentcolor is not COLOREND:
                currentcolor = COLOREND
                accum += COLOREND

            accum += char

        print(accum + "\n")


if __name__ == "__main__":
    with term.fullscreen(), term.cbreak():
        draw_board(board)
        term.inkey()
