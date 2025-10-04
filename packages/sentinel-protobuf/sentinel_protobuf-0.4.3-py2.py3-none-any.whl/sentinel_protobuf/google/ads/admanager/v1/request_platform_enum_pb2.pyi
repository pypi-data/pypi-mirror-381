from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RequestPlatformEnum(_message.Message):
    __slots__ = ()

    class RequestPlatform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUEST_PLATFORM_UNSPECIFIED: _ClassVar[RequestPlatformEnum.RequestPlatform]
        BROWSER: _ClassVar[RequestPlatformEnum.RequestPlatform]
        MOBILE_APP: _ClassVar[RequestPlatformEnum.RequestPlatform]
        VIDEO_PLAYER: _ClassVar[RequestPlatformEnum.RequestPlatform]
    REQUEST_PLATFORM_UNSPECIFIED: RequestPlatformEnum.RequestPlatform
    BROWSER: RequestPlatformEnum.RequestPlatform
    MOBILE_APP: RequestPlatformEnum.RequestPlatform
    VIDEO_PLAYER: RequestPlatformEnum.RequestPlatform

    def __init__(self) -> None:
        ...