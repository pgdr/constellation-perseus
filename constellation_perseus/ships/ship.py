from dataclasses import dataclass

from typing import Dict, List

from .. import GameObject
from .. import GameObjectState
from .. import GameObjectAction
from .. import Allotrope
from .. import Position
from .. import Player
from .. import Gun

from .shipclassification import ShipClassification


@dataclass(eq=False)
class Ship(GameObject):
    classification: ShipClassification = None
    cooldowntime: int = None
    actions: List[GameObjectAction] = None
    price: Dict[Allotrope, int] = None
    guns: List[Gun] = None
    name: str = None
    owner: Player = None

    damage: float = 1
    state: GameObjectState = GameObjectState.IDLE
    lastjumptime: int = -10 ** 10

    def price_of(self, a: Allotrope):
        return price.get(a, 0)

    def canjump(self):
        return self.cooldowntime == 0

    def remaining_cooldowntime(self):
        if self.lastjumptime == -10 ** 10:
            return 0
        now = Game.now()
        return max(0, now - self.lastjumptime)

    def jumpto(self, pos: Position):
        if not self.canjump():
            return False
        Game.instance().assign_position(self, pos)
        self.lastjumptime = Game.now()
        return True

    def __str__(self):
        s = "Ship " + str(self.classification)

        if not self.canjump():
            s += f"(cooling down ... {self.remaining_cooldowntime() / 1000})"
        return s

    def destructor(self):
        return True

    def destroy(self):
        if self.destructor():
            setState(GameObjectState.DESTROYED)

    def destroyed(self):
        self.state == GameObjectState.DESTROYED

    def idle(self):
        return self.state == GameObjectState.IDLE
