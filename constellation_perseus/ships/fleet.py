from dataclasses import dataclass
from typing import List

from . import Ship
from .. import Player, Position, GameObject, GameObjectAction


@dataclass
class Fleet(GameObject):

    actions: List[GameObjectAction]

    ships: List[Ship]
    position: Position
    name: str

    owner: Player

    def _ready(self):
        return all([s.ready() for s in self.ships])

    def jumpto(pos: Position):
        if not self._ready():
            return False
        for s in ships:
            s.jumpto(pos)
        self.position = pos

    def tick(self, time: int):
        # a fleet is more like an abstract concept so no action necessary
        pass

    def damage(self):
        return 0  # a fleet isn't damaged
