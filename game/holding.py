
class Holding:
    def __init__(self, sell_cost, rent_value) -> None:
        self._sell_cost = sell_cost
        self._rent_value = rent_value
        self._owner = None

    def available(self) -> bool:
        if self._owner is None:
            return True
        return False

    def get_rent_value(self) -> int:
        return self._rent_value

    def get_sell_cost(self) -> int:
        return self._sell_cost

    def get_owner(self) -> object:
        return self._owner

    def set_new_owner(self, owner) -> bool:
        if self.available():
            self._owner = owner
            return True
        return False

    def set_available_market(self):
        self._owner = None
