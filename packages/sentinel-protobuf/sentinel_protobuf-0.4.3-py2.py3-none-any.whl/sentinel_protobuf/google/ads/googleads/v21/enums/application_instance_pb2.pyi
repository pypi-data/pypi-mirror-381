from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationInstanceEnum(_message.Message):
    __slots__ = ()

    class ApplicationInstance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ApplicationInstanceEnum.ApplicationInstance]
        UNKNOWN: _ClassVar[ApplicationInstanceEnum.ApplicationInstance]
        DEVELOPMENT_AND_TESTING: _ClassVar[ApplicationInstanceEnum.ApplicationInstance]
        PRODUCTION: _ClassVar[ApplicationInstanceEnum.ApplicationInstance]
    UNSPECIFIED: ApplicationInstanceEnum.ApplicationInstance
    UNKNOWN: ApplicationInstanceEnum.ApplicationInstance
    DEVELOPMENT_AND_TESTING: ApplicationInstanceEnum.ApplicationInstance
    PRODUCTION: ApplicationInstanceEnum.ApplicationInstance

    def __init__(self) -> None:
        ...