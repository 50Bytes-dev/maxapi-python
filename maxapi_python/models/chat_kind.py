from enum import Enum


class ChatKind(str, Enum):
    CHANNEL = "channel"
    CHAT = "chat"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
