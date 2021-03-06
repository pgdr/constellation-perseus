"""House Harkonnen, from the volcanic wastelands of Giedi Prime.  The Harkonnen
know only malevolence, hatred and brutality.  Their leader is the corrupt and
vile Baron Rakan.  Rakan's power-hungry sons — Gunseng and Copec — eagerly await
the Baron's death.  Each plots to take his place.  But while he lives, they feed
upon him like parasites.

@author pgd

"""
from typing import List
from dataclasses import dataclass, field

import icontract

from .player import Player
from .. import Star, Stars, Position
from .. import Ship
from .. import ColonialViper
from ..ships.harvesters import Harvester, BasicCarbonHarvester, BasicOxygenHarvester
from ..stations import Shipyard


@dataclass(eq=False)
class Harkonnen(Player):

    yard: Shipyard = None
    basepos: Position = Stars.PLEIONE.position
    ships: List[Ship] = field(default_factory=list)
    harvesters: List[Harvester] = field(default_factory=list)
    last_tick: int = -1
    name: str = "Harkonnen"

    THINK_TIME: int = 25
    INIT_TIME: int = 3000

    def tick(self, now: int):
        if now < self.INIT_TIME:
            return
        if self.last_tick == -1:
            self.last_tick = now
            return
        if self.last_tick + self.THINK_TIME > now:
            return
        self.last_tick = now

        if len(self.ships) < 5:
            self.init_phase(now)
            return

        if len(self.ships) <= 20:
            self.develop_phase(now)
            return

        self.kill_phase(now)

    def kill_phase(self, now: int):
        from constellation_perseus import Game

        print("HARKONNEN KILL")
        enemy = Game.instance.get_closest_enemy_ship(self.hq)
        if not enemy:
            return
        enemy_pos = Game.instance.get_position(enemy)

        non_ready = 0
        for ship in self.ships:
            if not ship.ready():
                non_ready += 1
        if non_ready > 0:
            return  #  wait until we're all ready and then KILL!

        for s in self.ships:
            s.jumpto(enemy_pos)

    @icontract.require(lambda idx: isinstance(idx, int))
    @icontract.require(lambda idx: idx >= 0)
    @icontract.require(lambda to_star: isinstance(to_star, Star))
    def _hvs_logistic(self, idx: int, to_star: Star, now: int):
        """ move hvs[idx] home if full, to star if empty, return [if action]"""
        hv = self.harvesters[idx]
        if hv.is_empty():
            hv.set_star(to_star, now)
            return True
        elif hv.is_full():
            hv.send_home(now)
            print("is full!!")
            return True
        return False

    def develop_phase(self, now: int):
        print("HARKONNEN DEVELOP")
        self._hvs_logistic(idx=0, to_star=Stars.ATLAS, now=now)
        self._hvs_logistic(idx=1, to_star=Stars.ALCYONE, now=now)

        if len(self.harvesters) == 2:
            self.build_carbon_miner()
            return

        if len(self.harvesters) == 3:
            self.build_oxygen_miner()
            return

        self._hvs_logistic(2, Stars.ATLAS, now=now)
        self._hvs_logistic(3, Stars.ALCYONE, now=now)

        if len(self.ships) < 20:
            self.build_viper()

    def init_phase(self, now: int):
        print("HARKONNEN INIT")
        hvs = self.harvesters
        if not self.yard:
            self.build_shipyard()
            return

        if self.yard.is_under_construction():
            print("Harkonnen waiting ...")
            return

        if not hvs:
            self.build_carbonminer()
            print("HARKONNEN CARBON")
            return

        if self._hvs_logistic(0, Stars.ATLAS, now):
            return

        if len(hvs) == 1:
            self.build_oxygenminer()
            return

        if self._hvs_logistic(1, Stars.ALCYONE, now):
            return

        if len(self.ships) <= 5:
            self.build_viper()
            return

    def build_viper(self):
        from constellation_perseus import Game

        v = ColonialViper(Game.instance.get_position(Stars.MAIA), owner=self)
        if Game.instance.buy(v, self):
            print("HARKONNEN BUILDING VIPER!")
            self.yard.construct_ship(v, Game.instance.now())
            self.ships.append(v)
        else:
            print("HARKONNEN TO POOR FOR VIPER :(")

    def build_oxygenminer(self):
        from constellation_perseus import Game

        print("HARKONNEN builds oxygen miner.")

        hv = BasicOxygenHarvester(star=Stars.PLEIONE, default_hq=self.hq, owner=self)
        if Game.instance.buy(hv, self):
            self.yard.construct_ship(hv, Game.instance.now())
            self.harvesters.append(hv)

    def build_carbonminer(self):
        from constellation_perseus import Game

        print("HARKONNEN builds carbon miner.")

        hv = BasicCarbonHarvester(star=Stars.PLEIONE, default_hq=self.hq, owner=self)

        if Game.instance.buy(hv, self):
            self.yard.construct_ship(hv, Game.instance.now())
            self.harvesters.append(hv)

    def build_shipyard(self):
        from constellation_perseus import Game

        self.yard = Shipyard(default_hq=self.hq, owner=self)
        Game.instance.add(self.yard, self.basepos)

    def __str__(self):
        return "Harkonnen"

    def __repr__(self):
        return "Harkonnen"
