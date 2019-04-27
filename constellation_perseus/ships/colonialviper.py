"""The Mark I Colonial Viper, equipped with kinetic energy weapons and
conventional missiles.

@author pgd

"""

from dataclasses import dataclass


@dataclass
class ColonialViper(Ship):

    COOLDOWNTIME: int = 3500  # 1.5 sec

    price: dict[Allotrope, int] = {Allotrope.OXYGEN: 3000, Allotrope.CARBON: 7000}

    name: str = "Mark I Colonial Viper"
    classification: str = ShipClassification.VIPER
    guns: list[Gun] = [ViperMissile(), KineticEnergyWeapon(), KineticEnergyWeapon()]
