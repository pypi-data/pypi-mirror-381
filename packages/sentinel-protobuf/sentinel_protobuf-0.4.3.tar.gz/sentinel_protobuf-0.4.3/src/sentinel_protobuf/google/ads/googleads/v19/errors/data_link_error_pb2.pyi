from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DataLinkErrorEnum(_message.Message):
    __slots__ = ()

    class DataLinkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DataLinkErrorEnum.DataLinkError]
        UNKNOWN: _ClassVar[DataLinkErrorEnum.DataLinkError]
        YOUTUBE_CHANNEL_ID_INVALID: _ClassVar[DataLinkErrorEnum.DataLinkError]
        YOUTUBE_VIDEO_ID_INVALID: _ClassVar[DataLinkErrorEnum.DataLinkError]
        YOUTUBE_VIDEO_FROM_DIFFERENT_CHANNEL: _ClassVar[DataLinkErrorEnum.DataLinkError]
        PERMISSION_DENIED: _ClassVar[DataLinkErrorEnum.DataLinkError]
        INVALID_STATUS: _ClassVar[DataLinkErrorEnum.DataLinkError]
        INVALID_UPDATE_STATUS: _ClassVar[DataLinkErrorEnum.DataLinkError]
        INVALID_RESOURCE_NAME: _ClassVar[DataLinkErrorEnum.DataLinkError]
    UNSPECIFIED: DataLinkErrorEnum.DataLinkError
    UNKNOWN: DataLinkErrorEnum.DataLinkError
    YOUTUBE_CHANNEL_ID_INVALID: DataLinkErrorEnum.DataLinkError
    YOUTUBE_VIDEO_ID_INVALID: DataLinkErrorEnum.DataLinkError
    YOUTUBE_VIDEO_FROM_DIFFERENT_CHANNEL: DataLinkErrorEnum.DataLinkError
    PERMISSION_DENIED: DataLinkErrorEnum.DataLinkError
    INVALID_STATUS: DataLinkErrorEnum.DataLinkError
    INVALID_UPDATE_STATUS: DataLinkErrorEnum.DataLinkError
    INVALID_RESOURCE_NAME: DataLinkErrorEnum.DataLinkError

    def __init__(self) -> None:
        ...