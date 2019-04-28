"""This class controls the main logic behind the game, and keeps complete lists
  for the main objects in this game: players, celestials and ships.

@author pgd

"""

from typing import List, Dict

# import asyncio
import time

from . import Player, HumanPlayer, Harkonnen, Stars, Hq, Shipyard

from .celestials import Celestial
from .ships import Ship, ColonialViper
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
        self.instance = self
        Game.instance = self

    def _setup(self):
        self.initialize_time = time.time()
        human = HumanPlayer()
        harkonnen = Harkonnen()
        self.players = [human, harkonnen]

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

        hqship = Hq(name="HeadQuarter", owner=human)
        human.add_hq(hqship)
        add(hqship, Stars.SOL.position)
        hqship.set_star(Stars.SOL)

        yardpos = None  # self.get_position(hqship).add(Position(0, 50, 0))
        yard = Shipyard(yardpos, hqship, human)
        add(yard)

        self.set_contributors()

        for i in range(6):
            v = ColonialViper(Stars.ELECTRA.position, human)
            add(v, Stars.ELECTRA.position)

        harkonnen_hq = Hq("Harkonnen", Stars.PLEIONE.position, harkonnen)
        harkonnen.add_hq(harkonnen_hq)
        add(harkonnen_hq, Stars.PLEIONE.position)
        harkonnen_hq.set_star(Stars.PLEIONE)

    def get_human_player(self):
        return self.players[0]

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
        return 1000.0 * (n - self.initialize_time)

    # @icontract...
    def send_ship_to_celestial(self, ship: Ship, cel: Celestial) -> Position:
        """"
        Returns None if ship not ready to jump
        """
        if not ship.isReadyToJump():
            return None

        ship.jumpto(self.obj_to_pos[cel])
        return self.assign_position(ship, self.obj_to_pos[cel])

    def assign_position(self, obj: GameObject, pos: Position) -> Position:
        """Finds the nearest uninhabitated position in space and puts obj there.  This
        method calls setPosition on obj with the position it returns.  Returns
        the position it was moved to.

        """
        try:
            print(obj)
            print(pos)
        except TypeError as e:
            print(" " * 30, e)
        # lock = asyncio.Lock()
        # async with lock:
        if obj in self.obj_to_pos:
            oldpos = self.obj_to_pos[obj]
            if oldpos == pos:
                return None  # nothing to do
            self.obj_to_pos[obj] = pos
            self.pos_to_obj[oldpos] = None
            self.pos_to_obj[pos] = obj
        return pos

    def get_position(self, obj: GameObject) -> Position:
        return self.obj_to_pos.get(obj)

    def get_closes_enemy_ship(self, pos: Position):
        return None  # TODO implement

    # @singledispatch
    def add(self, obj: GameObject, pos: Position = None):
        if isinstance(obj, Ship):
            self.ships.append(obj)
        elif isinstance(obj, Celestial):
            self.celestials.append(obj)
        elif isinstance(obj, SpaceStation):
            self.stations.append(obj)
        if pos is None:
            assert (
                "position" in obj.__dict__
            ), f"Game.add needs position argument for type {type(obj)}."
            self.assign_position(obj, obj.position)
        else:
            self.assign_position(obj, pos)

    def get(self, target: Position, range_: float) -> GameObject:
        """Returns the object closest to given position. Returns null if no object is
        closer than range.

        """

        # async with asyncio.Lock():
        opt_dist = 10 ** 10
        opt_obj = None
        opt_pos = None
        for pos, obj in self.pos_to_obj.items:
            dist = target.distance(pos)
            if dist < opt_dist:
                opt_obj = obj
                opt_pos = pos
                opt_dist = dist

        if opt_dist > range_:
            return None

        return opt_obj

    def tick(self):
        def T(o):
            o.tick(self.now())

        # TODO with asyncio.Lock():
        print("\n" * 3)
        print("===" * 10)
        print("\n" * 3)
        print(f"{len(self.players)} players!")
        print(f"{len(self.celestials)} celestials")
        print(f"{len(self.stations)} stations")
        print(f"{len(self.ships)} ships")

        for obj in self.players + self.celestials + self.stations + self.ships:
            # try:
            #     print(f'ticking {obj}')
            # except Exception as e:
            #     print(f'ticking type {type(obj)}')
            T(obj)

    def __str__(self):
        def ntjoin(lst, header=""):
            return header + "\n\t".join([str(obj) for obj in lst])

        return (
            ntjoin(self.players, "Players:")
            + ntjoin(self.celestials, "Celestials:")
            + ntjoin(self.stations, "Stations:")
            + ntjoin(self.ships, "Ships:")
        )

    def set_contributors(self):
        self.contributors = ["Jonas Grønås Drange", "Pål Grønås Drange"]

    def run(self):
        for i in range(100):
            time.sleep(1)
            print(f"{i}\ttick {time.time()}")
            self.tick()
