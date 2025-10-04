from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ClickViewErrorEnum(_message.Message):
    __slots__ = ()

    class ClickViewError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ClickViewErrorEnum.ClickViewError]
        UNKNOWN: _ClassVar[ClickViewErrorEnum.ClickViewError]
        EXPECTED_FILTER_ON_A_SINGLE_DAY: _ClassVar[ClickViewErrorEnum.ClickViewError]
        DATE_TOO_OLD: _ClassVar[ClickViewErrorEnum.ClickViewError]
    UNSPECIFIED: ClickViewErrorEnum.ClickViewError
    UNKNOWN: ClickViewErrorEnum.ClickViewError
    EXPECTED_FILTER_ON_A_SINGLE_DAY: ClickViewErrorEnum.ClickViewError
    DATE_TOO_OLD: ClickViewErrorEnum.ClickViewError

    def __init__(self) -> None:
        ...