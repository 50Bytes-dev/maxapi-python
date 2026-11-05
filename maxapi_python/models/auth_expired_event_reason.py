from enum import Enum


class AuthExpiredEventReason(str, Enum):
    LOGGED_OUT = "logged_out"
    PAGE_BLOCKED = "page_blocked"
    REFRESH_FAILED = "refresh_failed"
    TOKEN_REVOKED = "token_revoked"

    def __str__(self) -> str:
        return str(self.value)
