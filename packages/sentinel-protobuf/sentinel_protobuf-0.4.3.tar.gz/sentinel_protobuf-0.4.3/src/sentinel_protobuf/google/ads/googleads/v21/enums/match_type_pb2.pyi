from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MatchTypeEnum(_message.Message):
    __slots__ = ()

    class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MatchTypeEnum.MatchType]
        UNKNOWN: _ClassVar[MatchTypeEnum.MatchType]
        BROAD: _ClassVar[MatchTypeEnum.MatchType]
        EXACT: _ClassVar[MatchTypeEnum.MatchType]
        PHRASE: _ClassVar[MatchTypeEnum.MatchType]
        AI_MAX: _ClassVar[MatchTypeEnum.MatchType]
    UNSPECIFIED: MatchTypeEnum.MatchType
    UNKNOWN: MatchTypeEnum.MatchType
    BROAD: MatchTypeEnum.MatchType
    EXACT: MatchTypeEnum.MatchType
    PHRASE: MatchTypeEnum.MatchType
    AI_MAX: MatchTypeEnum.MatchType

    def __init__(self) -> None:
        ...