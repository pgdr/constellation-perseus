import asyncio

import constellation_perseus

from .assets import Allotrope, Allotropes
from .position import Position
from .gameobjectaction import GameObjectAction
from .gameobjectstate import GameObjectState

from .message import Message
from .gameobject import GameObject

from .celestials import Celestial, Star, Stars


from .weapons import Gun, ViperMissile, KineticEnergyWeapon

from .players.player import Player
from .players import HumanPlayer


from .ships import ShipClassification
from .ships import Ship
from .ships import ColonialViper

#from .players.harkonnen import Harkonnen

from .ships import Hq

from .stations import SpaceStation, Shipyard


def game_loop():
    asyncio.get_event_loop()
