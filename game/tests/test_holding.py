
def test_holding(holding):
    holding.set_new_owner('John')

    assert holding.get_rent_value() == '150'
    assert holding.get_sell_cost() == '500'
    assert holding.get_owner() == 'John'
    assert holding.available() is False
