from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class VideoAdFormatRestrictionEnum(_message.Message):
    __slots__ = ()

    class VideoAdFormatRestriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[VideoAdFormatRestrictionEnum.VideoAdFormatRestriction]
        UNKNOWN: _ClassVar[VideoAdFormatRestrictionEnum.VideoAdFormatRestriction]
        NON_SKIPPABLE_IN_STREAM: _ClassVar[VideoAdFormatRestrictionEnum.VideoAdFormatRestriction]
    UNSPECIFIED: VideoAdFormatRestrictionEnum.VideoAdFormatRestriction
    UNKNOWN: VideoAdFormatRestrictionEnum.VideoAdFormatRestriction
    NON_SKIPPABLE_IN_STREAM: VideoAdFormatRestrictionEnum.VideoAdFormatRestriction

    def __init__(self) -> None:
        ...