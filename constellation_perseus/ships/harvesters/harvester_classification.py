"""Defines the harvester type, what it harvests/mines and at what speed it does
so.

@author pgd

"""

import enum

from dataclasses import dataclass
from ... import Allotropes, Allotrope


@dataclass
class HarvesterClassification:

    speed: float
    allotrope: Allotrope

    def __str__(self):
        return f"{self.name}: {self.speed} {self.allotrope}"


class HarvesterClassifications(enum.Enum):
    SPICE_SHIP = HarvesterClassification(2, Allotropes.SULFUR.value)  #  get it?
    CARBON_COLLECTOR = HarvesterClassification(76, Allotropes.CARBON.value)
    PHOSPORUS_MINER = HarvesterClassification(12, Allotropes.PHOSPORUS.value)
    OXYGEN_MINER = HarvesterClassification(97, Allotropes.OXYGEN.value)
    SULFUR_MINER = HarvesterClassification(16, Allotropes.SULFUR.value)
    SELENIUM_MINER = HarvesterClassification(72, Allotropes.SELENIUM.value)
    DYSON_SPHERE = HarvesterClassification(450, Allotropes.OXYGEN.value)
