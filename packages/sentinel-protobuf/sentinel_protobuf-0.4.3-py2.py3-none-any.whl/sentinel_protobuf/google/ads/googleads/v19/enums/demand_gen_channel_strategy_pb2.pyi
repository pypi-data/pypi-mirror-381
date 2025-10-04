from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DemandGenChannelStrategyEnum(_message.Message):
    __slots__ = ()

    class DemandGenChannelStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DemandGenChannelStrategyEnum.DemandGenChannelStrategy]
        UNKNOWN: _ClassVar[DemandGenChannelStrategyEnum.DemandGenChannelStrategy]
        ALL_CHANNELS: _ClassVar[DemandGenChannelStrategyEnum.DemandGenChannelStrategy]
        ALL_OWNED_AND_OPERATED_CHANNELS: _ClassVar[DemandGenChannelStrategyEnum.DemandGenChannelStrategy]
    UNSPECIFIED: DemandGenChannelStrategyEnum.DemandGenChannelStrategy
    UNKNOWN: DemandGenChannelStrategyEnum.DemandGenChannelStrategy
    ALL_CHANNELS: DemandGenChannelStrategyEnum.DemandGenChannelStrategy
    ALL_OWNED_AND_OPERATED_CHANNELS: DemandGenChannelStrategyEnum.DemandGenChannelStrategy

    def __init__(self) -> None:
        ...