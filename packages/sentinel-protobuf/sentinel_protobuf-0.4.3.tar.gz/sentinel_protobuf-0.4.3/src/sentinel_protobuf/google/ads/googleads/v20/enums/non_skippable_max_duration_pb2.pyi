from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class NonSkippableMaxDurationEnum(_message.Message):
    __slots__ = ()

    class NonSkippableMaxDuration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[NonSkippableMaxDurationEnum.NonSkippableMaxDuration]
        UNKNOWN: _ClassVar[NonSkippableMaxDurationEnum.NonSkippableMaxDuration]
        MAX_DURATION_FIFTEEN_SECONDS: _ClassVar[NonSkippableMaxDurationEnum.NonSkippableMaxDuration]
        MAX_DURATION_THIRTY_SECONDS: _ClassVar[NonSkippableMaxDurationEnum.NonSkippableMaxDuration]
        MAX_DURATION_SIXTY_SECONDS: _ClassVar[NonSkippableMaxDurationEnum.NonSkippableMaxDuration]
    UNSPECIFIED: NonSkippableMaxDurationEnum.NonSkippableMaxDuration
    UNKNOWN: NonSkippableMaxDurationEnum.NonSkippableMaxDuration
    MAX_DURATION_FIFTEEN_SECONDS: NonSkippableMaxDurationEnum.NonSkippableMaxDuration
    MAX_DURATION_THIRTY_SECONDS: NonSkippableMaxDurationEnum.NonSkippableMaxDuration
    MAX_DURATION_SIXTY_SECONDS: NonSkippableMaxDurationEnum.NonSkippableMaxDuration

    def __init__(self) -> None:
        ...