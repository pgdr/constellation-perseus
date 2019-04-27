from dataclasses import dataclass

#from .players import Player
import enum

class MessageType(enum.Enum):
    DIPLOMACY = "Diplomatic cable"
    WARNING = "Proposed sanction"
    THREAT = "Military intent"
    SUBMISSION = "Formal apology"
    NEWS = "News message"
    INTERNAL = "Message from advisor"


@dataclass
class Message:
    to_ : object  #: Player
    from_ : object #: Player
    content: str
    type_: MessageType
    created: int
    archived: bool = False
    read: bool = False
