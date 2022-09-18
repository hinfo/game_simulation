from simulation.game import Holding, Player, Board, PlayerType, Builder
import pytest


@pytest.fixture
def holding():
    return Holding('500', '150')


@pytest.fixture
def board():
    holdings = [holding]
    return Board(holdings)


@pytest.fixture
def player(board):

    return Player(board, PlayerType.Aleatorio)


@pytest.fixture
def builder():
    holding_values = [('500', '150')]
    return Builder(holding_values)
