from dataclasses import dataclass
from .color import Color
import enum


@dataclass(frozen=True)
class Allotrope:
    name: str
    abbr: str
    color: str


class Allotropes(enum.Enum):
    OXYGEN = Allotrope("Oxygen", "O", Color.PINK)
    CARBON = Allotrope("Carbon", "C", Color.LIGHT_GREY)
    PHOSPORUS = Allotrope("Phosphorus", "P", Color.ORANGE)
    SULFUR = Allotrope("Sulfur", "S", Color.MAGENTA)
    SELENIUM = Allotrope("Selenium", "Se", Color.WHITE)
    TRANSURANIC = Allotrope("Transuranium elements", "SHE", Color.RED)
