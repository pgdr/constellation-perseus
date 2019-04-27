import enum

class GameObjectState(enum.Enum):

    #
    # Game object is not doing anything of significance
    #
    IDLE = enum.auto()

    #
    # Object is harvesting
    #
    HARVESTING = enum.auto()

    #
    # Game object has ceased from being
    #
    DESTROYED = enum.auto()

    TRAVELLING = enum.auto()

    DEFENDING = enum.auto()

    ATTACKING = enum.auto()

    BUILDING = enum.auto()

