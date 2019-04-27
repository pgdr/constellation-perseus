from .gun import Gun

from dataclasses import dataclass


@dataclass
class ViperMissile(Gun):
    ammo: int = 1000
    damage_caused: float = 0.4
    precision: float = 0.5
    range_: int = 1000000
    recharge_time: int = 2000
    name: str = "Conventional Colonial Viper Missile"

    def get_damage(self):
        return 0
