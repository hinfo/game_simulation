import random
from .builder import Builder
from .winner import Winner
from .result import Result


class Simulation:

    def __init__(self, simulations, rounds):
        self._simulations_range = simulations
        self._rounds_range = rounds

    def run(self):
        result = Result(timeout=1000)
        holdings_values = [
            (random.randint(300, 1600),
             random.randint(20, 299)) for _ in range(20)]

        for _ in range(self._simulations_range):
            builder = Builder(holdings_values)
            board = builder.build_board()
            dice = builder.get_dice()
            players = builder.get_players()

            for _round in range(self._rounds_range):
                if board.get_total_players() <= 1:
                    break

                for player in players:
                    if player.get_in_game():
                        square = player.forward(dice.roll())
                        holding = board.get_holding(square)
                        player.analyze(holding)

            result.add_winner(
                Winner(_round, board.get_winner())
            )

        return result.get_results()
