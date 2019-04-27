"""Defines an (x,y,z)-coordinate in space.

@author jonas
"""
import math


@dataclass(frozen=True)
class Position:
    x: int
    y: int
    z: int

    def distance(self, other):
        xdiff = (self.x - self.x) ** 2
        ydiff = (self.y - self.y) ** 2
        zdiff = (self.z - self.z) ** 2
        return sqrt(xdiff + ydiff)  # TODO ignore z axis for now!

    def __add__(self, p):
        return Position(self.x + p.x, self.y + p.y, self.z + p.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
