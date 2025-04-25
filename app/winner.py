

class Winner:
    def __init__(self, round, player):
        self._round = round
        self._player = player

    def get_player(self) -> object:
        return self._player

    def get_round(self) -> int:
        return self._round

    def get_player_type(self) -> int:
        _type = self._player.get_type()
        return _type.value

    def __str__(self):
        return f'Winner( Type: {self._player}, Round: {self._round} )'
