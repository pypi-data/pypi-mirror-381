from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.alloydb.v1alpha import csql_resources_pb2 as _csql_resources_pb2
from google.cloud.alloydb.v1alpha import resources_pb2 as _resources_pb2
from google.cloud.alloydb.v1alpha import service_pb2 as _service_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RestoreFromCloudSQLRequest(_message.Message):
    __slots__ = ('cloudsql_backup_run_source', 'parent', 'cluster_id', 'cluster')
    CLOUDSQL_BACKUP_RUN_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cloudsql_backup_run_source: _csql_resources_pb2.CloudSQLBackupRunSource
    parent: str
    cluster_id: str
    cluster: _resources_pb2.Cluster

    def __init__(self, cloudsql_backup_run_source: _Optional[_Union[_csql_resources_pb2.CloudSQLBackupRunSource, _Mapping]]=..., parent: _Optional[str]=..., cluster_id: _Optional[str]=..., cluster: _Optional[_Union[_resources_pb2.Cluster, _Mapping]]=...) -> None:
        ...