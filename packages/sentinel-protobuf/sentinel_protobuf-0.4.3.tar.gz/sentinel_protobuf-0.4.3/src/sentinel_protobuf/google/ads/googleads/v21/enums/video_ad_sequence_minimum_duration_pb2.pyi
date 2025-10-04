from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class VideoAdSequenceMinimumDurationEnum(_message.Message):
    __slots__ = ()

    class VideoAdSequenceMinimumDuration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[VideoAdSequenceMinimumDurationEnum.VideoAdSequenceMinimumDuration]
        UNKNOWN: _ClassVar[VideoAdSequenceMinimumDurationEnum.VideoAdSequenceMinimumDuration]
        WEEK: _ClassVar[VideoAdSequenceMinimumDurationEnum.VideoAdSequenceMinimumDuration]
        MONTH: _ClassVar[VideoAdSequenceMinimumDurationEnum.VideoAdSequenceMinimumDuration]
    UNSPECIFIED: VideoAdSequenceMinimumDurationEnum.VideoAdSequenceMinimumDuration
    UNKNOWN: VideoAdSequenceMinimumDurationEnum.VideoAdSequenceMinimumDuration
    WEEK: VideoAdSequenceMinimumDurationEnum.VideoAdSequenceMinimumDuration
    MONTH: VideoAdSequenceMinimumDurationEnum.VideoAdSequenceMinimumDuration

    def __init__(self) -> None:
        ...