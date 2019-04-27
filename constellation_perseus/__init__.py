import asyncio

import constellation_perseus

from .assets import Allotrope, Allotropes
from .position import Position
from .gameobjectaction import GameObjectAction
from .gameobjectstate import GameObjectState

from .message import Message

from .players.player import Player

from .gameobject import GameObject


from .weapons import Gun

from .celestials import Celestial, Star

from .ships import Hq


def game_loop():
    asyncio.get_event_loop()
