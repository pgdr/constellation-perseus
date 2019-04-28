"""
A HqShip is the/a head quarter of a player.

@author pgd
"""

from dataclasses import dataclass, field
from typing import List, Dict

from .ship import Ship, ShipClassification
from .. import Allotrope, Allotropes, Star, Position, GameObject, Player
from .harvesters import Harvester


@dataclass(eq=False)
class Hq(Ship):
    star: Star = None  # This is the star the HqShip is orbiting. Might be None.
    harvesters: List[
        Harvester
    ] = None  # all harvesters this Hq operates. Note that this is not the  same as all the harvesters a player has.
    assets: Dict[Allotrope, int] = field(
        default_factory={
            Allotropes.OXYGEN: 1000,
            Allotropes.CARBON: 800,
            Allotropes.SELENIUM: 7000,
        }
    )  # The assets owned by this hq.
    cooldown_time: int = 10 * 1000  # 10 seconds

    def __init__(self, name: str, yield_: GameObject, owner: Player):
        super(Hq, self).__init__(
            name, ShipClassification.HQ, self.cooldown_time, owner, {}
        )

        self.assets = {
            Allotropes.OXYGEN: 1000,
            Allotropes.CARBON: 800,
            Allotropes.SELENIUM: 7000,
        }

    async def buy(self, ship: Ship):
        lock = asyncio.Lock()

        async with lock:
            assert ship.owner == self.owner(), "Owner of ship is not owner of hq buying"

            if not self.can_afford(ship):
                return False
            for a, p in ship.price.items():
                self.withdraw_asset(a, p)
            return True

    def can_afford(self, ship: Ship):
        lock = asyncio.Lock()

        with lock:
            for a, p in ship.price.items():
                if p > assets[a]:
                    return False
        return True

    def withdraw_asset(self, allotrope: Allotrope, amount: int) -> bool:
        if amount <= 0:
            return True
        lock = asyncio.Lock()

        with lock:
            cash = assets.get(allotrope, 0)
            if cash < amount:
                return False
            assets[allotrope] = cash - amount
            return True

    def get_asset(self, allotrope: Allotrope):
        return self.assets.get(allotrope, 0)

    def set_star(self, star: Star):
        """Sets the star this hq is assigned to, updates position to reflect that of the
        star

        """

        if not star:
            self.star = None
            return True
        return self.jumpto(star.position)

    def empty(self, harvester: Harvester):
        allotrope = harvester.classification.allotrope
        mined = harvester.reset()
        self.add_allotrope(allotrope, mined)

    def add_allotrope(self, allotrope: Allotrope, amount: int):
        lock = asyncio.Lock()
        with lock:
            self.assets[allotrope] = self.get_asset(allotrope) + amount

    def get_allotrope(self, allotrope: Allotrope) -> int:
        return self.get_asset(allotrope)

    def add_harvester(self, harvester: Harvester):
        """Adds a harvester to this hq's internal harvesters, sets star of harvester to
        be this hq's star.

        """
        self.harvesters.append(harvester)
        harvester.set_star(self.star)
        harvester.set_state(GameObjectState.HARVESTING)

    def tick(self, time: int):
        for harvester in self.harvesters:
            if h.destroyed():
                pass  # TODO perform GC
            elif h.harvesting():
                harvested = harvester.reset()
                allotrope = harvester.classification.allotrope
                self.add_allotrope(allotrope, harvested)

    def __str__(self) -> str:
        return "HQ, assets: " + str(self.assets)
