import operator
from functools import reduce
from .models import PlayerType
from .winner import Winner


class Result:
    def __init__(self, timeout) -> None:
        self._winners = []
        self._timeout = timeout

    def timeout_counter(self) -> int:
        return len(self.matches_time_out())

    def matches_time_out(self) -> list:
        result = list(filter(lambda x: x.get_round() == self._timeout,
                             self._winners))
        return list([str(x) for x in result])

    def add_winner(self, winner: Winner):
        self._winners.append(winner)

    def avg(self) -> int:
        _rounds = list([x.get_round() for x in self._winners])
        return round(reduce(lambda x, y: x + y, _rounds) / len(_rounds), 2)

    def get_players(self) -> list:
        players = []
        for _type in PlayerType:
            players.append(_type.name)
        return players

    def percentual_wins_by_behavior(self) -> dict:
        total = len(self._winners)
        wins = {}
        for _type in PlayerType:
            wins[_type.name] = round((len(
                list(
                    filter(
                        lambda x: x.get_player_type() == _type.value,
                        self._winners)
                )
            ) * 100) / total)
        return wins

    def most_winner(self):
        _result = self.percentual_wins_by_behavior()
        return max(_result.items(), key=operator.itemgetter(1))[0]

    def get_results(self):
        return {
            'time_out_matches': self.timeout_counter(),
            'avg': self.avg(),
            'percent': self.percentual_wins_by_behavior(),
            'most_winner': self.most_winner(),
            'players':  self.get_players()
            }
