from src.pieces.piece import *

class Queen(Piece):
    def __init__(self, file: FILE, rank: RANK, color: PIECE_COLOR) -> None:
        super().__init__(file, rank, color)

        self.__color = color

        if color == PIECE_COLOR.WHITE:
            self.img_path: str = getcwd() + '/assets/white_pieces/w_queen.png'
        else:
            self.img_path: str = getcwd() + '/assets/black_pieces/b_queen.png'


    def __str__(self) -> str:
        return 'Q' + super().__str__()


    def all_moves(self):
        pos = (self.file, self.rank)
        moves = []

        for i in [-1, 1]:
            for k in range(1, BOARD_SQUARES):
                if is_valid(pos[0] + k * i, pos[1]):
                    moves.append((pos[0] + k * i, pos[1]))
                else:
                    break
            for k in range(1, BOARD_SQUARES):
                if is_valid(pos[0], pos[1] + k * i):
                    moves.append((pos[0], pos[1] + k * i))
                else:
                    break

        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in range(1, BOARD_SQUARES):
                    if is_valid(pos[0] + k * i, pos[1] + k * j):
                        moves.append((pos[0] + k * i, pos[1] + k * j))
                    else:
                        break

        return moves
