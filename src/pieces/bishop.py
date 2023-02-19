from src.pieces.piece import *

class Bishop(Piece):
    def __init__(self, file: FILE, rank: RANK, color: PIECE_COLOR) -> None:
        super().__init__(file, rank, color)

        self.__color = color

        if color == PIECE_COLOR.WHITE:
            self.img_path: str = getcwd() + '/assets/white_pieces/w_bishop.png'
        else:
            self.img_path: str = getcwd() + '/assets/black_pieces/b_bishop.png'


    def __str__(self) -> str:
        return 'B' + super().__str__()


    def all_moves(self):
        pos = (self.file, self.rank)
        moves = []

        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in range(1, BOARD_SQUARES):
                    if is_valid(pos[0] + k * i, pos[1] + k * j):
                        moves.append((pos[0] + k * i, pos[1] + k * j))
                    else:
                        break

        return moves
