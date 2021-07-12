"""The entry point to this game."""

from typing import List

from blessed import Terminal

board = [
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", "d", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", "w", "w", "w", "w", ".", "w", "w", "w", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", "p", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
]

term = Terminal()

COLORPLAYER = term.blue_on_blue
COLORWALL = term.chartreuse4_on_chartreuse4
COLOREND = term.yellow_on_yellow
COLORAIR = term.white_on_white
COLORTERMINAL = term.white_on_white


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

        print(accum)


def find_player(_board: List):
    row_number = 0
    for row in board:  
        if 'p' in row:
            player_index_x = row_number
            player_index_y = row.index('p')
        row_number += 1
    return (player_index_x, player_index_y)


def move(direction: str):
    if direction != "btn_rotate":
        player_x, player_y = find_player(board)
        action = {
            "btn_left": (player_x, player_y - 1),
            "btn_right": (player_x, player_y + 1) ,
            "btn_up": (player_x - 1, player_y ),
            "btn_down": (player_x + 1, player_y ),
            "btn_rotate": (player_x, player_y)
        }
        new_board = board
        new_board[player_x][player_y] = '.'
        player_new_x, player_new_y = action[direction]
        new_board[player_new_x][player_new_y] = 'p'
    else:
        new_board = rotate_board(board)
    
    draw_board(new_board)

def key_mapping(key: str):
    action = {
        "a": "btn_left",
        "d": "btn_right",
        "w": "btn_up",
        "s": "btn_down",
        "e": "btn_rotate",
    }
    move(action[key])


def rotate_board(board):
    n = len(board)
    new_board = []
    for i in range(n):
        new_row = []
        for j in range(n - 1, -1, -1):
            new_row.append(board[j][i])
        new_board.append(new_row)
    return new_board


if __name__ == "__main__":
    with term.fullscreen(), term.cbreak():
        draw_board(board)
        val = term.inkey()
        # It will be working until ESCAPE pressed
        while val.code != term.KEY_ESCAPE:
            val = term.inkey()
            if val and str(val) in "wasde":
                key_mapping(str(val))
            else:
                pass
