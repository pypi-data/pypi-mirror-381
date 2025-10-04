from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LineOfBusiness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINE_OF_BUSINESS_UNSPECIFIED: _ClassVar[LineOfBusiness]
    COMMERCIAL: _ClassVar[LineOfBusiness]
    RETAIL: _ClassVar[LineOfBusiness]
LINE_OF_BUSINESS_UNSPECIFIED: LineOfBusiness
COMMERCIAL: LineOfBusiness
RETAIL: LineOfBusiness