"""This class controls the main logic behind the game, and keeps complete lists
  for the main objects in this game: players, celestials and ships.

@author pgd

"""

from typing import List, Dict
import time

from . import Player, HumanPlayer, Harkonnen, Stars, Hq, Shipyard

from .celestials import Celestial
from .ships import Ship, ColonialViper
from .stations import SpaceStation
from .position import Position
from .gameobject import GameObject

import icontract


class Soundsystem:
    @staticmethod
    def get_sound_system():
        pass


from dataclasses import dataclass, field


@dataclass(eq=False, frozen=False)
class Game:
    instance: "Game" = None

    initialize_time: int = time.time()
    players: List[Player] = field(default_factory=list)
    celestials: List[Celestial] = field(default_factory=list)
    ships: List[Ship] = field(default_factory=list)
    stations: List[SpaceStation] = field(default_factory=list)
    contributors: List[str] = field(default_factory=list)
    soundsystem: Soundsystem = Soundsystem.get_sound_system()

    pos_to_obj: Dict[Position, GameObject] = field(default_factory=dict)
    obj_to_pos: Dict[GameObject, Position] = field(default_factory=dict)

    is_instantiated: bool = False
    _tick_id: int = 0

    def setup(self):
        if self.instance:
            raise RuntimeError("Can only instantiate game once")
        self.instance = self
        Game.instance = self
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

        hqship = Hq(name="HeadQuarter", star=Stars.SOL, owner=human)
        human.add_hq(hqship)
        add(hqship, pos_from=hqship.star)

        yard = Shipyard(default_hq=hqship, owner=human)
        add(yard, pos=self.get_position(hqship) + Position(0, 50, 0))

        self.set_contributors()

        for _ in range(6):
            v = ColonialViper(Stars.ELECTRA.position, owner=human)
            add(v, Stars.ELECTRA.position)

        harkonnen_hq = Hq(name="Harkonnen", star=Stars.PLEIONE, owner=harkonnen)
        harkonnen.add_hq(harkonnen_hq)
        add(harkonnen_hq, pos_from=harkonnen_hq.star)

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
        if not ship.canjump(self.now()):
            return None

        ship.jumpto(self.obj_to_pos[cel], self.now())
        return self.assign_position(ship, self.obj_to_pos[cel])

    @icontract.require(lambda obj: isinstance(obj, GameObject))
    @icontract.require(lambda pos: isinstance(pos, Position))
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

        if obj in self.obj_to_pos:
            oldpos = self.obj_to_pos[obj]
            if oldpos == pos:
                return None  # nothing to do
            del self.pos_to_obj[oldpos]
        self.obj_to_pos[obj] = pos
        self.pos_to_obj[pos] = obj
        return pos

    def get_position(self, obj: GameObject) -> Position:
        return self.obj_to_pos.get(obj)

    def get_closest_enemy_ship(self, pos: Position):
        return None  #

    @icontract.ensure(lambda result: isinstance(result, Position))
    def add(self, obj: GameObject, pos: Position = None, pos_from: GameObject = None):
        if pos is None:
            pos = self.get_position(pos_from)
        if pos is None:
            try:
                pos = pos_from.position
            except:
                pass
        if pos is None and pos_from is not None:
            raise ValueError(f"Unable to get position from {pos_from}.")
        if pos is None:
            try:
                pos = obj.position
            except AttributeError:
                raise ValueError(f"Position cannot be None for Game.add({obj})")

        regs = {
            Ship: self.ships,
            Celestial: self.celestials,
            SpaceStation: self.stations,
        }
        for k, v in regs.items():
            if isinstance(obj, k):
                v.append(obj)
                break
        else:
            print(f"Game.add received unknown type {type(obj)}")

        return self.assign_position(obj, pos)

    def get(self, target: Position, range_: float = 1.0) -> GameObject:
        """Return the object closest to given position or None if no object is closer
        than range.
        """

        assert isinstance(
            target, Position
        ), f"wrong type on target, expected Position, was {type(target)}"
        # async with asyncio.Lock():
        opt_dist = 10 ** 10
        opt_obj = None
        for pos, obj in self.pos_to_obj.items():
            dist = target.distance(pos)
            if dist < opt_dist:
                opt_obj = obj
                opt_dist = dist

        if opt_dist > range_:
            return None

        return opt_obj

    def tick(self):
        self._tick_id += 1

        def T(o):
            o.tick(self.now())

        # TODO with asyncio.Lock():
        print("\n" * 2)
        print(f"🕑 {self._tick_id} {round(self.now(),2)}".center(20).center(40, "="))
        print("\n")
        print(f"{len(self.players)} players!")
        print(f"{len(self.celestials)} celestials")
        print(f"{len(self.stations)} stations")
        print(f"{len(self.ships)} ships")

        for station in self.stations:
            print(station, self.get_position(station))

        for ship in self.ships:
            print(ship, self.get_position(ship))

        for obj in self.players + self.celestials + self.stations + self.ships:
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
        if not self.instance:
            self.setup()

        for i in range(100):
            time.sleep(1)
            print(f"{i}\ttick {time.time()}")
            self.tick()

    def dispatch(self, *args, **kwargs):
        pass
