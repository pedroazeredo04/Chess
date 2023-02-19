from os import getcwd

BOARD_SQUARES: int = 8  # number of squares in a rank or file of the board


CIRCLE_PATH = getcwd() + '/assets/circle-logo.png'


## This class represents the color of a board square
class BOARD_COLOR:
    LIGHT: tuple = (255, 255, 255)  # white
    DARK: tuple = (232, 100, 52, 255)  # dark orange
    HIGHLIGHT: tuple = (170, 54, 54, 1)  # dark red


## This class represents the color of a piece
class PIECE_COLOR:
    WHITE: int = 1
    BLACK: int = 0


# I'm a chess player, sorry
class FILE:
    A: int = 0
    B: int = 1
    C: int = 2
    D: int = 3
    E: int = 4
    F: int = 5
    G: int = 6
    H: int = 7


# Pygame's y axis is from top to bottom
class RANK:
    _1: int = 7
    _2: int = 6
    _3: int = 5
    _4: int = 4
    _5: int = 3
    _6: int = 2
    _7: int = 1
    _8: int = 0


# Returns if a square is valid for moving or not
def is_valid(file: FILE, rank: RANK) -> bool:
    if file < 0 or file > BOARD_SQUARES - 1 or rank < 0 or rank > BOARD_SQUARES - 1:
        return False
    return True
