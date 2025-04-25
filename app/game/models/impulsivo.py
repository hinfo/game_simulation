

from app.holding import Holding
from .player_type import PlayerType
from .player import Player


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