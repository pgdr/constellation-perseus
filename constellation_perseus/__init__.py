import asyncio

import constellation_perseus

from .assets import Allotrope, Allotropes
from .position import Position
from .gameobjectaction import GameObjectAction
from .gameobjectstate import GameObjectState

from .message import Message

from .players.player import Player
from .players import HumanPlayer

from .gameobject import GameObject


from .weapons import Gun, ViperMissile, KineticEnergyWeapon

from .celestials import Celestial, Star
from .ships import ShipClassification
from .ships import Ship
from .ships import ColonialViper

from .ships import Hq
from .stations import SpaceStation, Shipyard

# from .players import Harkonnen


def game_loop():
    asyncio.get_event_loop()
