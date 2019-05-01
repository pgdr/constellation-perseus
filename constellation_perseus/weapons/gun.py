from dataclasses import dataclass

from .. import GameObject


@dataclass(eq=False)
class Gun(GameObject):
    ammo: int = 0
    damage_caused: float = 0
    precision: float = 0
    range_: int = 0
    recharge_time: float = 0
    name: str = ""
