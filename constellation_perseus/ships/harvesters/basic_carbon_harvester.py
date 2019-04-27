from dataclasses import dataclass

@dataclass
class BasicCarbonHarvester(Harvester):
    COOLDOWN_TIME: int = 2000  # 2 sec
    CAPACITY: int = 13500

    PRICE: dict[Allotrope, int] = {Allotrope.CARBON: 1000}

    harvester_classification = HarvesterClassification.CARBON_COLLECTOR

    def __str__(self):
        return f"C-Harvester: {self.amount} Carbon"
