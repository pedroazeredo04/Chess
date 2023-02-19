from src.pieces.piece import *

class Knight(Piece):
    def __init__(self, file: FILE, rank: RANK, color: PIECE_COLOR) -> None:
        super().__init__(file, rank, color)

        self.__color = color

        if color == PIECE_COLOR.WHITE:
            self.img_path: str = getcwd() + '/assets/white_pieces/w_knight.png'
        else:
            self.img_path: str = getcwd() + '/assets/black_pieces/b_knight.png'


    def __str__(self) -> str:
        return 'N' + super().__str__()


    def all_moves(self):
        pos = (self.file, self.rank)
        moves = []
        for i in [-1, 1]:
            for j in [-1, 1]:
                if is_valid(pos[0] + i, pos[1] + j * 2):
                    moves.append((pos[0] + i, pos[1] + j * 2))
                if is_valid(pos[0] + i * 2, pos[1] + j):
                    moves.append((pos[0] + i * 2, pos[1] + j))

        return moves
