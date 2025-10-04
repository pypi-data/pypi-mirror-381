from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class VideoAdSequenceInteractionTypeEnum(_message.Message):
    __slots__ = ()

    class VideoAdSequenceInteractionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType]
        UNKNOWN: _ClassVar[VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType]
        PAID_VIEW: _ClassVar[VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType]
        SKIP: _ClassVar[VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType]
        IMPRESSION: _ClassVar[VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType]
        ENGAGED_IMPRESSION: _ClassVar[VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType]
    UNSPECIFIED: VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType
    UNKNOWN: VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType
    PAID_VIEW: VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType
    SKIP: VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType
    IMPRESSION: VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType
    ENGAGED_IMPRESSION: VideoAdSequenceInteractionTypeEnum.VideoAdSequenceInteractionType

    def __init__(self) -> None:
        ...