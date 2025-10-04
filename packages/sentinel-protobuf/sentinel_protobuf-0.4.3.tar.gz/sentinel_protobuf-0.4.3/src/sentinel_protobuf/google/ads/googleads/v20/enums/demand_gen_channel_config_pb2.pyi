from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DemandGenChannelConfigEnum(_message.Message):
    __slots__ = ()

    class DemandGenChannelConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DemandGenChannelConfigEnum.DemandGenChannelConfig]
        UNKNOWN: _ClassVar[DemandGenChannelConfigEnum.DemandGenChannelConfig]
        CHANNEL_STRATEGY: _ClassVar[DemandGenChannelConfigEnum.DemandGenChannelConfig]
        SELECTED_CHANNELS: _ClassVar[DemandGenChannelConfigEnum.DemandGenChannelConfig]
    UNSPECIFIED: DemandGenChannelConfigEnum.DemandGenChannelConfig
    UNKNOWN: DemandGenChannelConfigEnum.DemandGenChannelConfig
    CHANNEL_STRATEGY: DemandGenChannelConfigEnum.DemandGenChannelConfig
    SELECTED_CHANNELS: DemandGenChannelConfigEnum.DemandGenChannelConfig

    def __init__(self) -> None:
        ...