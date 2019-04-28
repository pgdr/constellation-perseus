from typing import List, Dict
from dataclasses import dataclass, field

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


@dataclass(eq=False)
class Shipyard(SpaceStation):
    counstructed_at: int = 0

    SHIP_CONSTRUCTION_TIME: Dict[ShipClassification, int] = field(
        default_factory=_shipcon_fac
    )

    construction_time: int = 1500  # 2000 ms = 2 sec;
    actions: List[GameObjectAction] = field(default_factory=_action_fac)
    ship_construction: Dict[Ship, int] = None

    constructed: bool = False
    name: str = "Shipyard"

    def construct_ship(self, ship: Ship, time: int):
        print("Constructing ship now: " + (time / 1000) + " sec")
        ship_construction[ship] = time

    def deploy_ship(ship: Ship):
        game.add(ship)
        ship_construction.remove(ship)

        def tick(self, time: int):
            lock = game.lock()
            with lock:
                if not constructed:
                    if constructedAt + constructionTime <= time:
                        constructed = True

                for s, t in ship_construction.items():
                    sc = s.classification
                    if sc not in SHIP_CONSTRUCTION_TIME:
                        contiunue
                    if SHIP_CONSTRUCTION_TIME[s] is None:
                        continue
                    tc = SHIP_CONSTRUCTION_TIME[sc]
                    if t + tc <= time:
                        ship_construction[s] = None
                        self.deploy_ship(s)

        def __str__(self):
            if self.is_under_construction():
                return f"{self.name} (under construction)"
            if not ship_construction.is_empty():
                return f"{self.name} constructing ship {self.ship_construction}"

            return self.name

        # def to_message(self): -> Message:
        #    return Message.internal(str(self))

        def constructable_ships(self) -> list[Ship]:
            return None

        def constructable_spacestations(self) -> list[SpaceStation]:
            return None
