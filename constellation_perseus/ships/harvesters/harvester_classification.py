"""Defines the harvester type, what it harvests/mines and at what speed it does
so.

@author pgd

"""


from dataclasses import dataclass

@dataclass
class HarvesterClassification(enum):

    harvestSpeed: float
    allotrope: Allotrope

    def __str__(self):
        return f"{self.name}: {self.speed} {self.allotrope}"


SPICE_SHIP = HarvesterClassification(2, Allotrope.SULFUR)  #  get it?
CARBON_COLLECTOR = HarvesterClassification(76, Allotrope.CARBON)
PHOSPORUS_MINER = HarvesterClassification(12, Allotrope.PHOSPORUS)
OXYGEN_MINER = HarvesterClassification(97, Allotrope.OXYGEN)
SULFUR_MINER = HarvesterClassification(16, Allotrope.SULFUR)
SELENIUM_MINER = HarvesterClassification(72, Allotrope.SELENIUM)
DYSON_SPHERE = HarvesterClassification(450, Allotrope.OXYGEN)
