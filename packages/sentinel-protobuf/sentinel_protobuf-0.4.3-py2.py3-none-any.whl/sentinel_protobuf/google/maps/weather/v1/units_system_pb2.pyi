from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UnitsSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNITS_SYSTEM_UNSPECIFIED: _ClassVar[UnitsSystem]
    IMPERIAL: _ClassVar[UnitsSystem]
    METRIC: _ClassVar[UnitsSystem]
UNITS_SYSTEM_UNSPECIFIED: UnitsSystem
IMPERIAL: UnitsSystem
METRIC: UnitsSystem