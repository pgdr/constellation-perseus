@dataclass
class SpaceStation(GameObject):
    damage: float = 1.0
    position: Position
    name: str
    default_hq: Hq
    owner: Player

    def under_construction(self):
        return False

        def __str__(self):
            if self.is_under_construction():
                return f"{self.name} (under construction)"

            return self.name
