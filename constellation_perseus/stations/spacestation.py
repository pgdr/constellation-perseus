from dataclasses import dataclass

from .. import GameObject, Position, Player
from .. import Hq


@dataclass
class SpaceStation(GameObject):
    default_hq: Hq
    position: Position
    name: str
    owner: Player
    damage: float = 1.0

    def under_construction(self):
        return False

        def __str__(self):
            if self.is_under_construction():
                return f"{self.name} (under construction)"

            return self.name
