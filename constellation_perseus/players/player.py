from dataclasses import dataclass

from constellation_perseus import Position
from constellation_perseus import Allotrope
from constellation_perseus import Message


#from constellation_perseus import Hq

@dataclass
class Player:
    hqs: list  # TODO list[Hq]
    inbox: list  # TODO list[Message]
    name: str

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
