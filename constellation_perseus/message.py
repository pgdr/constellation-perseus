class MessageType(enum):
    DIPLOMACY = "Diplomatic cable"
    WARNING = "Proposed sanction"
    THREAT = "Military intent"
    SUBMISSION = "Formal apology"
    NEWS = "News message"
    INTERNAL = "Message from advisor"


@dataclass
class Message:
    to_: Player
    from_: Player
    content: str
    type_: MessageType
    archived: bool = False
    read: bool = False
    created: int

    @static_method
    def internal(msg):
        pass
