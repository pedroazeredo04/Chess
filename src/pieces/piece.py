from abc import ABC, abstractmethod
from src.utils import *
from os import getcwd


# Abstract class Piece
class Piece(ABC):
    def __init__(self, file: FILE, rank: RANK, color: PIECE_COLOR) -> None:
        self.file: FILE = file  # x axis
        self.rank: RANK = rank  # y axis
        self.color: PIECE_COLOR = color
        self.alive: bool = True

        self._img_path: str = ''

    
    def set_pos(self, key: tuple[int, int]) -> None:
        self.file = key[0]
        self.rank = key[1]


    def __del__(self) -> None:
        pass


    @abstractmethod
    def __str__(self) -> str:
        return f'{self.color}'


    def __repr__(self) -> str:
        return self.__str__()
    

    def print_pos(self) -> None:
        print(f'{self.__str__()} is at {self.file}, {self.rank}')


    @abstractmethod
    # ISSO vai retornar tipo __TODOS__ os lances possíveis, sem ligar para o resto do tabuleiro
    # mas ai VC faz um DECORATOR pra essa função @see https://www.youtube.com/watch?v=QH5fw9kxDQA
    # Isso vai retornar um método "real_moves" QUE AÍ SIM CONSIDERA O RESTO DAS POSIÇÕES
    def all_moves(self) -> list[tuple[FILE, RANK]]:
        pass
