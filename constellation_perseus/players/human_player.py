from dataclasses import dataclass
from .player import Player

@dataclass
class HumanPlayer(Player):
    def __init__(self):
        __super__(self, "Jonas")
