import enum


class GameObjectState(enum.Enum):

    IDLE = enum.auto()

    HARVESTING = enum.auto()

    EMPTYING = enum.auto()

    FUELLING = enum.auto()

    # Game object has ceased from being
    DESTROYED = enum.auto()

    TRAVELLING = enum.auto()

    DEFENDING = enum.auto()

    ATTACKING = enum.auto()

    BUILDING = enum.auto()

    JUMPING = enum.auto()
