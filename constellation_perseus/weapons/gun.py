from dataclasses import dataclass

from .. import GameObject


@dataclass
class Gun(GameObject):
    ammo: int
    damage_caused: float
    precision: float
    range_: int
    recharge_time: float
    name: str
