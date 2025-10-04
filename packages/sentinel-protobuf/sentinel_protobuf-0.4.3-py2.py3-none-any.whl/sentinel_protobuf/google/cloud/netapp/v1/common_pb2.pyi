from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ServiceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_LEVEL_UNSPECIFIED: _ClassVar[ServiceLevel]
    PREMIUM: _ClassVar[ServiceLevel]
    EXTREME: _ClassVar[ServiceLevel]
    STANDARD: _ClassVar[ServiceLevel]
    FLEX: _ClassVar[ServiceLevel]

class FlexPerformance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FLEX_PERFORMANCE_UNSPECIFIED: _ClassVar[FlexPerformance]
    FLEX_PERFORMANCE_DEFAULT: _ClassVar[FlexPerformance]
    FLEX_PERFORMANCE_CUSTOM: _ClassVar[FlexPerformance]

class EncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENCRYPTION_TYPE_UNSPECIFIED: _ClassVar[EncryptionType]
    SERVICE_MANAGED: _ClassVar[EncryptionType]
    CLOUD_KMS: _ClassVar[EncryptionType]

class DirectoryServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIRECTORY_SERVICE_TYPE_UNSPECIFIED: _ClassVar[DirectoryServiceType]
    ACTIVE_DIRECTORY: _ClassVar[DirectoryServiceType]

class HybridReplicationSchedule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HYBRID_REPLICATION_SCHEDULE_UNSPECIFIED: _ClassVar[HybridReplicationSchedule]
    EVERY_10_MINUTES: _ClassVar[HybridReplicationSchedule]
    HOURLY: _ClassVar[HybridReplicationSchedule]
    DAILY: _ClassVar[HybridReplicationSchedule]

class QosType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QOS_TYPE_UNSPECIFIED: _ClassVar[QosType]
    AUTO: _ClassVar[QosType]
    MANUAL: _ClassVar[QosType]
SERVICE_LEVEL_UNSPECIFIED: ServiceLevel
PREMIUM: ServiceLevel
EXTREME: ServiceLevel
STANDARD: ServiceLevel
FLEX: ServiceLevel
FLEX_PERFORMANCE_UNSPECIFIED: FlexPerformance
FLEX_PERFORMANCE_DEFAULT: FlexPerformance
FLEX_PERFORMANCE_CUSTOM: FlexPerformance
ENCRYPTION_TYPE_UNSPECIFIED: EncryptionType
SERVICE_MANAGED: EncryptionType
CLOUD_KMS: EncryptionType
DIRECTORY_SERVICE_TYPE_UNSPECIFIED: DirectoryServiceType
ACTIVE_DIRECTORY: DirectoryServiceType
HYBRID_REPLICATION_SCHEDULE_UNSPECIFIED: HybridReplicationSchedule
EVERY_10_MINUTES: HybridReplicationSchedule
HOURLY: HybridReplicationSchedule
DAILY: HybridReplicationSchedule
QOS_TYPE_UNSPECIFIED: QosType
AUTO: QosType
MANUAL: QosType

class LocationMetadata(_message.Message):
    __slots__ = ('supported_service_levels', 'supported_flex_performance', 'has_vcp')
    SUPPORTED_SERVICE_LEVELS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_FLEX_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    HAS_VCP_FIELD_NUMBER: _ClassVar[int]
    supported_service_levels: _containers.RepeatedScalarFieldContainer[ServiceLevel]
    supported_flex_performance: _containers.RepeatedScalarFieldContainer[FlexPerformance]
    has_vcp: bool

    def __init__(self, supported_service_levels: _Optional[_Iterable[_Union[ServiceLevel, str]]]=..., supported_flex_performance: _Optional[_Iterable[_Union[FlexPerformance, str]]]=..., has_vcp: bool=...) -> None:
        ...

class UserCommands(_message.Message):
    __slots__ = ('commands',)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, commands: _Optional[_Iterable[str]]=...) -> None:
        ...