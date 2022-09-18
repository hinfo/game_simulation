from .holding import Holding


class Board:
    def __init__(self, holdings: list) -> None:
        self._holdings = holdings
        self._players = []

    def total_squares(self) -> int:
        return len(self._holdings)

    def get_holding(self, square: int) -> Holding:
        return self._holdings[square - 1]

    def get_all_holdings(self) -> list:
        return self._holdings

    def add_players(self, players: list):
        self._players = players

    def get_total_players(self) -> int:
        in_game = 0
        for player in self._players:
            if player.get_in_game():
                in_game += 1

        return in_game

    def get_winner(self) -> object:
        for player in self._players:
            if player.get_in_game():
                return player
