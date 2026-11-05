from enum import Enum


class DeleteResultStatus(str, Enum):
    DELETED = "deleted"
    FORBIDDEN = "forbidden"
    NOT_FOUND = "not_found"
    TOO_OLD = "too_old"

    def __str__(self) -> str:
        return str(self.value)
