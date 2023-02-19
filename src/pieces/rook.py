from src.pieces.piece import *

class Rook(Piece):
    def __init__(self, file: FILE, rank: RANK, color: PIECE_COLOR) -> None:
        super().__init__(file, rank, color)

        self.__color = color

        if color == PIECE_COLOR.WHITE:
            self.img_path: str = getcwd() + '/assets/white_pieces/w_rook.png'
        else:
            self.img_path: str = getcwd() + '/assets/black_pieces/b_rook.png'


    def __str__(self) -> str:
        return 'R' + super().__str__()


    def all_moves(self):
        pos = (self.file, self.rank)
        moves = []

        for i in range(BOARD_SQUARES):
                moves.append((i, pos[1]))
                moves.append((pos[0], i))

        return moves
