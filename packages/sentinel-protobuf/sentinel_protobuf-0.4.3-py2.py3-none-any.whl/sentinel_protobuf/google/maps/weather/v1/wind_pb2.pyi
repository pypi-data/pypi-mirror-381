from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CardinalDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CARDINAL_DIRECTION_UNSPECIFIED: _ClassVar[CardinalDirection]
    NORTH: _ClassVar[CardinalDirection]
    NORTH_NORTHEAST: _ClassVar[CardinalDirection]
    NORTHEAST: _ClassVar[CardinalDirection]
    EAST_NORTHEAST: _ClassVar[CardinalDirection]
    EAST: _ClassVar[CardinalDirection]
    EAST_SOUTHEAST: _ClassVar[CardinalDirection]
    SOUTHEAST: _ClassVar[CardinalDirection]
    SOUTH_SOUTHEAST: _ClassVar[CardinalDirection]
    SOUTH: _ClassVar[CardinalDirection]
    SOUTH_SOUTHWEST: _ClassVar[CardinalDirection]
    SOUTHWEST: _ClassVar[CardinalDirection]
    WEST_SOUTHWEST: _ClassVar[CardinalDirection]
    WEST: _ClassVar[CardinalDirection]
    WEST_NORTHWEST: _ClassVar[CardinalDirection]
    NORTHWEST: _ClassVar[CardinalDirection]
    NORTH_NORTHWEST: _ClassVar[CardinalDirection]

class SpeedUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPEED_UNIT_UNSPECIFIED: _ClassVar[SpeedUnit]
    KILOMETERS_PER_HOUR: _ClassVar[SpeedUnit]
    MILES_PER_HOUR: _ClassVar[SpeedUnit]
CARDINAL_DIRECTION_UNSPECIFIED: CardinalDirection
NORTH: CardinalDirection
NORTH_NORTHEAST: CardinalDirection
NORTHEAST: CardinalDirection
EAST_NORTHEAST: CardinalDirection
EAST: CardinalDirection
EAST_SOUTHEAST: CardinalDirection
SOUTHEAST: CardinalDirection
SOUTH_SOUTHEAST: CardinalDirection
SOUTH: CardinalDirection
SOUTH_SOUTHWEST: CardinalDirection
SOUTHWEST: CardinalDirection
WEST_SOUTHWEST: CardinalDirection
WEST: CardinalDirection
WEST_NORTHWEST: CardinalDirection
NORTHWEST: CardinalDirection
NORTH_NORTHWEST: CardinalDirection
SPEED_UNIT_UNSPECIFIED: SpeedUnit
KILOMETERS_PER_HOUR: SpeedUnit
MILES_PER_HOUR: SpeedUnit

class Wind(_message.Message):
    __slots__ = ('direction', 'speed', 'gust')
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    GUST_FIELD_NUMBER: _ClassVar[int]
    direction: WindDirection
    speed: WindSpeed
    gust: WindSpeed

    def __init__(self, direction: _Optional[_Union[WindDirection, _Mapping]]=..., speed: _Optional[_Union[WindSpeed, _Mapping]]=..., gust: _Optional[_Union[WindSpeed, _Mapping]]=...) -> None:
        ...

class WindDirection(_message.Message):
    __slots__ = ('degrees', 'cardinal')
    DEGREES_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_FIELD_NUMBER: _ClassVar[int]
    degrees: int
    cardinal: CardinalDirection

    def __init__(self, degrees: _Optional[int]=..., cardinal: _Optional[_Union[CardinalDirection, str]]=...) -> None:
        ...

class WindSpeed(_message.Message):
    __slots__ = ('value', 'unit')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: SpeedUnit

    def __init__(self, value: _Optional[float]=..., unit: _Optional[_Union[SpeedUnit, str]]=...) -> None:
        ...