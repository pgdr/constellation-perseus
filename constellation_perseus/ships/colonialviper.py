"""The Mark I Colonial Viper, equipped with kinetic energy weapons and
conventional missiles.

@author pgd

"""

import dataclasses
from dataclasses import dataclass
from typing import Dict, List


from .ship import Ship
from .shipclassification import ShipClassification

from .. import Allotropes, Allotrope, Position, GameObjectState

from .. import Gun, ViperMissile, KineticEnergyWeapon


@dataclass(frozen=False)
class ColonialViper(Ship):
    cooldowntime: int = 3500  # 1.5 sec
    price: Dict[Allotrope, int] = dataclasses.field(
        default_factory={Allotropes.OXYGEN: 3000, Allotropes.CARBON: 7000}
    )
    name: str = "Mark I Colonial Viper"
    classification: str = ShipClassification.VIPER
    guns: List[Gun] = dataclasses.field(
        default_factory=[ViperMissile(), KineticEnergyWeapon(), KineticEnergyWeapon()]
    )
    damage: float = 1
    state: GameObjectState = GameObjectState.IDLE
    lastjumptime: int = -10 ** 10
