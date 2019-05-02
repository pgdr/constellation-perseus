from typing import List
from dataclasses import dataclass, field

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
        return int((100.0 * self.amount) / self.capacity)

    def is_full(self):
        return self.amount >= self.capacity

    def is_empty(self):
        return self.amount <= 0

    def reset(self):
        amount = self.amount
        self.amount = 0
        return amount

    def set_star(self, star: Star, now: int):
        if not star:
            self.star = None
            return True

        if star == self.star:
            return True

        if not self.canjump(now):
            return False

        self.jumpto(star.position, now)
        self.star = star
        self.at_hq = False
        return True

    def tick(self, now: int):
        if self.at_hq and not self.is_empty():
            self.default_hq.empty(self)

        if self.star:
            star_all = self.star.sc.allotrope
            harv_all = self.harvester_classification.allotrope
            harv_speed = self.harvester_classification.speed
            if star_all == harv_all:
                self.amount += harv_speed
            if self.amount > self.capacity:
                self.amount = self.capacity
        print(f"Harvester fill level = {self.amount}")

    def is_harvesting(self):
        return self.state == GameObjectState.HARVESTING

    def send_home(self, s: Star, now: int):
        if self.jumpto(s.position, now):
            self.at_hq = True
            self.star = None
            return True
        return False
