from unittest import TestCase

class TestPlayer(TestCase):     
    def test_player_aleatorio(self, player):
        assert player.get_amount() == 300
        assert player.get_type().name == 'Aleatorio'
        assert player.disqualify() is False
        assert player.return_holdings() is None


    def test_player_disqualified(self, player):     
        player.disqualify()
        assert player.get_amount() == 0
        assert player.get_type().name == 'Desclassificado'
        assert player.disqualify() is True
        assert player.return_holdings() is None
    
    def test_player_aleatorio_with_holdings(self, player, holding):
        player.add_holding(holding)
        assert player.get_amount() == 300
        assert player.get_type().name == 'Aleatorio'
        assert player.disqualify() is False
        assert player.return_holdings() == [holding]