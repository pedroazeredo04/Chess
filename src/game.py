from src.screen import *


## This class is responsible for running the game
class Game():
    def __init__(self) -> None:
        self.screen: Screen = Screen(720)


    def get_click(self, event: pygame.event.Event) -> tuple[float, float] or None:
        if event.type == pygame.MOUSEBUTTONUP:
            pos: tuple[float, float] = pygame.mouse.get_pos()

            return pos


    def run(self) -> None:
        running: bool = True
        move_options: list[tuple[FILE, RANK]] = []
        selected_piece: Piece or None = None
        previous_click: tuple[FILE, RANK] or None = None

        while running:
            event = pygame.event.wait()

            if event.type == pygame.QUIT: running = False

            ### IF EVENT TYPE == BOTÃO DIREITO
                #self.screen.alter_square(clicked_pos[0], clicked_pos[1])

            clicked_board_pos: tuple[FILE, RANK] = self.screen.handle_click(self.get_click(event))

            if clicked_board_pos:

                if self.screen.board[clicked_board_pos[0], clicked_board_pos[1]]:
                    move_options = self.screen.handle_move_display(clicked_board_pos[0], clicked_board_pos[1])
                    selected_piece = self.screen.board[clicked_board_pos[0], clicked_board_pos[1]]
                    previous_click = clicked_board_pos

                elif selected_piece:
                    if clicked_board_pos in move_options:
                        del self.screen.board[previous_click[0], previous_click[1]]
                        selected_piece.set_pos(clicked_board_pos)
                        self.screen.board[clicked_board_pos[0], clicked_board_pos[1]] = selected_piece

                        self.screen.reset_square(previous_click[0], previous_click[1])
                        self.screen.reset_squares(move_options)
                        self.screen.display_piece(selected_piece)

                    else:
                        self.screen.reset_squares(move_options)
