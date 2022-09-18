
def test_board(board):

    assert len(board.get_all_holdings()) == 1
    assert board.total_squares() == 1
    assert board.get_total_players() == 0


def test_board_with_players(board, player):
    board.add_players([player])

    assert board.get_total_players() == 1
