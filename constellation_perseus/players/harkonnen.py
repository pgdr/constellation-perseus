"""House Harkonnen, from the volcanic wastelands of Giedi Prime.  The Harkonnen
know only malevolence, hatred and brutality.  Their leader is the corrupt and
vile Baron Rakan.  Rakan's power-hungry sons — Gunseng and Copec — eagerly await
the Baron's death.  Each plots to take his place.  But while he lives, they feed
upon him like parasites.

@author pgd

"""
from typing import List
from dataclasses import dataclass, field
from .player import Player
from .. import Star, Stars, Position
from .. import Ship
from ..ships.harvesters import Harvester, BasicCarbonHarvester, BasicOxygenHarvester
from ..stations import Shipyard


@dataclass
class Harkonnen(Player):

    yard: Shipyard = None
    basepos: Position = Stars.PLEIONE.position
    ships: List[Ship] = field(default_factory=list)
    harvesters: List[Harvester] = field(default_factory=list)
    last_tick: int = -1
    name: str = "Harkonnen"

    THINK_TIME: int = 25
    INIT_TIME: int = 3000

    def tick(self, time: int):
        print(f"tick {time}")
        if time < self.INIT_TIME:
            return
        if self.last_tick == -1:
            self.last_tick = time
            return
        if self.last_tick + self.THINK_TIME > time:
            return
        self.last_tick = time

        if len(self.ships) < 5:
            self.init_phase()
            return

        if len(self.ships) <= 20:
            self.develop_phase()
            return

        self.kill_phase()

    def kill_phase(self):
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

    def _hvs_logistic(self, idx, to_star):
        """ move hvs[idx] home if full, to star if empty, return [if action]"""
        hv = self.harvesters[idx]
        if hv.is_empty():
            hv.star = to_star
            return True
        elif hv.is_full():
            hv.send_home(self.hq)
            return True
        return False

    def develop_phase(self):
        print("HARKONNEN DEVELOP")
        self._hvs_logistic(0, Stars.ATLAS)
        self._hvs_logistic(1, Stars.ALCYONE)

        if len(harvesters) == 2:
            self.build_carbon_miner()
            return

        if len(harvesters) == 3:
            self.build_oxygen_miner()
            return

        self._hvs_logistic(2, Stars.ATLAS)
        self._hvs_logistic(3, Stars.ALCYONE)

        if len(ships) < 20:
            self.build_viper()

    def init_phase(self):
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

        if self._hvs_logistic(0, Stars.ATLAS):
            return

        if len(hvs) == 1:
            self.build_oxygenminer()
            return

        if self._hvs_logistic(1, Stars.ALCYONE):
            return

        if len(self.ships) <= 5:
            self.build_viper()
            return

    def build_viper(self):
        from constellation_perseus import Game

        v = ColonialViper(Game.instance.get_position(Stars.MAIA), self)
        if Game.instance.buy(v, self):
            print("HARKONNEN BUILDING VIPER!")
            self.yard.construct_ship(v, Game.now())
            ships.append(v)
        else:
            print("HARKONNEN TO POOR FOR VIPER :(")

    def build_oxygenminer(self):
        from constellation_perseus import Game

        print("HARKONNEN builds oxygen miner.")

        cm = BasicOxygenHarvester(self.basepos, self.hq, self)
        if Game.instance.buy(cm, self):
            self.yard.construct_ship(cm, Game.now())
            self.harvesters.append(cm)

    def build_carbonminer(self):
        from constellation_perseus import Game

        print("HARKONNEN builds carbon miner.")

        cm = BasicCarbonHarvester(self.basepos, self.hq, self)
        if Game.instance.buy(cm, self):
            self.yard.construct_ship(cm, Game.instance.now())
            self.harvesters.append(cm)

    def build_shipyard(self):
        from constellation_perseus import Shipyard, Game

        self.yard = Shipyard(self.basepos, self.hq, self)
        Game.instance.add(self.yard)

    def __str__(self):
        return "Harkonnen"

    def __repr__(self):
        return "Harkonnen"
