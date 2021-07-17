"""The entry point to this game."""

from time import sleep
from typing import List

from blessed import Terminal

board = [[
    ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", ".", ".", ".", ".", ".", ".", "d", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", "w", "w", "w", ".", "w", "w", "w", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", "p", ".", ".", ".", ".", ".", ".", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
],
[
    ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", ".", ".", ".", ".", "w", ".", ".", "w"],
    ["w", ".", "w", "w", ".", "w", ".", "d", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", "w", "w", "w", ".", "w", "w", "w", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", ".", ".", ".", ".", ".", ".", ".", "w"],
    ["w", "p", ".", ".", ".", ".", ".", ".", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
]]

term = Terminal()

COLORPLAYER = term.blue_on_blue
COLORWALL = term.chartreuse4_on_chartreuse4
COLOREND = term.yellow_on_yellow
COLORAIR = term.white_on_white
COLORTERMINAL = term.white_on_white


class WinRound(BaseException):
    pass


def draw_board(_board: List[List[str]]) -> None:
    """
    Draws the game board.
    :param _board: 2D list of strings that represent the game state.
    """
    print(term.home + COLORTERMINAL + term.clear)
    for line in _board:
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


def find_symbol(_board: List, char):
    row_number = 0
    for row in _board:
        if char in row:
            player_index_x = row_number
            player_index_y = row.index(char)
        row_number += 1
    return (player_index_x, player_index_y)


def collision(_board, x=0, y=0) -> bool:

    rows = len(_board) - 1
    columns = len(_board[0]) - 1

    if x == 0 or y == 0:
        return False
    elif x == rows or y == columns:
        return False
    elif _board[x][y] == "w":
        return False
    else:
        return True


def check_win(_board, x, y):
    win_x, win_y = find_symbol(_board, "d")
    if win_x == x and win_y == y:
        return True
    else:
        return False


def move(_board: List, direction: str) -> List:
    player_x, player_y = find_symbol(_board, "p")
    action = {
        "btn_left": (player_x, player_y - 1),
        "btn_right": (player_x, player_y + 1),
        "btn_up": (player_x, player_y),
        "btn_down": (player_x, player_y),
    }
    player_new_x, player_new_y = action[direction]
    rotate_action = {
        "btn_left": rotate_board(_board, 0),
        "btn_right": rotate_board(_board, 0),
        "btn_up": rotate_board(_board, 1),
        "btn_down": rotate_board(_board, 2),
    }
    _board = rotate_action[direction]
    if player_x == player_new_x and player_y == player_new_y:
        player_new_x, player_new_y = find_symbol(_board, "p")
    if check_win(_board, player_new_x, player_new_y):
        raise WinRound
    if collision(_board, player_new_x, player_new_y):
        _board[player_x][player_y] = "."
        _board[player_new_x][player_new_y] = "p"
    return _board


def gravity(_board: List):
    player_x, player_y = find_symbol(_board, "p")
    while collision(_board, player_x + 1, player_y):
        if check_win(_board, player_x + 1, player_y):
            raise WinRound
        _board[player_x][player_y] = "."
        player_x += 1
        _board[player_x][player_y] = "p"
    return _board


def key_mapping(key: str, _board: List):
    action = {
        "a": "btn_left",
        "d": "btn_right",
        "w": "btn_up",
        "s": "btn_down",
    }
    _board = move(_board, action[key])
    return gravity(_board)


def rotate_board(_board, rotate_direction):
    n = len(_board)
    m = len(_board[1])
    new_board = []
    if rotate_direction == 0:
        return _board
    if rotate_direction == 1:
        for i in range(m):
            new_row = []
            for j in range(n - 1, -1, -1):
                new_row.append(_board[j][i])
            new_board.append(new_row)
    if rotate_direction == 2:
        for i in range(n - 1, -1, -1):
            new_row = []
            for j in range(m):
                new_row.append(_board[j][i])
            new_board.append(new_row)

    return new_board


if __name__ == "__main__":
    with term.fullscreen(), term.cbreak():
        boardcount = 0
        draw_board(board[boardcount])
        val = term.inkey()
        # It will be working until ESCAPE pressed
        while val.code != term.KEY_ESCAPE:
            val = term.inkey()
            if val and str(val) in "wasd":
                try:
                    board[boardcount] = key_mapping(str(val), board[boardcount])
                    draw_board(board[boardcount])
                except WinRound:
                    boardcount += 1
                    if boardcount > len(board)-1:
                        print(term.green_on_black + "You Win")
                        sleep(5)
                        break
                    else:
                        draw_board(board[boardcount])
            else:
                pass
