from enum import Enum


class BlastStatus(str, Enum):
    ABANDONED = "Abandoned"
    ACTIVE = "Active"
    FIRED = "Fired"
    SUSPENDED = "Suspended"

    def __str__(self) -> str:
        return str(self.value)
