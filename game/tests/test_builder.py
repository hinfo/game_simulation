
def test_builder(builder):
    players = builder.get_players()
    board = builder.build_board()
    dice = builder.get_dice()
    assert len(players) == 4
    assert players[0].get_amount() == 300
    assert len(board.get_all_holdings()) == 1
    assert dice._face == 0
