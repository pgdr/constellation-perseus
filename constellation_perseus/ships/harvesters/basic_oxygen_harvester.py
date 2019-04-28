from dataclasses import dataclass, field
from typing import Dict

from .harvester import Harvester
from .harvester_classification import HarvesterClassifications, HarvesterClassification
from ... import Allotropes, Allotrope


def _price_fac():
    return {Allotropes.OXYGEN: 1000}


@dataclass(eq=False)
class BasicOxygenHarvester(Harvester):
    COOLDOWN_TIME: int = 3000  # 3 sec
    CAPACITY: int = 16000

    PRICE: Dict[Allotrope, int] = field(default_factory=_price_fac)

    harvester_classification: HarvesterClassification = HarvesterClassifications.OXYGEN_MINER

    def __str__(self):
        return f"O-Harvester: {self.amount} Oxygen"
