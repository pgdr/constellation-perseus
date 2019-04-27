@dataclass
class Allotrope:
    name: str
    abbr: str
    color: str


OXYGEN = Allotrope("Oxygen", "O", Color.PINK)
CARBON = Allotrope("Carbon", "C", Color.LIGHT_GRAY)
PHOSPORUS = Allotrope("Phosphorus", "P", Color.ORANGE)
SULFUR = Allotrope("Sulfur", "S", Color.MAGENTA)
SELENIUM = Allotrope("Selenium", "Se", Color.WHITE)
TRANSURANIC = Allotrope("Transuranium elements", "SHE", Color.RED)
