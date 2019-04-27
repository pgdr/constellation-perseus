"""Stars are nuclear fusion devices converting hydrogen to helium.

"""


class Star(Celestial):
    pass


# SOME STARS
SOL = Star(1, 1, 1, "Sol", Position(700, 100, 400), StarClassification.G)

ALCYONE = Star(2400, 6, 8.2, "Alcyone", Position(200, 300, 0), StarClassification.G)
ATLAS = Star(940, 5, 5, "Atlas", Position(50, 200, 0), StarClassification.O)
ELECTRA = Star(1, 1, 1, "Electra", Position(700, 250, 0), StarClassification.B)
MAIA = Star(850, 5, 6.04, "Maia", Position(300, 500, 500), StarClassification.B)
MEROPE = Star(630, 4.5, 4, "Merope", Position(500, 200, 500), StarClassification.O)
PLEIONE = Star(190, 3.4, 3.2, "Pleione", Position(50, 250, 500), StarClassification.B)
CELAENO = Star(240, 9, 4.4, "Celaeno", Position(650, 500, 500), StarClassification.B)

# fix these
TAYGETA = Star(850, 5, 6.04, "Taygeta", Position(600, 600, 500), StarClassification.B)
STEROPE = Star(850, 5, 6.04, "Sterope", Position(550, 650, 500), StarClassification.B)
ASTEROPE = Star(850, 5, 6.04, "Asterope", Position(530, 630, 500), StarClassification.B)
