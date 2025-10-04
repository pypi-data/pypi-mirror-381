from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Visibility(_message.Message):
    __slots__ = ('distance', 'unit')

    class Unit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNIT_UNSPECIFIED: _ClassVar[Visibility.Unit]
        KILOMETERS: _ClassVar[Visibility.Unit]
        MILES: _ClassVar[Visibility.Unit]
    UNIT_UNSPECIFIED: Visibility.Unit
    KILOMETERS: Visibility.Unit
    MILES: Visibility.Unit
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    distance: float
    unit: Visibility.Unit

    def __init__(self, distance: _Optional[float]=..., unit: _Optional[_Union[Visibility.Unit, str]]=...) -> None:
        ...