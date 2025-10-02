from enum import StrEnum
from typing import List, Optional, Sequence, TypeVar
from maleo.types.string import ListOfStrings


class Role(StrEnum):
    ADMINISTRATOR = "administrator"
    ANALYST = "analyst"
    ENGINEER = "engineer"
    GUEST = "guest"
    MANAGER = "manager"
    OFFICER = "officer"
    OPERATIONS = "operations"
    SECURITY = "security"
    SUPPORT = "support"
    TESTER = "tester"
    USER = "user"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


RoleT = TypeVar("RoleT", bound=Role)
OptionalRole = Optional[Role]
OptionalRoleT = TypeVar("OptionalRoleT", bound=OptionalRole)
ListOfRoles = List[Role]
OptionalListOfRoles = Optional[ListOfRoles]
SequenceOfRoles = Sequence[Role]
OptionalSequenceOfRoles = Optional[SequenceOfRoles]
