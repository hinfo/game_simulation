
from app.holding import Holding
from .player_type import PlayerType
from .player import Player


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