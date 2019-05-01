from dataclasses import dataclass

from .. import GameObject, Player
from ..ships import Hq


@dataclass(eq=False)
class SpaceStation(GameObject):
    owner: Player
    default_hq: Hq = None
    name: str = ""
    damage: float = 1.0

    def is_under_construction(self):
        return False

    def __str__(self):
        unc = " (under construction)" if self.is_under_construction() else ""
        return f"🚉\tstation {self.name}" + unc
