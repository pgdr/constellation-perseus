"""
A HqShip is the/a head quarter of a player.

@author pgd
"""

from dataclasses import dataclass, field
from typing import List, Dict
import icontract

from .ship import Ship
from .. import Allotrope, Allotropes, Star
from .harvesters import Harvester

from .. import GameObjectState
from .shipclassification import ShipClassification


@dataclass(eq=False)
class Hq(Ship):

    # This is the star the HqShip is orbiting. Might be None.
    star: Star = None

    classification: ShipClassification = ShipClassification.HQ

    # all harvesters belonging to this Hq
    harvesters: List[Harvester] = field(default_factory=list)

    # The assets (allotropes) owned by this hq.
    assets: Dict[Allotrope, int] = field(
        default_factory=lambda: {
            Allotropes.OXYGEN.value: 1000,
            Allotropes.CARBON.value: 800,
            Allotropes.SELENIUM.value: 7000,
        }
    )

    cooldown_time: int = 10 * 1000  # 10 seconds

    def buy(self, ship: Ship):
        assert (
            ship.owner == self.owner
        ), f"Owner of ship {ship.owner} is not owner of hq buying {self.owner}"

        if not self.can_afford(ship):
            return False
        for a, p in ship.price.items():
            self.withdraw_asset(a, p)
        return True

    @icontract.require(
        lambda ship: all([isinstance(k, Allotrope) for k in ship.price.keys()])
    )
    @icontract.require(
        lambda self: all([isinstance(k, Allotrope) for k in self.assets.keys()])
    )
    def can_afford(self, ship: Ship):
        for a, p in ship.price.items():
            a_in_stock = self.assets.get(a, 0)
            if p > a_in_stock:
                return False
        return True

    @icontract.require(lambda allotrope: isinstance(allotrope, Allotrope))
    @icontract.require(lambda amount: isinstance(amount, int))
    @icontract.require(lambda amount: amount >= 0)
    def withdraw_asset(self, allotrope: Allotrope, amount: int) -> bool:
        if amount <= 0:
            return True

        cash = self.assets.get(allotrope, 0)
        if cash < amount:
            return False
        self.assets[allotrope] = cash - amount
        return True

    @icontract.require(lambda allotrope: isinstance(allotrope, Allotrope))
    def get_asset(self, allotrope: Allotrope):
        return self.assets.get(allotrope, 0)

    @icontract.require(lambda star: star is None or isinstance(star, Celestial))
    def set_star(self, star: Star, now: int):
        """Sets the star this hq is assigned to, updates position to reflect that of the
        star

        """

        if not star:
            self.star = None
            return True
        return self.jumpto(star.position, now)

    @icontract.require(lambda harvester: isinstance(harvester, Harvester))
    @icontract.require(lambda harvester: harvester.amount >= 0)
    @icontract.require(
        lambda harvester: isinstance(
            harvester.harvester_classification.allotrope, Allotrope
        )
    )
    @icontract.ensure(lambda harvester: harvester.amount == 0)
    def empty(self, harvester: Harvester):
        allotrope = harvester.harvester_classification.allotrope
        mined = harvester.reset()
        self.add_allotrope(allotrope, mined)

    @icontract.require(lambda amount: amount >= 0)
    @icontract.require(lambda amount: isinstance(amount, int))
    @icontract.require(lambda allotrope: isinstance(allotrope, Allotrope))
    def add_allotrope(self, allotrope: Allotrope, amount: int):
        self.assets[allotrope] = self.get_asset(allotrope) + amount

    @icontract.require(lambda harvester: isinstance(harvester, Harvester))
    def register_harvester(self, harvester: Harvester):
        if harvester not in self.harvesters:
            self.harvesters.append(harvester)

    def tick(self, now: int):
        for harvester in self.harvesters:
            if harvester.destroyed():
                pass  # TODO perform GC
            elif not harvester.is_harvesting() and harvester.at_hq:
                harvested = harvester.reset()
                allotrope = harvester.harvester_classification.allotrope
                self.add_allotrope(allotrope, harvested)

    def __str__(self) -> str:
        hvs = len(self.harvesters)
        ass = ", ".join([f"{k}:{v}" for k, v in self.assets.items()])
        return f"🏰\tHQ ({self.owner.name}) — {hvs} harvesters,  assets: {ass}"
