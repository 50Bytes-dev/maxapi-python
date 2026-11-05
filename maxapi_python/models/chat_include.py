from enum import Enum


class ChatInclude(str, Enum):
    LASTMESSAGE = "lastMessage"
    PARTICIPANTS = "participants"

    def __str__(self) -> str:
        return str(self.value)
