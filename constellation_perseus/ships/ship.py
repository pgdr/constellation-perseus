from dataclasses import dataclass, field

from typing import Dict, List

import icontract

from .. import GameObject
from .. import GameObjectState
from .. import GameObjectAction
from .. import Allotrope
from .. import Position
from .. import Player
from .. import Gun

from .shipclassification import ShipClassification


@icontract.invariant(lambda self: self.owner is not None)
@icontract.invariant(lambda self: isinstance(self.owner, Player))
@icontract.invariant(lambda self: isinstance(self.classification, ShipClassification))
@icontract.invariant(
    lambda self: all([isinstance(k, Allotrope) for k in self.price.keys()])
)
@dataclass(eq=False)
class Ship(GameObject):
    owner: Player
    classification: ShipClassification = None
    cooldowntime: int = 0
    actions: List[GameObjectAction] = field(default_factory=list)
    price: Dict[Allotrope, int] = field(default_factory=dict)
    guns: List[Gun] = field(default_factory=list)
    name: str = None

    damage: float = 1
    state: GameObjectState = GameObjectState.IDLE
    lastjumptime: int = -10 ** 10

    def price_of(self, a: Allotrope):
        return self.price.get(a, 0)

    def remaining_cooldowntime(self, now: int):
        if self.lastjumptime == -10 ** 10:
            return 0

        diff = now - self.lastjumptime
        if diff >= self.cooldowntime:
            return 0
        return self.cooldowntime - diff

    @icontract.require(lambda now: isinstance(now, int))
    @icontract.require(lambda now: now > 0)
    def canjump(self, now: int):
        return self.remaining_cooldowntime(now) <= 0

    @icontract.require(lambda now: isinstance(now, int))
    @icontract.require(lambda now: now >= 0)
    @icontract.require(lambda pos: isinstance(pos, Position))
    def jumpto(self, pos: Position, now: int):
        if not self.canjump(now):
            return False
        self.assign_position(pos, now)
        self.lastjumptime = now
        return True

    def __str__(self):
        s = f"✈\t{self.classification} (owner={self.owner.name})"

        return s

    def destructor(self):
        return True

    def destroy(self):
        if self.destructor():
            self.state = GameObjectState.DESTROYED

    def destroyed(self):
        return self.state == GameObjectState.DESTROYED

    def idle(self):
        return self.state == GameObjectState.IDLE
