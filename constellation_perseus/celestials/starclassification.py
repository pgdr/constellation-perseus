from dataclasses import dataclass

from .. import Allotrope, Allotropes


@dataclass
class StarClassification:
    name: str
    surface_temperature: int
    allotrope: Allotrope


import enum


class StarClassifications(enum.Enum):

    #
    # Mass=60, Radius=15, Lumen=1400000
    #
    # Singly ionized helium lines (H I) either in emission or absorption.
    # Strong UV continuum.
    #
    # Ex. 10 Lacertra
    #
    O = StarClassification("Blue", 30000, Allotropes.CARBON.value)

    #
    # Mass=18, Radius=7, Lumen=20000,
    #
    # Neutral helium lines (H II) in absorption.
    #
    # ex. Rigel Spica
    #
    #
    B = StarClassification("Blue", 11000, Allotropes.OXYGEN.value)

    #
    # 3.2, 2.5, 80,
    # "Hydrogen (H) lines strongest for A0 stars, decreasing for other A's.",
    # "Sirius, Vega"
    #
    A = StarClassification("Blue", 7500, Allotropes.PHOSPORUS.value)

    #
    # Mass=1.7, Radius=1.3, Lumen=6,
    #
    # Ca II absorption. Metallic lines become noticeable.
    #
    # ex. Canopus, Procyon
    #
    F = StarClassification("Blue to White", 6000, Allotropes.SELENIUM.value)

    #
    # Mass=1.1, Radius=1.1, Lumen=1.2
    #
    # Absorption lines of neutral metallic atoms and ions (e.g. once-ionized
    # calcium).
    #
    # ex. Sun, Capella
    #
    G = StarClassification("White to Yellow", 5000, Allotropes.OXYGEN.value)

    #
    # Mass=0.8, Radius=0.9, Lumen=0.4
    #
    # Metallic lines, some blue continuum.
    #
    # ex. Arcturus, Aldebaran
    #
    K = StarClassification("Orange to Red", 3500, Allotropes.CARBON.value)

    #
    # Mass=0.3, Radius=0.4, Lumen=0.04
    #
    # Some molecular bands of titanium oxide.
    #
    # ex. Betelgeuse, Antares
    #
    M = StarClassification("Red", 2500, Allotropes.SULFUR.value)
