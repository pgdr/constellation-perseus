from dataclasses import dataclass, field

from constellation_perseus import Position
from constellation_perseus import Allotrope
from constellation_perseus import Message


# from constellation_perseus import Hq


@dataclass
class Player:
    name: str
    hqs: list = None  # field(default_factory=[])  # TODO list[Hq]
    inbox: list = None  # field(default_factory=[]) # TODO list[Message]

    @property
    def position(self) -> Position:
        if hqs:
            return hqs[0].position
        return Position.ORIGIN

    def tick(self, time: int):
        pass

    def get_total(self, allotrope: Allotrope) -> int:
        return sum([hq.allotrope(allotrope) for hq in self.hqs])

    def get_total_oxygen(self):
        return self.get_total(Allotrope.OXYGEN)

    def get_total_carbon(self):
        return self.get_total(Allotrope.CARBON)

    def get_total_phosphorus(self):
        return self.get_total(Allotrope.PHOSPHORUS)

    def get_total_sulfur(self):
        return self.get_total(Allotrope.SULFUR)

    def get_total_selenium(self):
        return self.get_total(Allotrope.SELENIUM)

    def send_message(self, message: Message):
        self.inbox.append(message)

    @property
    def hq(self):
        if self.hqs:
            return self.hqs[0]
        return None

    def add_hq(self, hq):
        if not self.hqs:
            self.hqs = [hq]
        else:
            self.hqs.append(hq)
