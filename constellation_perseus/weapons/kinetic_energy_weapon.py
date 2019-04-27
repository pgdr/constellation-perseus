from .gun import Gun
from dataclasses import dataclass


@dataclass
class KineticEnergyWeapon(Gun):
    ammo: int = 10 ** 10
    damage_caused: float = 0.1
    precision: float = 0.7
    range_: int = 500
    recharge_time: int = 50
    name: str = "Kinetic Energy Laser"

    def get_damage(self):
        return 1
