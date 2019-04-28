from dataclasses import dataclass

from .. import GameObject, Position, Player
from ..ships import Hq


@dataclass(eq=False)
class SpaceStation(GameObject):
    default_hq: Hq = None
    position: Position = None
    name: str = ""
    owner: Player = None
    damage: float = 1.0

    def is_under_construction(self):
        return False

    def __str__(self):
        if self.is_under_construction():
            return f"{self.name} (under construction)"

        return self.name
