from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PscConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PSC_CONNECTION_STATUS_UNSPECIFIED: _ClassVar[PscConnectionStatus]
    PSC_CONNECTION_STATUS_ACTIVE: _ClassVar[PscConnectionStatus]
    PSC_CONNECTION_STATUS_NOT_FOUND: _ClassVar[PscConnectionStatus]

class AuthorizationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTH_MODE_UNSPECIFIED: _ClassVar[AuthorizationMode]
    AUTH_MODE_IAM_AUTH: _ClassVar[AuthorizationMode]
    AUTH_MODE_DISABLED: _ClassVar[AuthorizationMode]

class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_TYPE_UNSPECIFIED: _ClassVar[NodeType]
    REDIS_SHARED_CORE_NANO: _ClassVar[NodeType]
    REDIS_HIGHMEM_MEDIUM: _ClassVar[NodeType]
    REDIS_HIGHMEM_XLARGE: _ClassVar[NodeType]
    REDIS_STANDARD_SMALL: _ClassVar[NodeType]

class TransitEncryptionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSIT_ENCRYPTION_MODE_UNSPECIFIED: _ClassVar[TransitEncryptionMode]
    TRANSIT_ENCRYPTION_MODE_DISABLED: _ClassVar[TransitEncryptionMode]
    TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION: _ClassVar[TransitEncryptionMode]

class ConnectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTION_TYPE_UNSPECIFIED: _ClassVar[ConnectionType]
    CONNECTION_TYPE_DISCOVERY: _ClassVar[ConnectionType]
    CONNECTION_TYPE_PRIMARY: _ClassVar[ConnectionType]
    CONNECTION_TYPE_READER: _ClassVar[ConnectionType]
PSC_CONNECTION_STATUS_UNSPECIFIED: PscConnectionStatus
PSC_CONNECTION_STATUS_ACTIVE: PscConnectionStatus
PSC_CONNECTION_STATUS_NOT_FOUND: PscConnectionStatus
AUTH_MODE_UNSPECIFIED: AuthorizationMode
AUTH_MODE_IAM_AUTH: AuthorizationMode
AUTH_MODE_DISABLED: AuthorizationMode
NODE_TYPE_UNSPECIFIED: NodeType
REDIS_SHARED_CORE_NANO: NodeType
REDIS_HIGHMEM_MEDIUM: NodeType
REDIS_HIGHMEM_XLARGE: NodeType
REDIS_STANDARD_SMALL: NodeType
TRANSIT_ENCRYPTION_MODE_UNSPECIFIED: TransitEncryptionMode
TRANSIT_ENCRYPTION_MODE_DISABLED: TransitEncryptionMode
TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION: TransitEncryptionMode
CONNECTION_TYPE_UNSPECIFIED: ConnectionType
CONNECTION_TYPE_DISCOVERY: ConnectionType
CONNECTION_TYPE_PRIMARY: ConnectionType
CONNECTION_TYPE_READER: ConnectionType

class CreateClusterRequest(_message.Message):
    __slots__ = ('parent', 'cluster_id', 'cluster', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cluster_id: str
    cluster: Cluster
    request_id: str

    def __init__(self, parent: _Optional[str]=..., cluster_id: _Optional[str]=..., cluster: _Optional[_Union[Cluster, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListClustersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListClustersResponse(_message.Message):
    __slots__ = ('clusters', 'next_page_token', 'unreachable')
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[Cluster]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, clusters: _Optional[_Iterable[_Union[Cluster, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ('update_mask', 'cluster', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    cluster: Cluster
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., cluster: _Optional[_Union[Cluster, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetClusterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetClusterCertificateAuthorityRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBackupCollectionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBackupCollectionsResponse(_message.Message):
    __slots__ = ('backup_collections', 'next_page_token', 'unreachable')
    BACKUP_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backup_collections: _containers.RepeatedCompositeFieldContainer[BackupCollection]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, backup_collections: _Optional[_Iterable[_Union[BackupCollection, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetBackupCollectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBackupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBackupsResponse(_message.Message):
    __slots__ = ('backups', 'next_page_token', 'unreachable')
    BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backups: _containers.RepeatedCompositeFieldContainer[Backup]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, backups: _Optional[_Iterable[_Union[Backup, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetBackupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ExportBackupRequest(_message.Message):
    __slots__ = ('gcs_bucket', 'name')
    GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    gcs_bucket: str
    name: str

    def __init__(self, gcs_bucket: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class BackupClusterRequest(_message.Message):
    __slots__ = ('name', 'ttl', 'backup_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    ttl: _duration_pb2.Duration
    backup_id: str

    def __init__(self, name: _Optional[str]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., backup_id: _Optional[str]=...) -> None:
        ...

class Cluster(_message.Message):
    __slots__ = ('gcs_source', 'managed_backup_source', 'name', 'create_time', 'state', 'uid', 'replica_count', 'authorization_mode', 'transit_encryption_mode', 'size_gb', 'shard_count', 'psc_configs', 'discovery_endpoints', 'psc_connections', 'state_info', 'node_type', 'persistence_config', 'redis_configs', 'precise_size_gb', 'zone_distribution_config', 'cross_cluster_replication_config', 'deletion_protection_enabled', 'maintenance_policy', 'maintenance_schedule', 'psc_service_attachments', 'cluster_endpoints', 'backup_collection', 'kms_key', 'automated_backup_config', 'encryption_info')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Cluster.State]
        CREATING: _ClassVar[Cluster.State]
        ACTIVE: _ClassVar[Cluster.State]
        UPDATING: _ClassVar[Cluster.State]
        DELETING: _ClassVar[Cluster.State]
    STATE_UNSPECIFIED: Cluster.State
    CREATING: Cluster.State
    ACTIVE: Cluster.State
    UPDATING: Cluster.State
    DELETING: Cluster.State

    class StateInfo(_message.Message):
        __slots__ = ('update_info',)

        class UpdateInfo(_message.Message):
            __slots__ = ('target_shard_count', 'target_replica_count')
            TARGET_SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
            TARGET_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
            target_shard_count: int
            target_replica_count: int

            def __init__(self, target_shard_count: _Optional[int]=..., target_replica_count: _Optional[int]=...) -> None:
                ...
        UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
        update_info: Cluster.StateInfo.UpdateInfo

        def __init__(self, update_info: _Optional[_Union[Cluster.StateInfo.UpdateInfo, _Mapping]]=...) -> None:
            ...

    class GcsBackupSource(_message.Message):
        __slots__ = ('uris',)
        URIS_FIELD_NUMBER: _ClassVar[int]
        uris: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, uris: _Optional[_Iterable[str]]=...) -> None:
            ...

    class ManagedBackupSource(_message.Message):
        __slots__ = ('backup',)
        BACKUP_FIELD_NUMBER: _ClassVar[int]
        backup: str

        def __init__(self, backup: _Optional[str]=...) -> None:
            ...

    class RedisConfigsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MANAGED_BACKUP_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_MODE_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    PSC_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    PSC_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_INFO_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REDIS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    PRECISE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    ZONE_DISTRIBUTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CROSS_CLUSTER_REPLICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    PSC_SERVICE_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    AUTOMATED_BACKUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    gcs_source: Cluster.GcsBackupSource
    managed_backup_source: Cluster.ManagedBackupSource
    name: str
    create_time: _timestamp_pb2.Timestamp
    state: Cluster.State
    uid: str
    replica_count: int
    authorization_mode: AuthorizationMode
    transit_encryption_mode: TransitEncryptionMode
    size_gb: int
    shard_count: int
    psc_configs: _containers.RepeatedCompositeFieldContainer[PscConfig]
    discovery_endpoints: _containers.RepeatedCompositeFieldContainer[DiscoveryEndpoint]
    psc_connections: _containers.RepeatedCompositeFieldContainer[PscConnection]
    state_info: Cluster.StateInfo
    node_type: NodeType
    persistence_config: ClusterPersistenceConfig
    redis_configs: _containers.ScalarMap[str, str]
    precise_size_gb: float
    zone_distribution_config: ZoneDistributionConfig
    cross_cluster_replication_config: CrossClusterReplicationConfig
    deletion_protection_enabled: bool
    maintenance_policy: ClusterMaintenancePolicy
    maintenance_schedule: ClusterMaintenanceSchedule
    psc_service_attachments: _containers.RepeatedCompositeFieldContainer[PscServiceAttachment]
    cluster_endpoints: _containers.RepeatedCompositeFieldContainer[ClusterEndpoint]
    backup_collection: str
    kms_key: str
    automated_backup_config: AutomatedBackupConfig
    encryption_info: EncryptionInfo

    def __init__(self, gcs_source: _Optional[_Union[Cluster.GcsBackupSource, _Mapping]]=..., managed_backup_source: _Optional[_Union[Cluster.ManagedBackupSource, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Cluster.State, str]]=..., uid: _Optional[str]=..., replica_count: _Optional[int]=..., authorization_mode: _Optional[_Union[AuthorizationMode, str]]=..., transit_encryption_mode: _Optional[_Union[TransitEncryptionMode, str]]=..., size_gb: _Optional[int]=..., shard_count: _Optional[int]=..., psc_configs: _Optional[_Iterable[_Union[PscConfig, _Mapping]]]=..., discovery_endpoints: _Optional[_Iterable[_Union[DiscoveryEndpoint, _Mapping]]]=..., psc_connections: _Optional[_Iterable[_Union[PscConnection, _Mapping]]]=..., state_info: _Optional[_Union[Cluster.StateInfo, _Mapping]]=..., node_type: _Optional[_Union[NodeType, str]]=..., persistence_config: _Optional[_Union[ClusterPersistenceConfig, _Mapping]]=..., redis_configs: _Optional[_Mapping[str, str]]=..., precise_size_gb: _Optional[float]=..., zone_distribution_config: _Optional[_Union[ZoneDistributionConfig, _Mapping]]=..., cross_cluster_replication_config: _Optional[_Union[CrossClusterReplicationConfig, _Mapping]]=..., deletion_protection_enabled: bool=..., maintenance_policy: _Optional[_Union[ClusterMaintenancePolicy, _Mapping]]=..., maintenance_schedule: _Optional[_Union[ClusterMaintenanceSchedule, _Mapping]]=..., psc_service_attachments: _Optional[_Iterable[_Union[PscServiceAttachment, _Mapping]]]=..., cluster_endpoints: _Optional[_Iterable[_Union[ClusterEndpoint, _Mapping]]]=..., backup_collection: _Optional[str]=..., kms_key: _Optional[str]=..., automated_backup_config: _Optional[_Union[AutomatedBackupConfig, _Mapping]]=..., encryption_info: _Optional[_Union[EncryptionInfo, _Mapping]]=...) -> None:
        ...

class AutomatedBackupConfig(_message.Message):
    __slots__ = ('fixed_frequency_schedule', 'automated_backup_mode', 'retention')

    class AutomatedBackupMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUTOMATED_BACKUP_MODE_UNSPECIFIED: _ClassVar[AutomatedBackupConfig.AutomatedBackupMode]
        DISABLED: _ClassVar[AutomatedBackupConfig.AutomatedBackupMode]
        ENABLED: _ClassVar[AutomatedBackupConfig.AutomatedBackupMode]
    AUTOMATED_BACKUP_MODE_UNSPECIFIED: AutomatedBackupConfig.AutomatedBackupMode
    DISABLED: AutomatedBackupConfig.AutomatedBackupMode
    ENABLED: AutomatedBackupConfig.AutomatedBackupMode

    class FixedFrequencySchedule(_message.Message):
        __slots__ = ('start_time',)
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timeofday_pb2.TimeOfDay

        def __init__(self, start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=...) -> None:
            ...
    FIXED_FREQUENCY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATED_BACKUP_MODE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    fixed_frequency_schedule: AutomatedBackupConfig.FixedFrequencySchedule
    automated_backup_mode: AutomatedBackupConfig.AutomatedBackupMode
    retention: _duration_pb2.Duration

    def __init__(self, fixed_frequency_schedule: _Optional[_Union[AutomatedBackupConfig.FixedFrequencySchedule, _Mapping]]=..., automated_backup_mode: _Optional[_Union[AutomatedBackupConfig.AutomatedBackupMode, str]]=..., retention: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class BackupCollection(_message.Message):
    __slots__ = ('name', 'cluster_uid', 'cluster', 'kms_key', 'uid')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    cluster_uid: str
    cluster: str
    kms_key: str
    uid: str

    def __init__(self, name: _Optional[str]=..., cluster_uid: _Optional[str]=..., cluster: _Optional[str]=..., kms_key: _Optional[str]=..., uid: _Optional[str]=...) -> None:
        ...

class Backup(_message.Message):
    __slots__ = ('name', 'create_time', 'cluster', 'cluster_uid', 'total_size_bytes', 'expire_time', 'engine_version', 'backup_files', 'node_type', 'replica_count', 'shard_count', 'backup_type', 'state', 'encryption_info', 'uid')

    class BackupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BACKUP_TYPE_UNSPECIFIED: _ClassVar[Backup.BackupType]
        ON_DEMAND: _ClassVar[Backup.BackupType]
        AUTOMATED: _ClassVar[Backup.BackupType]
    BACKUP_TYPE_UNSPECIFIED: Backup.BackupType
    ON_DEMAND: Backup.BackupType
    AUTOMATED: Backup.BackupType

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Backup.State]
        CREATING: _ClassVar[Backup.State]
        ACTIVE: _ClassVar[Backup.State]
        DELETING: _ClassVar[Backup.State]
        SUSPENDED: _ClassVar[Backup.State]
    STATE_UNSPECIFIED: Backup.State
    CREATING: Backup.State
    ACTIVE: Backup.State
    DELETING: Backup.State
    SUSPENDED: Backup.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENGINE_VERSION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILES_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    cluster: str
    cluster_uid: str
    total_size_bytes: int
    expire_time: _timestamp_pb2.Timestamp
    engine_version: str
    backup_files: _containers.RepeatedCompositeFieldContainer[BackupFile]
    node_type: NodeType
    replica_count: int
    shard_count: int
    backup_type: Backup.BackupType
    state: Backup.State
    encryption_info: EncryptionInfo
    uid: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., cluster: _Optional[str]=..., cluster_uid: _Optional[str]=..., total_size_bytes: _Optional[int]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., engine_version: _Optional[str]=..., backup_files: _Optional[_Iterable[_Union[BackupFile, _Mapping]]]=..., node_type: _Optional[_Union[NodeType, str]]=..., replica_count: _Optional[int]=..., shard_count: _Optional[int]=..., backup_type: _Optional[_Union[Backup.BackupType, str]]=..., state: _Optional[_Union[Backup.State, str]]=..., encryption_info: _Optional[_Union[EncryptionInfo, _Mapping]]=..., uid: _Optional[str]=...) -> None:
        ...

class BackupFile(_message.Message):
    __slots__ = ('file_name', 'size_bytes', 'create_time')
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    size_bytes: int
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, file_name: _Optional[str]=..., size_bytes: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class PscServiceAttachment(_message.Message):
    __slots__ = ('service_attachment', 'connection_type')
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    service_attachment: str
    connection_type: ConnectionType

    def __init__(self, service_attachment: _Optional[str]=..., connection_type: _Optional[_Union[ConnectionType, str]]=...) -> None:
        ...

class CrossClusterReplicationConfig(_message.Message):
    __slots__ = ('cluster_role', 'primary_cluster', 'secondary_clusters', 'update_time', 'membership')

    class ClusterRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLUSTER_ROLE_UNSPECIFIED: _ClassVar[CrossClusterReplicationConfig.ClusterRole]
        NONE: _ClassVar[CrossClusterReplicationConfig.ClusterRole]
        PRIMARY: _ClassVar[CrossClusterReplicationConfig.ClusterRole]
        SECONDARY: _ClassVar[CrossClusterReplicationConfig.ClusterRole]
    CLUSTER_ROLE_UNSPECIFIED: CrossClusterReplicationConfig.ClusterRole
    NONE: CrossClusterReplicationConfig.ClusterRole
    PRIMARY: CrossClusterReplicationConfig.ClusterRole
    SECONDARY: CrossClusterReplicationConfig.ClusterRole

    class RemoteCluster(_message.Message):
        __slots__ = ('cluster', 'uid')
        CLUSTER_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        cluster: str
        uid: str

        def __init__(self, cluster: _Optional[str]=..., uid: _Optional[str]=...) -> None:
            ...

    class Membership(_message.Message):
        __slots__ = ('primary_cluster', 'secondary_clusters')
        PRIMARY_CLUSTER_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
        primary_cluster: CrossClusterReplicationConfig.RemoteCluster
        secondary_clusters: _containers.RepeatedCompositeFieldContainer[CrossClusterReplicationConfig.RemoteCluster]

        def __init__(self, primary_cluster: _Optional[_Union[CrossClusterReplicationConfig.RemoteCluster, _Mapping]]=..., secondary_clusters: _Optional[_Iterable[_Union[CrossClusterReplicationConfig.RemoteCluster, _Mapping]]]=...) -> None:
            ...
    CLUSTER_ROLE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    cluster_role: CrossClusterReplicationConfig.ClusterRole
    primary_cluster: CrossClusterReplicationConfig.RemoteCluster
    secondary_clusters: _containers.RepeatedCompositeFieldContainer[CrossClusterReplicationConfig.RemoteCluster]
    update_time: _timestamp_pb2.Timestamp
    membership: CrossClusterReplicationConfig.Membership

    def __init__(self, cluster_role: _Optional[_Union[CrossClusterReplicationConfig.ClusterRole, str]]=..., primary_cluster: _Optional[_Union[CrossClusterReplicationConfig.RemoteCluster, _Mapping]]=..., secondary_clusters: _Optional[_Iterable[_Union[CrossClusterReplicationConfig.RemoteCluster, _Mapping]]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., membership: _Optional[_Union[CrossClusterReplicationConfig.Membership, _Mapping]]=...) -> None:
        ...

class ClusterMaintenancePolicy(_message.Message):
    __slots__ = ('create_time', 'update_time', 'weekly_maintenance_window')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    weekly_maintenance_window: _containers.RepeatedCompositeFieldContainer[ClusterWeeklyMaintenanceWindow]

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., weekly_maintenance_window: _Optional[_Iterable[_Union[ClusterWeeklyMaintenanceWindow, _Mapping]]]=...) -> None:
        ...

class ClusterWeeklyMaintenanceWindow(_message.Message):
    __slots__ = ('day', 'start_time')
    DAY_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    day: _dayofweek_pb2.DayOfWeek
    start_time: _timeofday_pb2.TimeOfDay

    def __init__(self, day: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]]=..., start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=...) -> None:
        ...

class ClusterMaintenanceSchedule(_message.Message):
    __slots__ = ('start_time', 'end_time')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class PscConfig(_message.Message):
    __slots__ = ('network',)
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    network: str

    def __init__(self, network: _Optional[str]=...) -> None:
        ...

class DiscoveryEndpoint(_message.Message):
    __slots__ = ('address', 'port', 'psc_config')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PSC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    psc_config: PscConfig

    def __init__(self, address: _Optional[str]=..., port: _Optional[int]=..., psc_config: _Optional[_Union[PscConfig, _Mapping]]=...) -> None:
        ...

class PscConnection(_message.Message):
    __slots__ = ('psc_connection_id', 'address', 'forwarding_rule', 'project_id', 'network', 'service_attachment', 'psc_connection_status', 'connection_type')
    PSC_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    PSC_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    psc_connection_id: str
    address: str
    forwarding_rule: str
    project_id: str
    network: str
    service_attachment: str
    psc_connection_status: PscConnectionStatus
    connection_type: ConnectionType

    def __init__(self, psc_connection_id: _Optional[str]=..., address: _Optional[str]=..., forwarding_rule: _Optional[str]=..., project_id: _Optional[str]=..., network: _Optional[str]=..., service_attachment: _Optional[str]=..., psc_connection_status: _Optional[_Union[PscConnectionStatus, str]]=..., connection_type: _Optional[_Union[ConnectionType, str]]=...) -> None:
        ...

class ClusterEndpoint(_message.Message):
    __slots__ = ('connections',)
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[ConnectionDetail]

    def __init__(self, connections: _Optional[_Iterable[_Union[ConnectionDetail, _Mapping]]]=...) -> None:
        ...

class ConnectionDetail(_message.Message):
    __slots__ = ('psc_auto_connection', 'psc_connection')
    PSC_AUTO_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    PSC_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    psc_auto_connection: PscAutoConnection
    psc_connection: PscConnection

    def __init__(self, psc_auto_connection: _Optional[_Union[PscAutoConnection, _Mapping]]=..., psc_connection: _Optional[_Union[PscConnection, _Mapping]]=...) -> None:
        ...

class PscAutoConnection(_message.Message):
    __slots__ = ('psc_connection_id', 'address', 'forwarding_rule', 'project_id', 'network', 'service_attachment', 'psc_connection_status', 'connection_type')
    PSC_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    PSC_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    psc_connection_id: str
    address: str
    forwarding_rule: str
    project_id: str
    network: str
    service_attachment: str
    psc_connection_status: PscConnectionStatus
    connection_type: ConnectionType

    def __init__(self, psc_connection_id: _Optional[str]=..., address: _Optional[str]=..., forwarding_rule: _Optional[str]=..., project_id: _Optional[str]=..., network: _Optional[str]=..., service_attachment: _Optional[str]=..., psc_connection_status: _Optional[_Union[PscConnectionStatus, str]]=..., connection_type: _Optional[_Union[ConnectionType, str]]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class CertificateAuthority(_message.Message):
    __slots__ = ('managed_server_ca', 'name')

    class ManagedCertificateAuthority(_message.Message):
        __slots__ = ('ca_certs',)

        class CertChain(_message.Message):
            __slots__ = ('certificates',)
            CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
            certificates: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, certificates: _Optional[_Iterable[str]]=...) -> None:
                ...
        CA_CERTS_FIELD_NUMBER: _ClassVar[int]
        ca_certs: _containers.RepeatedCompositeFieldContainer[CertificateAuthority.ManagedCertificateAuthority.CertChain]

        def __init__(self, ca_certs: _Optional[_Iterable[_Union[CertificateAuthority.ManagedCertificateAuthority.CertChain, _Mapping]]]=...) -> None:
            ...
    MANAGED_SERVER_CA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    managed_server_ca: CertificateAuthority.ManagedCertificateAuthority
    name: str

    def __init__(self, managed_server_ca: _Optional[_Union[CertificateAuthority.ManagedCertificateAuthority, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class ClusterPersistenceConfig(_message.Message):
    __slots__ = ('mode', 'rdb_config', 'aof_config')

    class PersistenceMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERSISTENCE_MODE_UNSPECIFIED: _ClassVar[ClusterPersistenceConfig.PersistenceMode]
        DISABLED: _ClassVar[ClusterPersistenceConfig.PersistenceMode]
        RDB: _ClassVar[ClusterPersistenceConfig.PersistenceMode]
        AOF: _ClassVar[ClusterPersistenceConfig.PersistenceMode]
    PERSISTENCE_MODE_UNSPECIFIED: ClusterPersistenceConfig.PersistenceMode
    DISABLED: ClusterPersistenceConfig.PersistenceMode
    RDB: ClusterPersistenceConfig.PersistenceMode
    AOF: ClusterPersistenceConfig.PersistenceMode

    class RDBConfig(_message.Message):
        __slots__ = ('rdb_snapshot_period', 'rdb_snapshot_start_time')

        class SnapshotPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SNAPSHOT_PERIOD_UNSPECIFIED: _ClassVar[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod]
            ONE_HOUR: _ClassVar[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod]
            SIX_HOURS: _ClassVar[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod]
            TWELVE_HOURS: _ClassVar[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod]
            TWENTY_FOUR_HOURS: _ClassVar[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod]
        SNAPSHOT_PERIOD_UNSPECIFIED: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        ONE_HOUR: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        SIX_HOURS: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        TWELVE_HOURS: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        TWENTY_FOUR_HOURS: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        RDB_SNAPSHOT_PERIOD_FIELD_NUMBER: _ClassVar[int]
        RDB_SNAPSHOT_START_TIME_FIELD_NUMBER: _ClassVar[int]
        rdb_snapshot_period: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        rdb_snapshot_start_time: _timestamp_pb2.Timestamp

        def __init__(self, rdb_snapshot_period: _Optional[_Union[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod, str]]=..., rdb_snapshot_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class AOFConfig(_message.Message):
        __slots__ = ('append_fsync',)

        class AppendFsync(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            APPEND_FSYNC_UNSPECIFIED: _ClassVar[ClusterPersistenceConfig.AOFConfig.AppendFsync]
            NO: _ClassVar[ClusterPersistenceConfig.AOFConfig.AppendFsync]
            EVERYSEC: _ClassVar[ClusterPersistenceConfig.AOFConfig.AppendFsync]
            ALWAYS: _ClassVar[ClusterPersistenceConfig.AOFConfig.AppendFsync]
        APPEND_FSYNC_UNSPECIFIED: ClusterPersistenceConfig.AOFConfig.AppendFsync
        NO: ClusterPersistenceConfig.AOFConfig.AppendFsync
        EVERYSEC: ClusterPersistenceConfig.AOFConfig.AppendFsync
        ALWAYS: ClusterPersistenceConfig.AOFConfig.AppendFsync
        APPEND_FSYNC_FIELD_NUMBER: _ClassVar[int]
        append_fsync: ClusterPersistenceConfig.AOFConfig.AppendFsync

        def __init__(self, append_fsync: _Optional[_Union[ClusterPersistenceConfig.AOFConfig.AppendFsync, str]]=...) -> None:
            ...
    MODE_FIELD_NUMBER: _ClassVar[int]
    RDB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AOF_CONFIG_FIELD_NUMBER: _ClassVar[int]
    mode: ClusterPersistenceConfig.PersistenceMode
    rdb_config: ClusterPersistenceConfig.RDBConfig
    aof_config: ClusterPersistenceConfig.AOFConfig

    def __init__(self, mode: _Optional[_Union[ClusterPersistenceConfig.PersistenceMode, str]]=..., rdb_config: _Optional[_Union[ClusterPersistenceConfig.RDBConfig, _Mapping]]=..., aof_config: _Optional[_Union[ClusterPersistenceConfig.AOFConfig, _Mapping]]=...) -> None:
        ...

class ZoneDistributionConfig(_message.Message):
    __slots__ = ('mode', 'zone')

    class ZoneDistributionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ZONE_DISTRIBUTION_MODE_UNSPECIFIED: _ClassVar[ZoneDistributionConfig.ZoneDistributionMode]
        MULTI_ZONE: _ClassVar[ZoneDistributionConfig.ZoneDistributionMode]
        SINGLE_ZONE: _ClassVar[ZoneDistributionConfig.ZoneDistributionMode]
    ZONE_DISTRIBUTION_MODE_UNSPECIFIED: ZoneDistributionConfig.ZoneDistributionMode
    MULTI_ZONE: ZoneDistributionConfig.ZoneDistributionMode
    SINGLE_ZONE: ZoneDistributionConfig.ZoneDistributionMode
    MODE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    mode: ZoneDistributionConfig.ZoneDistributionMode
    zone: str

    def __init__(self, mode: _Optional[_Union[ZoneDistributionConfig.ZoneDistributionMode, str]]=..., zone: _Optional[str]=...) -> None:
        ...

class RescheduleClusterMaintenanceRequest(_message.Message):
    __slots__ = ('name', 'reschedule_type', 'schedule_time')

    class RescheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESCHEDULE_TYPE_UNSPECIFIED: _ClassVar[RescheduleClusterMaintenanceRequest.RescheduleType]
        IMMEDIATE: _ClassVar[RescheduleClusterMaintenanceRequest.RescheduleType]
        SPECIFIC_TIME: _ClassVar[RescheduleClusterMaintenanceRequest.RescheduleType]
    RESCHEDULE_TYPE_UNSPECIFIED: RescheduleClusterMaintenanceRequest.RescheduleType
    IMMEDIATE: RescheduleClusterMaintenanceRequest.RescheduleType
    SPECIFIC_TIME: RescheduleClusterMaintenanceRequest.RescheduleType
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    reschedule_type: RescheduleClusterMaintenanceRequest.RescheduleType
    schedule_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., reschedule_type: _Optional[_Union[RescheduleClusterMaintenanceRequest.RescheduleType, str]]=..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class EncryptionInfo(_message.Message):
    __slots__ = ('encryption_type', 'kms_key_versions', 'kms_key_primary_state', 'last_update_time')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[EncryptionInfo.Type]
        GOOGLE_DEFAULT_ENCRYPTION: _ClassVar[EncryptionInfo.Type]
        CUSTOMER_MANAGED_ENCRYPTION: _ClassVar[EncryptionInfo.Type]
    TYPE_UNSPECIFIED: EncryptionInfo.Type
    GOOGLE_DEFAULT_ENCRYPTION: EncryptionInfo.Type
    CUSTOMER_MANAGED_ENCRYPTION: EncryptionInfo.Type

    class KmsKeyState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KMS_KEY_STATE_UNSPECIFIED: _ClassVar[EncryptionInfo.KmsKeyState]
        ENABLED: _ClassVar[EncryptionInfo.KmsKeyState]
        PERMISSION_DENIED: _ClassVar[EncryptionInfo.KmsKeyState]
        DISABLED: _ClassVar[EncryptionInfo.KmsKeyState]
        DESTROYED: _ClassVar[EncryptionInfo.KmsKeyState]
        DESTROY_SCHEDULED: _ClassVar[EncryptionInfo.KmsKeyState]
        EKM_KEY_UNREACHABLE_DETECTED: _ClassVar[EncryptionInfo.KmsKeyState]
        BILLING_DISABLED: _ClassVar[EncryptionInfo.KmsKeyState]
        UNKNOWN_FAILURE: _ClassVar[EncryptionInfo.KmsKeyState]
    KMS_KEY_STATE_UNSPECIFIED: EncryptionInfo.KmsKeyState
    ENABLED: EncryptionInfo.KmsKeyState
    PERMISSION_DENIED: EncryptionInfo.KmsKeyState
    DISABLED: EncryptionInfo.KmsKeyState
    DESTROYED: EncryptionInfo.KmsKeyState
    DESTROY_SCHEDULED: EncryptionInfo.KmsKeyState
    EKM_KEY_UNREACHABLE_DETECTED: EncryptionInfo.KmsKeyState
    BILLING_DISABLED: EncryptionInfo.KmsKeyState
    UNKNOWN_FAILURE: EncryptionInfo.KmsKeyState
    ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_PRIMARY_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    encryption_type: EncryptionInfo.Type
    kms_key_versions: _containers.RepeatedScalarFieldContainer[str]
    kms_key_primary_state: EncryptionInfo.KmsKeyState
    last_update_time: _timestamp_pb2.Timestamp

    def __init__(self, encryption_type: _Optional[_Union[EncryptionInfo.Type, str]]=..., kms_key_versions: _Optional[_Iterable[str]]=..., kms_key_primary_state: _Optional[_Union[EncryptionInfo.KmsKeyState, str]]=..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...