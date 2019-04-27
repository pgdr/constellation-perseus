import enum

class ShipClassification(enum.Enum):

    HQ = enum.auto()  # The head quarter of a player.
    HARVESTER = enum.auto()  # a harvester ship
    CARRIER = enum.auto()
    BATTLESHIP = enum.auto()
    VIPER = enum.auto()
    #
    # Lightly armored spaceship with no weapons. It is able to quickly
    # transport harvesters, but also large batches of vipers.
    #
    CARYALL = enum.auto()
