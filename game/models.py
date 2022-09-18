import random
from enum import Enum
from .player import Player
from .holding import Holding


class PlayerType(Enum):
    Impulsivo = 1,
    Exigente = 2,
    Cauteloso = 3,
    Aleatorio = 4


class Exigente(Player):
    def __init__(self, board) -> None:
        super().__init__(board, PlayerType.Exigente)

    def analyze(self, holding: Holding):
        if holding.available():
            if holding.get_rent_value() > 50:
                self._buy(holding)
        else:
            self._pay(holding)

        if self.disqualify():
            self.return_holdings()


class Impulsivo(Player):
    def __init__(self, board) -> None:
        super().__init__(board, PlayerType.Impulsivo)

    def analyze(self, holding: Holding):
        if holding.available():
            self._buy(holding)
        else:
            self._pay(holding)

        if self.disqualify():
            self.return_holdings()


class Aleatorio(Player):
    def __init__(self, board) -> None:
        super().__init__(board, PlayerType.Aleatorio)

    def analyze(self, board: Holding):
        if board.available():
            if random.randint(1, 2) == 1:
                self._buy(board)
        else:
            self._pay(board)

        if self.disqualify():
            self.return_holdings()


class Cauteloso(Player):
    def __init__(self, board) -> None:
        super().__init__(board, PlayerType.Cauteloso)

    def analyze(self, board: Holding):
        if board.available():
            if self.get_amount() - board.get_sell_cost() >= 80:
                self._buy(board)
        else:
            self._pay(board)

        if self.disqualify():
            self.return_holdings()
