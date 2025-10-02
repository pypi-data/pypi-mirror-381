from enum import StrEnum
from typing import List, Optional, Sequence, TypeVar
from maleo.types.string import ListOfStrings


class UserType(StrEnum):
    PROXY = "proxy"
    REGULAR = "regular"
    SERVICE = "service"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


UserTypeT = TypeVar("UserTypeT", bound=UserType)
OptionalUserType = Optional[UserType]
OptionalUserTypeT = TypeVar("OptionalUserTypeT", bound=OptionalUserType)
ListOfUserTypes = List[UserType]
OptionalListOfUserTypes = Optional[ListOfUserTypes]
SequenceOfUserTypes = Sequence[UserType]
OptionalSequenceOfUserTypes = Optional[SequenceOfUserTypes]
