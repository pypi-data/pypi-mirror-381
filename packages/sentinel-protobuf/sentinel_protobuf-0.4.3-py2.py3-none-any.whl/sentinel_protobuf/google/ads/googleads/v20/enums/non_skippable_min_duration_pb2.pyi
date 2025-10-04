from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class NonSkippableMinDurationEnum(_message.Message):
    __slots__ = ()

    class NonSkippableMinDuration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[NonSkippableMinDurationEnum.NonSkippableMinDuration]
        UNKNOWN: _ClassVar[NonSkippableMinDurationEnum.NonSkippableMinDuration]
        MIN_DURATION_FIVE_SECONDS: _ClassVar[NonSkippableMinDurationEnum.NonSkippableMinDuration]
        MIN_DURATION_SEVEN_SECONDS: _ClassVar[NonSkippableMinDurationEnum.NonSkippableMinDuration]
        MIN_DURATION_SIXTEEN_SECONDS: _ClassVar[NonSkippableMinDurationEnum.NonSkippableMinDuration]
        MIN_DURATION_THIRTY_ONE_SECONDS: _ClassVar[NonSkippableMinDurationEnum.NonSkippableMinDuration]
    UNSPECIFIED: NonSkippableMinDurationEnum.NonSkippableMinDuration
    UNKNOWN: NonSkippableMinDurationEnum.NonSkippableMinDuration
    MIN_DURATION_FIVE_SECONDS: NonSkippableMinDurationEnum.NonSkippableMinDuration
    MIN_DURATION_SEVEN_SECONDS: NonSkippableMinDurationEnum.NonSkippableMinDuration
    MIN_DURATION_SIXTEEN_SECONDS: NonSkippableMinDurationEnum.NonSkippableMinDuration
    MIN_DURATION_THIRTY_ONE_SECONDS: NonSkippableMinDurationEnum.NonSkippableMinDuration

    def __init__(self) -> None:
        ...