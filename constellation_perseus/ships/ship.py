from dataclasses import dataclass


@dataclass
class Ship(GameObject):

    price: dict[Allotrope, int]
    guns: list[Gun]
    name: str
    classification: ShipClassification
    damage: float = 1
    state: GameObjectState = GameObjectState.IDLE
    pos: Position
    cooldowntime: int
    lastjumptime: int = -10 ** 10
    owner: Player
    actions: list[GameObjectActions]

    def price_of(self, a: Allotrope):
        return price.get(a, 0)

    def canjump(self):
        return self.cooldowntime == 0

    def remaining_cooldowntime(self):
        if lastjumptime == -10 ** 10:
            return 0
        now = Game.now()
        return max(0, now - lastjumptime)

    def jumpto(pos: Position):
        if not self.canjump():
            return False
        Game.instance().assign_position(self, pos)
        lastJumpTime = Game.now()
        return True

    def __str__(self):
        s = "Ship " + classification

        if not self.canjump():
            s += " (cooling down ... "
            s += (getCooldownTimeLeft() / 1000) + ")"
        return s

    def destructor(self):
        return True

    def destroy(self):
        if self.destructor():
            setState(GameObjectState.DESTROYED)

    def destroyed(self):
        self.state == GameObjectState.DESTROYED

    def idle(self):
        return self.state == GameObjectState.IDLE
