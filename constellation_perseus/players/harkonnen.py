"""House Harkonnen, from the volcanic wastelands of Giedi Prime.  The Harkonnen
know only malevolence, hatred and brutality.  Their leader is the corrupt and
vile Baron Rakan.  Rakan's power-hungry sons — Gunseng and Copec — eagerly await
the Baron's death.  Each plots to take his place.  But while he lives, they feed
upon him like parasites.

@author pgd

"""

from dataclasses import dataclass

@dataclass
class Harkonnen(Player):

    yard: ShipYard = None
    basepos: Position = Star.PLEIONE.position
    ships: list[Ship] = []
    harvesters: list[Harvester] = []
    last_tick: int = -1

    THINK_TIME: int = 25
    INIT_TIME: int = 3000

    def tick(self, time: int):
        if time < self.INIT_TIME:
            return
        if last_tick == -1:
            last_tick = time
            return
        if last_tick + THINK_TIME > time:
            return
        last_tick = time

        if len(ships) < 5:
            self.init_phase()
            return

        if len(ships) <= 20:
            self.develop_phase()
            return

        kill_phase()

    def kill_phase(self):
        enemy = Game.instance.getClosestEnemyShip(self.hq)
        if not enemy:
            return
        enemy_pos = Game.instance.get_position(enemy)

        non_ready = 0
        for ship in ships:
            if not ship.ready():
                non_ready += 1
        if non_ready > 0:
            return  #  wait until we're all ready and then KILL!

        for s in ships:
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
        self._hvs_logistic(0, Star.ATLAS)
        self._hvs_logistic(1, Star.ALCYONE)

        if len(harvesters) == 2:
            self.build_carbon_miner()
            return

        if len(harvesters) == 3:
            self.build_oxygen_miner()
            return

        self._hvs_logistic(2, Star.ATLAS)
        self._hvs_logistic(3, Star.ALCYONE)

        if len(ships) < 20:
            self.build_viper()

    def init_phase(self):
        yard = self.yard
        hvs = self.harvesters
        if not yard:
            self.build_shipyard()
            return

        if yard and not yard.is_under_construction():
            return

        if not hvs:
            self.buildCarbonMiner()
            print("HARKONNEN CARBON")
            return

        if self._hvs_logistic(0, Star.ATLAS):
            return

        if len(hvs) == 1:
            self.build_oxygenminer()
            return

        if self._hvs_logistic(1, Star.ALCYONE):
            return

        if len(self.ships) <= 5:
            self.build_viper()
            return

    def build_viper(self):
        v = ColonialViper(Game.instance.get_position(Star.MAIA), self)
        if Game.instance.buy(v, self):
            print("HARKONNEN BUILDING VIPER!")
            self.yard.construct_ship(v, Game.now())
            ships.append(v)
        else:
            print("HARKONNEN TO POOR FOR VIPER :(")

    def build_oxygenminer(self):
        print("HARKONNEN builds oxygen miner.")

        cm = BasicOxygenHarvester(self.base_pos, self.hq, self)
        if Game.instance.buy(cm, self):
            self.yard.construct_ship(cm, Game.now())
            self.harvesters.append(cm)

    def build_carbonminer(self):
        print("HARKONNEN builds carbon miner.")

        cm = BasicCarbonHarvester(self.base_pos, self.hq, self)
        if Game.instance.buy(cm, self):
            self.yard.construct_ship(cm, Game.now())
            self.harvesters.append(cm)

    def build_shipyard(self):
        yard = ShipYard(self.base_pos, self.hq, self)
        game.instance.add(yard)
