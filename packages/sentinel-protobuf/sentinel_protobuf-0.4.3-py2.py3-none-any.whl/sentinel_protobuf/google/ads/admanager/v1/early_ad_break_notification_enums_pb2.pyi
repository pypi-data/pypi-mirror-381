from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdBreakStateEnum(_message.Message):
    __slots__ = ()

    class AdBreakState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AD_BREAK_STATE_UNSPECIFIED: _ClassVar[AdBreakStateEnum.AdBreakState]
        DECISIONED: _ClassVar[AdBreakStateEnum.AdBreakState]
        COMPLETE: _ClassVar[AdBreakStateEnum.AdBreakState]
        SCHEDULED: _ClassVar[AdBreakStateEnum.AdBreakState]
    AD_BREAK_STATE_UNSPECIFIED: AdBreakStateEnum.AdBreakState
    DECISIONED: AdBreakStateEnum.AdBreakState
    COMPLETE: AdBreakStateEnum.AdBreakState
    SCHEDULED: AdBreakStateEnum.AdBreakState

    def __init__(self) -> None:
        ...