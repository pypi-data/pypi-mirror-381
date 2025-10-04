from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class EuPoliticalAdvertisingStatusEnum(_message.Message):
    __slots__ = ()

    class EuPoliticalAdvertisingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[EuPoliticalAdvertisingStatusEnum.EuPoliticalAdvertisingStatus]
        UNKNOWN: _ClassVar[EuPoliticalAdvertisingStatusEnum.EuPoliticalAdvertisingStatus]
        CONTAINS_EU_POLITICAL_ADVERTISING: _ClassVar[EuPoliticalAdvertisingStatusEnum.EuPoliticalAdvertisingStatus]
        DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING: _ClassVar[EuPoliticalAdvertisingStatusEnum.EuPoliticalAdvertisingStatus]
    UNSPECIFIED: EuPoliticalAdvertisingStatusEnum.EuPoliticalAdvertisingStatus
    UNKNOWN: EuPoliticalAdvertisingStatusEnum.EuPoliticalAdvertisingStatus
    CONTAINS_EU_POLITICAL_ADVERTISING: EuPoliticalAdvertisingStatusEnum.EuPoliticalAdvertisingStatus
    DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING: EuPoliticalAdvertisingStatusEnum.EuPoliticalAdvertisingStatus

    def __init__(self) -> None:
        ...