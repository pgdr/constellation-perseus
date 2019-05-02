from dataclasses import dataclass, field
from typing import Dict

from .harvester import Harvester
from .harvester_classification import HarvesterClassifications, HarvesterClassification
from ... import Allotropes, Allotrope


def _price_fac():
    return {Allotropes.CARBON: 1000}


@dataclass(eq=False)
class BasicCarbonHarvester(Harvester):
    COOLDOWN_TIME: int = 2000  # 2 sec
    CAPACITY: int = 13500

    PRICE: Dict[Allotrope, int] = field(default_factory=_price_fac)

    harvester_classification: HarvesterClassification = HarvesterClassifications.CARBON_COLLECTOR.value

    def __str__(self):
        return f"⛴\tC-Harvester: {self.amount} Carbon"
