from app.holding import Holding
from app.game.models.player_type import PlayerType
from app.game.models.player import Player


DEFAULT_VALUE = 80

class Cauteloso(Player):
    def __init__(self, board) -> None:
        super().__init__(board, PlayerType.Cauteloso)

    def analyze(self, board: Holding):
        if board.available():
            if self.get_amount() - board.get_sell_cost() >= DEFAULT_VALUE:
                self._buy(board)
        else:
            self._pay(board)

        if self.disqualify():
            self.return_holdings()