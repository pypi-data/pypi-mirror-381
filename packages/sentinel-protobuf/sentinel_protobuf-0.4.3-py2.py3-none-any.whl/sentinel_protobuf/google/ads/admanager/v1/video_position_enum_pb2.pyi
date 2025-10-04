from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class VideoPositionEnum(_message.Message):
    __slots__ = ()

    class VideoPosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIDEO_POSITION_UNSPECIFIED: _ClassVar[VideoPositionEnum.VideoPosition]
        ALL: _ClassVar[VideoPositionEnum.VideoPosition]
        MIDROLL: _ClassVar[VideoPositionEnum.VideoPosition]
        POSTROLL: _ClassVar[VideoPositionEnum.VideoPosition]
        PREROLL: _ClassVar[VideoPositionEnum.VideoPosition]
    VIDEO_POSITION_UNSPECIFIED: VideoPositionEnum.VideoPosition
    ALL: VideoPositionEnum.VideoPosition
    MIDROLL: VideoPositionEnum.VideoPosition
    POSTROLL: VideoPositionEnum.VideoPosition
    PREROLL: VideoPositionEnum.VideoPosition

    def __init__(self) -> None:
        ...