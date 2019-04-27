from typing import List

from ... import GameObjectAction

from .. import Ship
from .. import ShipClassification
from ... import Star

# from .. import Hq
from .harvester_classification import HarvesterClassification


class Harvester(Ship):
    star: Star  # The star it is connected to, might be None
    harvester_classification: HarvesterClassification
    ship_classification: ShipClassification = ShipClassification.HARVESTER
    amount: int
    capacity: int
    default_hq: object  # TODO Hq
    at_hq: bool = False
    actions = List[GameObjectAction]

    def percentage(self):
        if self.isfull():
            return 100
        if self.isempty():
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

    def set_star(star: Star):
        if not star:
            self.star = None
            return True

        if star == self.star:
            return True

        if not self.ready():
            return False

        self.jumpto(star.position)
        self.star = star
        self.at_hq = False
        return True

    def tick(self, time: int):
        if self.at_hq and not self.isempty():
            default_hq.empty(self)

        if star:
            if star.classification.allotrope == harvester_classification.allotrope:
                amount += harvester_classification.speed
            if self.amount > self.capacity:
                self.amount = self.capacity

        def is_harvesting(self):
            return self.state == GameObjectState.HARVESTING

        def send_home(s: Hq):
            if self.jumpto(s.position):
                at_hq = True
                star = None
                return True
            return False
