from unittest import TestCase

class TestBoard(TestCase):
    def test_board(self, board):
        assert len(board.get_all_holdings()) == 1
        assert board.total_squares() == 1
        assert board.get_total_players() == 0

    def test_board_with_players(self, board, player):
        board.add_players([player])

        assert board.get_total_players() == 1