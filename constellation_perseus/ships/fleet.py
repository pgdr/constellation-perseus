@dataclass
class Fleet(GameObject):

    ships: list[Ship]
    position: Position
    name: str

    actions: list[GameObjectActions]
    owner: Player

    def _ready(self):
        return all([s.ready() for s in self.ships])

    def jumpto(pos: Position):
        if not self._ready():
            return False
        for s in ships:
            s.jumpto(pos)
        self.position = pos

    def tick(self, time: int):
        # a fleet is more like an abstract concept so no action necessary
        pass

    def damage(self):
        return 0  # a fleet isn't damaged
