from typing import List
from dataclasses import dataclass, field
import icontract

from ... import GameObjectState, GameObjectAction

from .. import Ship
from .. import ShipClassification
from ... import Star

from .harvester_classification import HarvesterClassification


@dataclass(eq=False)
class Harvester(Ship):
    star: Star = None  # The star it is connected to, might be None
    harvester_classification: HarvesterClassification = None
    classification: ShipClassification = ShipClassification.HARVESTER
    amount: int = 0
    capacity: int = 1000
    default_hq: "Hq" = None  # TODO Hq
    at_hq: bool = False
    actions: List[GameObjectAction] = field(default_factory=list)

    def percentage(self):
        if self.is_full():
            return 100
        if self.is_empty():
            return 0
        return int((100.0 * self.amount) / float(self.capacity))

    def is_full(self):
        return self.amount >= self.capacity

    def is_empty(self):
        return self.amount <= 0

    def reset(self):
        amount = self.amount
        self.amount = 0
        return amount

    @icontract.require(lambda star: isinstance(star, Star))
    @icontract.require(lambda now: isinstance(now, int))
    def set_star(self, star: Star, now: int):
        if star == self.star:
            return True

        if not self.canjump(now):
            return False

        self.state = GameObjectState.JUMPING
        self.jumpto(star.position, now)
        self.star = star
        self.at_hq = False
        return True

    def tick(self, now: int):
        print(f"{self} -> {self.amount} ({self.percentage()})% [{self.state}]")
        if self.at_hq and not self.is_empty():
            self.state = GameObjectState.EMPTYING
            self.default_hq.empty(self)
        elif self.at_hq and self.is_empty():
            self.state = GameObjectState.IDLE
        elif self.star:
            self.state = GameObjectState.HARVESTING
            star_all = self.star.sc.allotrope
            harv_all = self.harvester_classification.allotrope
            harv_speed = self.harvester_classification.speed
            if star_all == harv_all:
                self.amount += harv_speed
                print(
                    f"\n\t harvesting  star:{star_all} & harv_all:{harv_all} -> {harv_speed} (cap={self.capacity})"
                )
            else:
                print(f"\n\t wrong type!!!  star:{star_all} & harv_all:{harv_all}")
            if self.amount > self.capacity:
                self.amount = self.capacity
        hqstr = "at hq" if self.at_hq else "not at hq"
        starstr = "at star" if self.star else "not at star"
        print(f"Harvester fill level = {self.amount} {hqstr} {starstr}")

    def is_harvesting(self):
        return self.state == GameObjectState.HARVESTING

    @icontract.require(lambda self: isinstance(self.default_hq, "Hq"))
    def send_home(self, now: int):
        if self.jumpto(s.position, now):
            self.at_hq = True
            self.star = None
            return True
        return False
