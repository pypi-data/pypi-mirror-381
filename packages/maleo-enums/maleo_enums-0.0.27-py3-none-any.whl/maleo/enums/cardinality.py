from enum import StrEnum
from typing import List, Optional, Sequence, TypeVar
from maleo.types.string import ListOfStrings


class Cardinality(StrEnum):
    MULTIPLE = "multiple"
    SINGLE = "single"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


CardinalityT = TypeVar("CardinalityT", bound=Cardinality)
OptionalCardinality = Optional[Cardinality]
OptionalCardinalityT = TypeVar("OptionalCardinalityT", bound=OptionalCardinality)
ListOfCardinalities = List[Cardinality]
OptionalListOfCardinalities = Optional[ListOfCardinalities]
SequenceOfCardinalities = Sequence[Cardinality]
OptionalSequenceOfCardinalities = Optional[SequenceOfCardinalities]


class Relationship(StrEnum):
    # One origin
    ONE_TO_ONE = "one_to_one"
    ONE_TO_OPTIONAL_ONE = "one_to_optional_one"
    ONE_TO_MANY = "one_to_many"
    ONE_TO_OPTIONAL_MANY = "one_to_optional_many"
    # Optional one origin
    OPTIONAL_ONE_TO_ONE = "optional_one_to_one"
    OPTIONAL_ONE_TO_OPTIONAL_ONE = "optional_one_to_optional_one"
    OPTIONAL_ONE_TO_MANY = "optional_one_to_many"
    OPTIONAL_ONE_TO_OPTIONAL_MANY = "optional_one_to_optional_many"
    # Many origin
    MANY_TO_ONE = "many_to_one"
    MANY_TO_OPTIONAL_ONE = "many_to_optional_one"
    MANY_TO_MANY = "many_to_many"
    MANY_TO_OPTIONAL_MANY = "many_to_optional_many"
    # Optional many origin
    OPTIONAL_MANY_TO_ONE = "optional_many_to_one"
    OPTIONAL_MANY_TO_OPTIONAL_ONE = "optional_many_to_optional_one"
    OPTIONAL_MANY_TO_MANY = "optional_many_to_many"
    OPTIONAL_MANY_TO_OPTIONAL_MANY = "optional_many_to_optional_many"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


RelationshipT = TypeVar("RelationshipT", bound=Relationship)
OptionalRelationship = Optional[Relationship]
OptionalRelationshipT = TypeVar("OptionalRelationshipT", bound=OptionalRelationship)
ListOfRelationships = List[Relationship]
OptionalListOfRelationships = Optional[ListOfRelationships]
SequenceOfRelationships = Sequence[Relationship]
OptionalSequenceOfRelationships = Optional[SequenceOfRelationships]
