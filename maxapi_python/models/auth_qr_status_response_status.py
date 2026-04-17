from enum import Enum


class AuthQRStatusResponseStatus(str, Enum):
    AUTHORIZED = "authorized"
    EXPIRED = "expired"
    PENDING = "pending"
    SCANNED = "scanned"

    def __str__(self) -> str:
        return str(self.value)
