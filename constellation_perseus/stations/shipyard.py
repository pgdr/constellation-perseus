from typing import List, Dict
from dataclasses import dataclass, field
import icontract

from .spacestation import SpaceStation
from .. import ShipClassification, GameObjectAction

from .. import Ship


def _action_fac():
    return [
        GameObjectAction.BUILD_SHIP,
        GameObjectAction.BUILD_CARBONHARVESTER,
        GameObjectAction.BUILD_OXYGENHARVESTER,
        GameObjectAction.BUILD_COLONIALVIPER,
    ]


def _shipcon_fac():
    return {ShipClassification.HARVESTER: 2000, ShipClassification.VIPER: 1000}


@icontract.invariant(lambda self: isinstance(self.construction_time, int))
@icontract.invariant(lambda self: isinstance(self.name, str))
@dataclass(eq=False, frozen=False)
class Shipyard(SpaceStation):
    constructed_at: int = 0

    SHIP_CONSTRUCTION_TIME: Dict[ShipClassification, int] = field(
        default_factory=_shipcon_fac
    )

    construction_time: int = 1500  # 2000 ms = 2 sec;
    actions: List[GameObjectAction] = field(default_factory=_action_fac)

    ship_construction: Dict[Ship, int] = field(
        default_factory=dict
    )  # Currently building ... ship->time_of_construction

    constructed: bool = False
    name: str = "Shipyard"

    def construct_ship(self, ship: Ship, now: int):
        print(f"Constructing ship now: {(now / 1000)} sec")
        self.ship_construction[ship] = now

    def deploy_ship(self, ship: Ship):
        from constellation_perseus import Game
        from constellation_perseus import Harvester

        Game.instance.add(ship, pos_from=self)
        del self.ship_construction[ship]
        try:
            if isinstance(ship, Harvester):
                ship_hq = ship.default_hq
                ship_hq.register_harvester(ship)
        except AttributeError as e:
            print(f"Cannot set hq. {e}")

    def tick(self, now: int):
        if not self.constructed:
            if self.constructed_at + self.construction_time <= now:
                self.constructed = True
            return

        items = list(
            self.ship_construction.items()
        )  # due to `del ship_construction[s]`
        for s, t in items:
            sc = s.classification
            tc = self.SHIP_CONSTRUCTION_TIME.get(sc)

            if tc is None:
                raise ValueError(f"Invalid ship type {sc} for ship {s} in yard {self}")

            if t + tc <= now:
                print("DEPLOY!!!")
                self.deploy_ship(s)
            else:
                print(f"\t\tWaiting for {sc} to be completed (in {(t+tc) - now} secs)")

    def is_under_construction(self):
        return not self.constructed

    def __str__(self):
        pfx = f"🛫\tshipyard (station) {self.name}"
        if self.is_under_construction():
            return f"{pfx} (under construction) (owner={self.owner.name})"

        cons = ", ".join([f"{k}:{v}" for k, v in self.ship_construction.items()])

        if cons:
            return f"{pfx} constructing ship <!<{cons}>> (owner={self.owner.name})"
        return f"{pfx} <idle> (owner={self.owner.name})"
