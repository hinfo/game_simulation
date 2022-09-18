
def test_player(player):

    assert player.get_amount() == 300
    assert player.get_type().name == 'Aleatorio'
    assert player.disqualify() is False
    assert player.return_holdings() is None
