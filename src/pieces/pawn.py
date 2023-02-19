from src.pieces.piece import *

class Pawn(Piece):
    def __init__(self, file: FILE, rank: RANK, color: PIECE_COLOR) -> None:
        super().__init__(file, rank, color)

        self.__color = color

        if color == PIECE_COLOR.WHITE:
            self.img_path: str = getcwd() + '/assets/white_pieces/w_pawn.png'
        else:
            self.img_path: str = getcwd() + '/assets/black_pieces/b_pawn.png'


    def __str__(self) -> str:
        return 'P' + super().__str__()


    def all_moves(self):
        moves = []

        if self.color == PIECE_COLOR.WHITE:
            # Start condition
            if (self.rank == RANK._2):
                for i in range(1, 3):
                    move = (self.file, self.rank - i)
                    if is_valid(move[0], move[1]):
                        moves.append(move)
            else:
                move = (self.file, self.rank - 1)
                if is_valid(move[0], move[1]):
                    moves.append(move)

        
        elif self.color == PIECE_COLOR.BLACK:
            # Start state condition
            if (self.rank == RANK._7):
                for i in range(1, 3):
                    move = (self.file, self.rank + i)
                    if is_valid(move[0], move[1]):
                        moves.append(move)
            else:
                move = (self.file, self.rank + 1)
                if is_valid(move[0], move[1]):
                    moves.append(move)

        return moves
