from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.backupdr.v1 import backupvault_pb2 as _backupvault_pb2
from google.cloud.backupdr.v1 import backupvault_cloudsql_pb2 as _backupvault_cloudsql_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataSourceReference(_message.Message):
    __slots__ = ('name', 'data_source', 'create_time', 'data_source_backup_config_state', 'data_source_backup_count', 'data_source_backup_config_info', 'data_source_gcp_resource_info')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_BACKUP_CONFIG_STATE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_BACKUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_BACKUP_CONFIG_INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_GCP_RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_source: str
    create_time: _timestamp_pb2.Timestamp
    data_source_backup_config_state: _backupvault_pb2.BackupConfigState
    data_source_backup_count: int
    data_source_backup_config_info: DataSourceBackupConfigInfo
    data_source_gcp_resource_info: DataSourceGcpResourceInfo

    def __init__(self, name: _Optional[str]=..., data_source: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., data_source_backup_config_state: _Optional[_Union[_backupvault_pb2.BackupConfigState, str]]=..., data_source_backup_count: _Optional[int]=..., data_source_backup_config_info: _Optional[_Union[DataSourceBackupConfigInfo, _Mapping]]=..., data_source_gcp_resource_info: _Optional[_Union[DataSourceGcpResourceInfo, _Mapping]]=...) -> None:
        ...

class DataSourceBackupConfigInfo(_message.Message):
    __slots__ = ('last_backup_state', 'last_successful_backup_consistency_time')
    LAST_BACKUP_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_BACKUP_CONSISTENCY_TIME_FIELD_NUMBER: _ClassVar[int]
    last_backup_state: _backupvault_pb2.BackupConfigInfo.LastBackupState
    last_successful_backup_consistency_time: _timestamp_pb2.Timestamp

    def __init__(self, last_backup_state: _Optional[_Union[_backupvault_pb2.BackupConfigInfo.LastBackupState, str]]=..., last_successful_backup_consistency_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DataSourceGcpResourceInfo(_message.Message):
    __slots__ = ('gcp_resourcename', 'type', 'location', 'cloud_sql_instance_properties')
    GCP_RESOURCENAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_INSTANCE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    gcp_resourcename: str
    type: str
    location: str
    cloud_sql_instance_properties: _backupvault_cloudsql_pb2.CloudSqlInstanceDataSourceReferenceProperties

    def __init__(self, gcp_resourcename: _Optional[str]=..., type: _Optional[str]=..., location: _Optional[str]=..., cloud_sql_instance_properties: _Optional[_Union[_backupvault_cloudsql_pb2.CloudSqlInstanceDataSourceReferenceProperties, _Mapping]]=...) -> None:
        ...

class GetDataSourceReferenceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class FetchDataSourceReferencesForResourceTypeRequest(_message.Message):
    __slots__ = ('parent', 'resource_type', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    resource_type: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., resource_type: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class FetchDataSourceReferencesForResourceTypeResponse(_message.Message):
    __slots__ = ('data_source_references', 'next_page_token')
    DATA_SOURCE_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_source_references: _containers.RepeatedCompositeFieldContainer[DataSourceReference]
    next_page_token: str

    def __init__(self, data_source_references: _Optional[_Iterable[_Union[DataSourceReference, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...