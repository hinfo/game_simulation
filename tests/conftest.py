import pytest

from app.board import Board
from app.builder import Builder
from app.game.models.player import Player
from app.game.models.player_type import PlayerType
from app.holding import Holding


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
