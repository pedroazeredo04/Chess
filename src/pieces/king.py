from src.pieces.piece import *

class King(Piece):
    def __init__(self, file: FILE, rank: RANK, color: PIECE_COLOR) -> None:
        super().__init__(file, rank, color)

        self.__color = color

        if color == PIECE_COLOR.WHITE:
            self.img_path: str = getcwd() + '/assets/white_pieces/w_king.png'
        else:
            self.img_path: str = getcwd() + '/assets/black_pieces/b_king.png'


    def __str__(self) -> str:
        return 'K' + super().__str__()


    def all_moves(self) -> list[tuple[FILE, RANK]]:
        pos = (self.file, self.rank)
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if is_valid(pos[0] + i, pos[1] + j):
                    moves.append((pos[0] + i, pos[1] + j))

        return moves
