from dataclasses import dataclass, field
from typing import List
import icontract

from constellation_perseus import Position
from constellation_perseus import Allotrope, Allotropes
from constellation_perseus import Message


@icontract.invariant(lambda self: isinstance(self.name, str))
@icontract.invariant(lambda self: isinstance(self.hqs, list))
@icontract.invariant(lambda self: isinstance(self.inbox, list))
@icontract.invariant(lambda self: isinstance(self.listeners, list))
@dataclass(eq=False)
class Player:
    name: str
    hqs: List["Hq"] = field(default_factory=list)
    inbox: List[Message] = field(default_factory=list)
    listeners: List = field(default_factory=list)

    def tick(self, time: int):
        pass

    @icontract.require(lambda allotrope: isinstance(allotrope, Allotrope))
    def get_total(self, allotrope: Allotrope) -> int:
        return sum([hq.get_asset(allotrope) for hq in self.hqs])

    def get_total_oxygen(self):
        return self.get_total(Allotropes.OXYGEN.value)

    def get_total_carbon(self):
        return self.get_total(Allotropes.CARBON.value)

    def get_total_phosphorus(self):
        return self.get_total(Allotropes.PHOSPHORUS.value)

    def get_total_sulfur(self):
        return self.get_total(Allotropes.SULFUR.value)

    def get_total_selenium(self):
        return self.get_total(Allotropes.SELENIUM.value)

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
