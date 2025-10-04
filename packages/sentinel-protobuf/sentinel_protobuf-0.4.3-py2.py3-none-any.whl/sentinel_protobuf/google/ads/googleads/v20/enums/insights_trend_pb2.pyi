from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class InsightsTrendEnum(_message.Message):
    __slots__ = ()

    class InsightsTrend(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[InsightsTrendEnum.InsightsTrend]
        UNKNOWN: _ClassVar[InsightsTrendEnum.InsightsTrend]
        EMERGING: _ClassVar[InsightsTrendEnum.InsightsTrend]
        RISING: _ClassVar[InsightsTrendEnum.InsightsTrend]
        SUSTAINED: _ClassVar[InsightsTrendEnum.InsightsTrend]
        DECLINING: _ClassVar[InsightsTrendEnum.InsightsTrend]
    UNSPECIFIED: InsightsTrendEnum.InsightsTrend
    UNKNOWN: InsightsTrendEnum.InsightsTrend
    EMERGING: InsightsTrendEnum.InsightsTrend
    RISING: InsightsTrendEnum.InsightsTrend
    SUSTAINED: InsightsTrendEnum.InsightsTrend
    DECLINING: InsightsTrendEnum.InsightsTrend

    def __init__(self) -> None:
        ...