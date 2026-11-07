from enum import Enum


class QRExpiredEventReason(str, Enum):
    LOGIN_EXPIRED = "login_expired"
    LOGIN_FAILED = "login_failed"
    LOGIN_UNSUPPORTED = "login_unsupported"

    def __str__(self) -> str:
        return str(self.value)
