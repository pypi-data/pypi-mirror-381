from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BusinessMessageProviderEnum(_message.Message):
    __slots__ = ()

    class BusinessMessageProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BusinessMessageProviderEnum.BusinessMessageProvider]
        UNKNOWN: _ClassVar[BusinessMessageProviderEnum.BusinessMessageProvider]
        WHATSAPP: _ClassVar[BusinessMessageProviderEnum.BusinessMessageProvider]
    UNSPECIFIED: BusinessMessageProviderEnum.BusinessMessageProvider
    UNKNOWN: BusinessMessageProviderEnum.BusinessMessageProvider
    WHATSAPP: BusinessMessageProviderEnum.BusinessMessageProvider

    def __init__(self) -> None:
        ...