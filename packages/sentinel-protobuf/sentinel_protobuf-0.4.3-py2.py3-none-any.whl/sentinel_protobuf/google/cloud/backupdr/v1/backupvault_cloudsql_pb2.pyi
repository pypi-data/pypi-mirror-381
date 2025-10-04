from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CloudSqlInstanceDataSourceProperties(_message.Message):
    __slots__ = ('name', 'database_installed_version', 'instance_create_time', 'instance_tier')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INSTALLED_VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TIER_FIELD_NUMBER: _ClassVar[int]
    name: str
    database_installed_version: str
    instance_create_time: _timestamp_pb2.Timestamp
    instance_tier: str

    def __init__(self, name: _Optional[str]=..., database_installed_version: _Optional[str]=..., instance_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., instance_tier: _Optional[str]=...) -> None:
        ...

class CloudSqlInstanceBackupProperties(_message.Message):
    __slots__ = ('database_installed_version', 'final_backup', 'source_instance', 'instance_tier')
    DATABASE_INSTALLED_VERSION_FIELD_NUMBER: _ClassVar[int]
    FINAL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TIER_FIELD_NUMBER: _ClassVar[int]
    database_installed_version: str
    final_backup: bool
    source_instance: str
    instance_tier: str

    def __init__(self, database_installed_version: _Optional[str]=..., final_backup: bool=..., source_instance: _Optional[str]=..., instance_tier: _Optional[str]=...) -> None:
        ...

class CloudSqlInstanceDataSourceReferenceProperties(_message.Message):
    __slots__ = ('name', 'database_installed_version', 'instance_create_time', 'instance_tier')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INSTALLED_VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TIER_FIELD_NUMBER: _ClassVar[int]
    name: str
    database_installed_version: str
    instance_create_time: _timestamp_pb2.Timestamp
    instance_tier: str

    def __init__(self, name: _Optional[str]=..., database_installed_version: _Optional[str]=..., instance_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., instance_tier: _Optional[str]=...) -> None:
        ...

class CloudSqlInstanceInitializationConfig(_message.Message):
    __slots__ = ('edition',)

    class Edition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EDITION_UNSPECIFIED: _ClassVar[CloudSqlInstanceInitializationConfig.Edition]
        ENTERPRISE: _ClassVar[CloudSqlInstanceInitializationConfig.Edition]
        ENTERPRISE_PLUS: _ClassVar[CloudSqlInstanceInitializationConfig.Edition]
    EDITION_UNSPECIFIED: CloudSqlInstanceInitializationConfig.Edition
    ENTERPRISE: CloudSqlInstanceInitializationConfig.Edition
    ENTERPRISE_PLUS: CloudSqlInstanceInitializationConfig.Edition
    EDITION_FIELD_NUMBER: _ClassVar[int]
    edition: CloudSqlInstanceInitializationConfig.Edition

    def __init__(self, edition: _Optional[_Union[CloudSqlInstanceInitializationConfig.Edition, str]]=...) -> None:
        ...

class CloudSqlInstanceBackupPlanAssociationProperties(_message.Message):
    __slots__ = ('instance_create_time',)
    INSTANCE_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    instance_create_time: _timestamp_pb2.Timestamp

    def __init__(self, instance_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...