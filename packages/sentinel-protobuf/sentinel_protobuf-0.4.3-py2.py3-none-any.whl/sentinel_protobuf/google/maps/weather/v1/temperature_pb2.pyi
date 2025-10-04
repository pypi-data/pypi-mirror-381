from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TemperatureUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPERATURE_UNIT_UNSPECIFIED: _ClassVar[TemperatureUnit]
    CELSIUS: _ClassVar[TemperatureUnit]
    FAHRENHEIT: _ClassVar[TemperatureUnit]
TEMPERATURE_UNIT_UNSPECIFIED: TemperatureUnit
CELSIUS: TemperatureUnit
FAHRENHEIT: TemperatureUnit

class Temperature(_message.Message):
    __slots__ = ('degrees', 'unit')
    DEGREES_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    degrees: float
    unit: TemperatureUnit

    def __init__(self, degrees: _Optional[float]=..., unit: _Optional[_Union[TemperatureUnit, str]]=...) -> None:
        ...