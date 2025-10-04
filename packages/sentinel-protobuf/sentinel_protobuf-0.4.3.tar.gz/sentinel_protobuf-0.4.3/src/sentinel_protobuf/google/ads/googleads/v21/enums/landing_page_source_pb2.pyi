from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LandingPageSourceEnum(_message.Message):
    __slots__ = ()

    class LandingPageSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LandingPageSourceEnum.LandingPageSource]
        UNKNOWN: _ClassVar[LandingPageSourceEnum.LandingPageSource]
        ADVERTISER: _ClassVar[LandingPageSourceEnum.LandingPageSource]
        AUTOMATIC: _ClassVar[LandingPageSourceEnum.LandingPageSource]
    UNSPECIFIED: LandingPageSourceEnum.LandingPageSource
    UNKNOWN: LandingPageSourceEnum.LandingPageSource
    ADVERTISER: LandingPageSourceEnum.LandingPageSource
    AUTOMATIC: LandingPageSourceEnum.LandingPageSource

    def __init__(self) -> None:
        ...