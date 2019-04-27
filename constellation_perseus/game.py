"""This class controls the main logic behind the game, and keeps complete lists
  for the main objects in this game: players, celestials and ships.

@author pgd

"""

from typing import List, Dict
import asyncio
import time

from . import Player, HumanPlayer, Harkonnen, Star, Stars, Hq, Shipyard

from .celestials import Celestial
from .ships import Ship
from .stations import SpaceStation
from .position import Position
from .gameobject import GameObject


class Soundsystem:
    @staticmethod
    def get_sound_system():
        pass


class Game:
    initialize_time: int
    players: List[Player] = []
    celestials: List[Celestial] = []
    ships: List[Ship] = []
    stations: List[SpaceStation] = []
    contributors: List[str] = []
    soundsystem: Soundsystem = Soundsystem.get_sound_system()

    pos_to_obj: Dict[Position, GameObject] = {}
    obj_to_pos: Dict[GameObject, Position] = {}

    is_instantiated: bool = False

    instance: "Game"

    def __init__(self):
        self._setup()

    def _setup(self):
        human = HumanPlayer()
        harkonnen = Harkonnen()
        players = [human, harkonnen]

        add = self.add
        add(Stars.SOL)

        add(Stars.ALCYONE)
        add(Stars.ATLAS)
        add(Stars.ELECTRA)
        add(Stars.MAIA)
        add(Stars.MEROPE)

        add(Stars.TAYGETA)
        add(Stars.PLEIONE)
        add(Stars.CELAENO)
        add(Stars.STEROPE)
        add(Stars.ASTEROPE)

        hqship = Hq(
            name="HeadQuarter",
            position=self.get_position(Stars.SOL),
            yield_=None,
            owner=human,
        )
        human.add_hq(hqship)
        add(hqship)
        hqship.star = Stars.SOL

        yard = Shipyard(hqship.position.add(Position(0, 50, 0)), hqship, human)
        add(yard)

        self.set_contributors()

        for i in range(6):
            v = ColonialViper(Stars.ELECTRA.position, human)
            add(v)

        harkonnen_hq = Hq("Harkonnen", Stars.PLEIONE.position, harkonnen)
        harkonnen.add_hq(harkonnenHq)
        add(harkonnenHq)
        harkonnen_hq.star = Stars.PLEIONE

    def get_human_player(self):
        return players.get(0)

    def buy(self, ship: Ship, player: Player):
        """ Returns true if player can afford to buy ship AND the money is withdrawn
        from the Hq's assets!"""
        hq = player.hq
        return hq.buy(ship)

    def now(self) -> int:
        """
        Returns the current time in milliseconds relative to when the game
        started, i.e. it will be 0 immediately when the game starts.
        """

        n = time.time()
        return n - initialize_time

    # @icontract...
    def send_ship_to_celestial(self, ship: Ship, cel: Celestial) -> Position:
        """"
        Returns None if ship not ready to jump
        """
        if not ship.isReadyToJump():
            return

        ship.jumpto(objToPos[cel])
        return self.assign_position(ship, objToPos[cel])

    async def assign_position(self, obj: GameObject, pos: Position) -> Position:
        """Finds the nearest uninhabitated position in space and puts obj there.  This
        method calls setPosition on obj with the position it returns.  Returns
        the position it was moved to.

        """
        lock = asyncio.Lock()
        async with lock:
            if obj in objToPos:
                oldpos = objToPos[obj]
                if oldPos == position:
                    return position  # nothing to do
                obj_to_pos[obj] = pos
                pos_to_obj[oldpos] = None
                pos_to_obj[pos] = obj

    def get_position(self, obj: GameObject) -> Position:
        return self.obj_to_pos.get(obj)

    # @singledispatch
    def add(self, obj: GameObject):
        if isinstance(obj, Ship):
            self.ships.append(obj)
        elif isinstance(obj, Celestial):
            self.celestials.append(obj)
        elif isinstance(obj, Spacestation):
            self.stations.append(obj)

        self.assign_position(obj, obj.position)

    async def get(self, target: Position, range_: float) -> GameObject:
        """Returns the object closest to given position. Returns null if no object is
        closer than range.

        """

        async with asyncio.Lock():
            opt_dist = 10 ** 10
            opt_obj = None
            opt_pos = None
            for pos, obj in self.pos_to_obj.items:
                dist = target.distance(pos)
                if dist < optDist:
                    opt_obj = obj
                    opt_pos = pos
                    opt_dist = dist

        if optDist > range_:
            return None

        return opt_obj

    def tick(self):
        def T(o):
            o.tick(self.now())

        with asyncio.Lock():
            for obj in players + celestials + stations + ships:
                T(obj)

    def __str__(self):
        def ntjoin(lst, header=""):
            return header + "\n\t".join([str(obj) for obj in lst])

        return (
            ntjoin(players, "Players:")
            + ntjoin(celestials, "Celestials:")
            + ntjoin(stations, "Stations:")
            + ntjoin(ships, "Ships:")
        )

    def set_contributors(self):
        self.contributors = ["Jonas Grønås Drange", "Pål Grønås Drange"]
