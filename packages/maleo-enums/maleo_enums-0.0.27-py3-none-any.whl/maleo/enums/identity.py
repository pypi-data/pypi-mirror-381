from enum import StrEnum
from typing import List, Optional, Sequence, TypeVar
from maleo.types.string import ListOfStrings


class BloodType(StrEnum):
    A = "a"
    B = "b"
    AB = "ab"
    O = "o"  # noqa: E741

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


BloodTypeT = TypeVar("BloodTypeT", bound=BloodType)
OptionalBloodType = Optional[BloodType]
OptionalBloodTypeT = TypeVar("OptionalBloodTypeT", bound=OptionalBloodType)
ListOfBloodTypes = List[BloodType]
OptionalListOfBloodTypes = Optional[ListOfBloodTypes]
SequenceOfBloodTypes = Sequence[BloodType]
OptionalSequenceOfBloodTypes = Optional[SequenceOfBloodTypes]


class Gender(StrEnum):
    UNDISCLOSED = "undisclosed"
    FEMALE = "female"
    MALE = "male"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


GenderT = TypeVar("GenderT", bound=Gender)
OptionalGender = Optional[Gender]
OptionalGenderT = TypeVar("OptionalGenderT", bound=OptionalGender)
ListOfGenders = List[Gender]
OptionalListOfGenders = Optional[ListOfGenders]
SequenceOfGenders = Sequence[Gender]
OptionalSequenceOfGenders = Optional[SequenceOfGenders]
