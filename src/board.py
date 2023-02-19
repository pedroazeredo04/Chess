from src.pieces.piece import *
from src.pieces.king import *
from src.pieces.queen import *
from src.pieces.pawn import *
from src.pieces.bishop import *
from src.pieces.knight import *
from src.pieces.rook import *

from numpy import matrix as np_matrix
from src.utils import *

## This class represents the chess board
class Board:
    ## The board is represented by a 2D matrix
    def __init__(self) -> None:
        self.matrix: list[list[Piece or None]] = [[None for _ in range(8)] for _ in range(8)]

        for color in [PIECE_COLOR.BLACK, PIECE_COLOR.WHITE]:

            if color == PIECE_COLOR.WHITE:
                first_rank = RANK._1
                second_rank = RANK._2
            else:  # black
                first_rank = RANK._8
                second_rank = RANK._7
        
            self[FILE.E, first_rank] = King(FILE.E, first_rank, color)
            self[FILE.D, first_rank] = Queen(FILE.D, first_rank, color)
            self[FILE.C, first_rank] = Bishop(FILE.C, first_rank, color)
            self[FILE.F, first_rank] = Bishop(FILE.F, first_rank, color)
            self[FILE.B, first_rank] = Knight(FILE.B, first_rank, color)
            self[FILE.G, first_rank] = Knight(FILE.G, first_rank, color)
            self[FILE.A, first_rank] = Rook(FILE.A, first_rank, color)
            self[FILE.H, first_rank] = Rook(FILE.H, first_rank, color)

            for file in range(BOARD_SQUARES):
                self[file, second_rank] = Pawn(file, second_rank, color)
                


    ## This method converts from the board's coordinate system to the matrix's coordinate system
    def __getitem__(self, key: tuple[FILE, RANK]) -> Piece:
        return self.matrix[int(key[1])][int(key[0])]  # Looks ugly but conversion is necessary


    def __setitem__(self, key: tuple[FILE, RANK], value) -> None:
        self.matrix[int(key[1])][int(key[0])] = value


    def __delitem__(self, key: tuple[FILE, RANK]) -> None:
        self.matrix[int(key[1])][int(key[0])] = None


    ## other board related methods, like function decorating for moving pieces
