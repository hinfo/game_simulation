import random
from app.holding import Holding
from .player_type import PlayerType
from .player import Player


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