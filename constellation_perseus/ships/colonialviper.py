"""The Mark I Colonial Viper, equipped with kinetic energy weapons and
conventional missiles.

@author pgd

"""

import dataclasses
from dataclasses import dataclass
from typing import Dict, List


from .ship import Ship
from .shipclassification import ShipClassification

from .. import Allotropes, Allotrope, GameObjectState

from .. import Gun, ViperMissile, KineticEnergyWeapon


def _gun_fac():
    return [ViperMissile(), KineticEnergyWeapon(), KineticEnergyWeapon()]


def _price_fac():
    return {Allotropes.OXYGEN.value: 3000, Allotropes.CARBON.value: 7000}


@dataclass(frozen=False, eq=False)
class ColonialViper(Ship):
    cooldowntime: int = 3500  # 1.5 sec
    price: Dict[Allotrope, int] = dataclasses.field(default_factory=_price_fac)
    name: str = "Mark I Colonial Viper"
    classification: ShipClassification = ShipClassification.VIPER
    guns: List[Gun] = dataclasses.field(default_factory=_gun_fac)
    damage: float = 1
    state: GameObjectState = GameObjectState.IDLE
    lastjumptime: int = -10 ** 10
