from dataclasses import dataclass
from .player import Player


@dataclass
class HumanPlayer(Player):
    def __init__(self):
        super(HumanPlayer, self).__init__("Jonas")
