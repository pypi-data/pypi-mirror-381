from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TargetedVideoBumperTypeEnum(_message.Message):
    __slots__ = ()

    class TargetedVideoBumperType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TARGETED_VIDEO_BUMPER_TYPE_UNSPECIFIED: _ClassVar[TargetedVideoBumperTypeEnum.TargetedVideoBumperType]
        AFTER: _ClassVar[TargetedVideoBumperTypeEnum.TargetedVideoBumperType]
        BEFORE: _ClassVar[TargetedVideoBumperTypeEnum.TargetedVideoBumperType]
    TARGETED_VIDEO_BUMPER_TYPE_UNSPECIFIED: TargetedVideoBumperTypeEnum.TargetedVideoBumperType
    AFTER: TargetedVideoBumperTypeEnum.TargetedVideoBumperType
    BEFORE: TargetedVideoBumperTypeEnum.TargetedVideoBumperType

    def __init__(self) -> None:
        ...