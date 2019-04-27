from typing import List, Dict

from .spacestation import SpaceStation
from .. import ShipClassification, GameObjectAction

from .. import Ship

class Shipyard(SpaceStation):

    SHIP_CONSTRUCTION_TIME = {
        ShipClassification.HARVESTER: 2000,
        ShipClassification.VIPER: 1000,
    }

    construction_time: int = 1500
    # 2000 ms = 2 sec;
    counstructed_at: int
    actions: List[GameObjectAction] = [
        GameObjectAction.BUILD_SHIP,
        GameObjectAction.BUILD_CARBONHARVESTER,
        GameObjectAction.BUILD_OXYGENHARVESTER,
        GameObjectAction.BUILD_COLONIALVIPER,
    ]
    constructed: bool = False
    ship_construction: Dict[Ship, int]

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
