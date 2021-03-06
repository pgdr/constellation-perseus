"""Astronomical objects or celestial objects are naturally occurring physical
entities, associations or structures that current science has demonstrated to
exist in the observable universe.  The term astronomical object is sometimes
used interchangeably with astronomical body.  Typically, an astronomical
(celestial) body refers to a single, cohesive structure that is bound together
by gravity (and sometimes by electromagnetism).

Examples include the asteroids, moons, planets and the stars.  Astronomical
objects are gravitationally bound structures that are associated with a position
in space, but may consist of multiple independent astronomical bodies or
objects.  These objects range from single planets to star clusters, nebulae or
entire galaxies.  A comet may be described as a body, in reference to the frozen
nucleus of ice and dust, or as an object, when describing the nucleus with its
diffuse coma and tail.

@author jonas

"""


from dataclasses import dataclass, field
from typing import Tuple

from .. import GameObject, GameObjectState, GameObjectAction, Position


@dataclass(eq=False)
class Celestial(GameObject):
    name: str

    lumen: float = 0
    mass: float = 0
    radius: float = 0

    position: Position = None
