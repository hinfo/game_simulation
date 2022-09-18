from abc import abstractmethod
from enum import Enum
from .holding import Holding
from .board import Board


class Player:
    def __init__(self, board: Board, type: Enum) -> None:
        self._board = board
        self._holdings = []
        self._square = 0
        self._amount = 300
        self._type = type
        self._in_game = True

    @abstractmethod
    def analyze(self, holding: Holding):
        pass

    def forward(self, dado: int) -> int:
        _result = self._square + dado

        if _result > self._board.total_squares():
            self._square = _result - self._board.total_squares()
            self.add_amount(100)
        else:
            self._square = _result
        return self._square

    def get_in_game(self):
        return self._in_game

    def disqualify(self) -> bool:
        if self._amount < 0:
            self._in_game = False
            return True
        return False

    def get_amount(self) -> int:
        return self._amount

    def add_amount(self, valor: int):
        self._amount += valor

    def add_holding(self, holding: Holding):
        self._holdings.append(holding)

    def _buy(self, holding: Holding):
        if self._amount >= holding.get_sell_cost():
            self._amount -= holding.get_sell_cost()
            self.add_holding(holding)
            holding.set_new_owner(self)

    def _pay(self, holding: Holding):
        self._amount -= holding.get_rent_value()
        owner = holding.get_owner()
        owner.get_paid(holding.get_rent_value())

    def get_paid(self, valor: int):
        self._amount += valor

    def return_holdings(self):
        holdings = \
            list(
                filter(
                    lambda x: x in self._holdings,
                    self._board.get_all_holdings()
                )
            )

        for holding in holdings:
            holding.set_available_market()

        self.holdings = []

    def get_type(self) -> Enum:
        return self._type

    def __str__(self):
        return f"Player( type: {self._type.name}, amount: {self._amount}, \
    In Game? {self._in_game} )"
