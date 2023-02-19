import pygame
from src.board import *
from src.utils import *


## This class is responsible for drawing the board and handling clicks
class Screen():
    # Constructor draws the pygame Board
    def __init__(self, screen_size: int) -> None:
        self.__highlighted_squares: list[tuple[FILE, RANK]] = []
        self.__circled_squares: list[tuple[FILE, RANK]] = []
        self.__screen_size: int = screen_size

        self.__screen: pygame.Surface = pygame.display.set_mode((screen_size, screen_size))

        pygame.display.set_caption("Chess")
        self.__screen.fill(BOARD_COLOR.LIGHT)

        self.__square_size: float = screen_size/BOARD_SQUARES

        self.board: Board = Board()

        for file in range(BOARD_SQUARES):
            for rank in range(BOARD_SQUARES):
                # Draw tasty rectangle colors
                self.reset_square(file, rank)

                if self.board[file, rank] is not None:
                    self.display_piece(self.board[file, rank])

        self.update_screen()



    # Returns file and rank of a position in the screen
    def handle_click(self, click: tuple[float, float]) -> tuple[FILE, RANK]:
        if click:
            x: int = (click[0] / self.__square_size) // 1
            y: int = (click[1] / self.__square_size) // 1

            ### vc tem que fazer (7 - rank) pra TUDO papai

            return (x, y)


    # Resets a board square
    def reset_square(self, file: FILE, rank: RANK, light_color: BOARD_COLOR = BOARD_COLOR.LIGHT, dark_color: BOARD_COLOR = BOARD_COLOR.DARK) -> None:
        color: BOARD_COLOR
        
        if rank % 2 == 0:
            color = light_color if (file % 2 == 0) else dark_color
        else:
            color = dark_color if (file % 2 == 0) else light_color

        square: pygame.Rect = pygame.Rect(self.__square_size * file, self.__square_size * rank, self.__square_size, self.__square_size)
        pygame.draw.rect(self.__screen, color, square)

        if self.board[file, rank]:
            self.display_piece(self.board[file, rank])

        self.update_screen()


    def reset_squares(self, squares: list[tuple[FILE, RANK]]) -> None:
        for square in squares:
            self.reset_square(square[0], square[1])


    # Highlights a board square
    def highlight_square(self, file: FILE, rank: RANK, highlight_color: BOARD_COLOR = BOARD_COLOR.HIGHLIGHT) -> None: 
        square: pygame.Rect = pygame.Rect(self.__square_size * file, self.__square_size * rank, self.__square_size, self.__square_size)
        pygame.draw.rect(self.__screen, highlight_color, square)

        if self.board[file, rank]:
            self.board[file, rank].all_moves()

        if self.board[file, rank]:
            self.display_piece(self.board[file, rank])

        self.update_screen()


    # Resetes a square if highlighted and vice versa
    def alter_square(self, file: FILE, rank: RANK, highlight_color: BOARD_COLOR = BOARD_COLOR.HIGHLIGHT, light_color: BOARD_COLOR = BOARD_COLOR.LIGHT, dark_color: BOARD_COLOR = BOARD_COLOR.DARK) -> None:
        if (file, rank) in self.__highlighted_squares:
            self.reset_square(file, rank, light_color, dark_color)
            self.__highlighted_squares.remove((file, rank))
        else:
            self.highlight_square(file, rank, highlight_color)
            self.__highlighted_squares.append((file, rank))


    # Destructor
    def __del__(self) -> None:
        pygame.quit()


    # Displays a piece
    def display_piece(self, piece: Piece) -> None:
        piece_surface: pygame.Surface = pygame.image.load(piece.img_path).convert_alpha()
        scaled_piece: pygame.Surface = pygame.transform.scale(piece_surface, (self.__square_size, self.__square_size))
        self.__screen.blit(scaled_piece, (piece.file * self.__square_size, piece.rank * self.__square_size))
        self.update_screen()


    # Display the possible moves of a piece on the board OR desdiplay them
    def display_possible_moves(self, moves: list[tuple]) -> None:
        self.__circled_squares = moves
        for move in moves:
            circle: pygame.Surface = pygame.image.load(CIRCLE_PATH).convert_alpha()
            scaled_circle: pygame.Surface = pygame.transform.scale(circle, (self.__square_size, self.__square_size))
            self.__screen.blit(scaled_circle, (move[0] * self.__square_size, move[1] * self.__square_size))
            self.update_screen()


    # Display and returns the possible moves
    # This function also does the resetting logic if the selected piece is changed
    def handle_move_display(self, file: FILE, rank: RANK) -> list[tuple[FILE, RANK]]:
        if self.__circled_squares != []:
            self.reset_squares(self.__circled_squares)
            self.__circled_squares = []

        if self.board[file, rank]:
            self.__circled_squares = self.board[file, rank].all_moves()
        else:
            self.__circled_squares = []

        self.display_possible_moves(self.__circled_squares)
        return self.__circled_squares


    def update_screen(self) -> None:
        pygame.transform.flip(self.__screen, False, True)
        pygame.display.update()
