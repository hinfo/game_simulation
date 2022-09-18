import random


class Dice:
    def __init__(self) -> None:
        self._face = 0

    def roll(self) -> int:
        self._face = random.randint(1, 6)
        return self._face
