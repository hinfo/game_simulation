from unittest import TestCase


class TestHolding(TestCase):
    def test_holding(self, holding):
        assert holding.get_rent_value() == "150"
        assert holding.get_sell_cost() == "500"
        assert holding.get_owner() == "None"
        assert holding.available() is True

    def test_holding_with_owner(self, holding, player):
        holding.set_new_owner(player)

        assert holding.get_rent_value() == "150"
        assert holding.get_sell_cost() == "500"
        assert holding.get_owner() == player
        assert holding.available() is False

    def test_holding_with_owner_and_rent(self, holding, player):
        holding.set_new_owner(player)
        holding.set_rent_value(200)

        assert holding.get_rent_value() == "200"
        assert holding.get_sell_cost() == "500"
        assert holding.get_owner() == player
        assert holding.available() is False

    def test_holding_with_owner_and_sell_cost(self, holding, player):
        holding.set_new_owner(player)
        holding.set_sell_cost(1000)

        assert holding.get_rent_value() == "150"
        assert holding.get_sell_cost() == "1000"
        assert holding.get_owner() == player
        assert holding.available() is False
