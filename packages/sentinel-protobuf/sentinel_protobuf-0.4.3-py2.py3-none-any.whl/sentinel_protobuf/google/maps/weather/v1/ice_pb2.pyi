from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IceThickness(_message.Message):
    __slots__ = ('thickness', 'unit')

    class Unit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNIT_UNSPECIFIED: _ClassVar[IceThickness.Unit]
        MILLIMETERS: _ClassVar[IceThickness.Unit]
        INCHES: _ClassVar[IceThickness.Unit]
    UNIT_UNSPECIFIED: IceThickness.Unit
    MILLIMETERS: IceThickness.Unit
    INCHES: IceThickness.Unit
    THICKNESS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    thickness: float
    unit: IceThickness.Unit

    def __init__(self, thickness: _Optional[float]=..., unit: _Optional[_Union[IceThickness.Unit, str]]=...) -> None:
        ...