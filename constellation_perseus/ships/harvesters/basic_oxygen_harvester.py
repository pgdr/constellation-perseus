@dataclass
class BasicOxygenHarvester(Harvester):
    COOLDOWN_TIME: int = 3000  # 3 sec
    CAPACITY: int = 16000

    PRICE: dict[Allotrope, int] = {Allotrope.OXYGEN: 1000}

    harvester_classification = HarvesterClassification.OXYGEN_MINER

    def __str__(self):
        return f"O-Harvester: {self.amount} Oxygen"
