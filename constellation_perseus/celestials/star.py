"""Stars are nuclear fusion devices converting hydrogen to helium.

"""
from dataclasses import dataclass

from .starclassification import StarClassifications, StarClassification
from .celestial import Celestial
from .. import Position


@dataclass(eq=False)
class Star(Celestial):
    sc: StarClassification = None


class Stars:
    # SOME STARS
    SOL = Star(
        1, 1, 1, "Sol", position=Position(700, 100, 400), sc=StarClassifications.G.value
    )

    ALCYONE = Star(
        2400,
        6,
        8.2,
        "Alcyone",
        position=Position(200, 300, 0),
        sc=StarClassifications.G.value,
    )
    ATLAS = Star(
        940,
        5,
        5,
        "Atlas",
        position=Position(50, 200, 0),
        sc=StarClassifications.O.value,
    )
    ELECTRA = Star(
        1,
        1,
        1,
        "Electra",
        position=Position(700, 250, 0),
        sc=StarClassifications.B.value,
    )
    MAIA = Star(
        850,
        5,
        6.04,
        "Maia",
        position=Position(300, 500, 500),
        sc=StarClassifications.B.value,
    )
    MEROPE = Star(
        630,
        4.5,
        4,
        "Merope",
        position=Position(500, 200, 500),
        sc=StarClassifications.O.value,
    )
    PLEIONE = Star(
        190,
        3.4,
        3.2,
        "Pleione",
        position=Position(50, 250, 500),
        sc=StarClassifications.B.value,
    )
    CELAENO = Star(
        240,
        9,
        4.4,
        "Celaeno",
        position=Position(650, 500, 500),
        sc=StarClassifications.B.value,
    )

    # fix these
    TAYGETA = Star(
        850,
        5,
        6.04,
        "Taygeta",
        position=Position(600, 600, 500),
        sc=StarClassifications.B.value,
    )
    STEROPE = Star(
        850,
        5,
        6.04,
        "Sterope",
        position=Position(550, 650, 500),
        sc=StarClassifications.B.value,
    )
    ASTEROPE = Star(
        850,
        5,
        6.04,
        "Asterope",
        position=Position(530, 630, 500),
        sc=StarClassifications.B.value,
    )
