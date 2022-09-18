from .models import Impulsivo, Exigente, Cauteloso, Aleatorio
from .dice import Dice
from .holding import Holding
from .board import Board


class Builder:
    def __init__(self, holding_values) -> None:
        self.__board = Board(self.build_holdings(holding_values))
        self.__dice = Dice()
        self.__players = [
            Impulsivo(self.__board), Exigente(self.__board),
            Cauteloso(self.__board), Aleatorio(self.__board)
        ]
        self.__board.add_players(self.__players)

    @staticmethod
    def build_holdings(holding_values) -> list:
        return [Holding(value[0], value[1]) for value in holding_values]

    def build_board(self) -> Board:
        return self.__board

    def get_players(self) -> list:
        return self.__players

    def get_dice(self) -> Dice:
        return self.__dice
