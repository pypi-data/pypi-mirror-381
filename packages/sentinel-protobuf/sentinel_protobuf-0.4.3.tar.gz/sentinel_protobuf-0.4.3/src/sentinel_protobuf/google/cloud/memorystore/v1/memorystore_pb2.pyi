from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
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
    ACTIVE: _ClassVar[PscConnectionStatus]
    NOT_FOUND: _ClassVar[PscConnectionStatus]

class ConnectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTION_TYPE_UNSPECIFIED: _ClassVar[ConnectionType]
    CONNECTION_TYPE_DISCOVERY: _ClassVar[ConnectionType]
    CONNECTION_TYPE_PRIMARY: _ClassVar[ConnectionType]
    CONNECTION_TYPE_READER: _ClassVar[ConnectionType]
PSC_CONNECTION_STATUS_UNSPECIFIED: PscConnectionStatus
ACTIVE: PscConnectionStatus
NOT_FOUND: PscConnectionStatus
CONNECTION_TYPE_UNSPECIFIED: ConnectionType
CONNECTION_TYPE_DISCOVERY: ConnectionType
CONNECTION_TYPE_PRIMARY: ConnectionType
CONNECTION_TYPE_READER: ConnectionType

class Instance(_message.Message):
    __slots__ = ('gcs_source', 'managed_backup_source', 'name', 'create_time', 'update_time', 'labels', 'state', 'state_info', 'uid', 'replica_count', 'authorization_mode', 'transit_encryption_mode', 'shard_count', 'discovery_endpoints', 'node_type', 'persistence_config', 'engine_version', 'engine_configs', 'node_config', 'zone_distribution_config', 'deletion_protection_enabled', 'psc_auto_connections', 'psc_attachment_details', 'endpoints', 'mode', 'ondemand_maintenance', 'maintenance_policy', 'maintenance_schedule', 'cross_instance_replication_config', 'async_instance_endpoints_deletion_enabled', 'backup_collection', 'automated_backup_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        ACTIVE: _ClassVar[Instance.State]
        UPDATING: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    ACTIVE: Instance.State
    UPDATING: Instance.State
    DELETING: Instance.State

    class AuthorizationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUTHORIZATION_MODE_UNSPECIFIED: _ClassVar[Instance.AuthorizationMode]
        AUTH_DISABLED: _ClassVar[Instance.AuthorizationMode]
        IAM_AUTH: _ClassVar[Instance.AuthorizationMode]
    AUTHORIZATION_MODE_UNSPECIFIED: Instance.AuthorizationMode
    AUTH_DISABLED: Instance.AuthorizationMode
    IAM_AUTH: Instance.AuthorizationMode

    class TransitEncryptionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSIT_ENCRYPTION_MODE_UNSPECIFIED: _ClassVar[Instance.TransitEncryptionMode]
        TRANSIT_ENCRYPTION_DISABLED: _ClassVar[Instance.TransitEncryptionMode]
        SERVER_AUTHENTICATION: _ClassVar[Instance.TransitEncryptionMode]
    TRANSIT_ENCRYPTION_MODE_UNSPECIFIED: Instance.TransitEncryptionMode
    TRANSIT_ENCRYPTION_DISABLED: Instance.TransitEncryptionMode
    SERVER_AUTHENTICATION: Instance.TransitEncryptionMode

    class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NODE_TYPE_UNSPECIFIED: _ClassVar[Instance.NodeType]
        SHARED_CORE_NANO: _ClassVar[Instance.NodeType]
        HIGHMEM_MEDIUM: _ClassVar[Instance.NodeType]
        HIGHMEM_XLARGE: _ClassVar[Instance.NodeType]
        STANDARD_SMALL: _ClassVar[Instance.NodeType]
    NODE_TYPE_UNSPECIFIED: Instance.NodeType
    SHARED_CORE_NANO: Instance.NodeType
    HIGHMEM_MEDIUM: Instance.NodeType
    HIGHMEM_XLARGE: Instance.NodeType
    STANDARD_SMALL: Instance.NodeType

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[Instance.Mode]
        STANDALONE: _ClassVar[Instance.Mode]
        CLUSTER: _ClassVar[Instance.Mode]
        CLUSTER_DISABLED: _ClassVar[Instance.Mode]
    MODE_UNSPECIFIED: Instance.Mode
    STANDALONE: Instance.Mode
    CLUSTER: Instance.Mode
    CLUSTER_DISABLED: Instance.Mode

    class StateInfo(_message.Message):
        __slots__ = ('update_info',)

        class UpdateInfo(_message.Message):
            __slots__ = ('target_shard_count', 'target_replica_count', 'target_engine_version', 'target_node_type')
            TARGET_SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
            TARGET_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
            TARGET_ENGINE_VERSION_FIELD_NUMBER: _ClassVar[int]
            TARGET_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
            target_shard_count: int
            target_replica_count: int
            target_engine_version: str
            target_node_type: Instance.NodeType

            def __init__(self, target_shard_count: _Optional[int]=..., target_replica_count: _Optional[int]=..., target_engine_version: _Optional[str]=..., target_node_type: _Optional[_Union[Instance.NodeType, str]]=...) -> None:
                ...
        UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
        update_info: Instance.StateInfo.UpdateInfo

        def __init__(self, update_info: _Optional[_Union[Instance.StateInfo.UpdateInfo, _Mapping]]=...) -> None:
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

    class InstanceEndpoint(_message.Message):
        __slots__ = ('connections',)
        CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        connections: _containers.RepeatedCompositeFieldContainer[Instance.ConnectionDetail]

        def __init__(self, connections: _Optional[_Iterable[_Union[Instance.ConnectionDetail, _Mapping]]]=...) -> None:
            ...

    class ConnectionDetail(_message.Message):
        __slots__ = ('psc_auto_connection', 'psc_connection')
        PSC_AUTO_CONNECTION_FIELD_NUMBER: _ClassVar[int]
        PSC_CONNECTION_FIELD_NUMBER: _ClassVar[int]
        psc_auto_connection: PscAutoConnection
        psc_connection: PscConnection

        def __init__(self, psc_auto_connection: _Optional[_Union[PscAutoConnection, _Mapping]]=..., psc_connection: _Optional[_Union[PscConnection, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class EngineConfigsEntry(_message.Message):
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
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_INFO_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_MODE_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENGINE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENGINE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ZONE_DISTRIBUTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PSC_AUTO_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    PSC_ATTACHMENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    ONDEMAND_MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CROSS_INSTANCE_REPLICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ASYNC_INSTANCE_ENDPOINTS_DELETION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    AUTOMATED_BACKUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    gcs_source: Instance.GcsBackupSource
    managed_backup_source: Instance.ManagedBackupSource
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Instance.State
    state_info: Instance.StateInfo
    uid: str
    replica_count: int
    authorization_mode: Instance.AuthorizationMode
    transit_encryption_mode: Instance.TransitEncryptionMode
    shard_count: int
    discovery_endpoints: _containers.RepeatedCompositeFieldContainer[DiscoveryEndpoint]
    node_type: Instance.NodeType
    persistence_config: PersistenceConfig
    engine_version: str
    engine_configs: _containers.ScalarMap[str, str]
    node_config: NodeConfig
    zone_distribution_config: ZoneDistributionConfig
    deletion_protection_enabled: bool
    psc_auto_connections: _containers.RepeatedCompositeFieldContainer[PscAutoConnection]
    psc_attachment_details: _containers.RepeatedCompositeFieldContainer[PscAttachmentDetail]
    endpoints: _containers.RepeatedCompositeFieldContainer[Instance.InstanceEndpoint]
    mode: Instance.Mode
    ondemand_maintenance: bool
    maintenance_policy: MaintenancePolicy
    maintenance_schedule: MaintenanceSchedule
    cross_instance_replication_config: CrossInstanceReplicationConfig
    async_instance_endpoints_deletion_enabled: bool
    backup_collection: str
    automated_backup_config: AutomatedBackupConfig

    def __init__(self, gcs_source: _Optional[_Union[Instance.GcsBackupSource, _Mapping]]=..., managed_backup_source: _Optional[_Union[Instance.ManagedBackupSource, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Instance.State, str]]=..., state_info: _Optional[_Union[Instance.StateInfo, _Mapping]]=..., uid: _Optional[str]=..., replica_count: _Optional[int]=..., authorization_mode: _Optional[_Union[Instance.AuthorizationMode, str]]=..., transit_encryption_mode: _Optional[_Union[Instance.TransitEncryptionMode, str]]=..., shard_count: _Optional[int]=..., discovery_endpoints: _Optional[_Iterable[_Union[DiscoveryEndpoint, _Mapping]]]=..., node_type: _Optional[_Union[Instance.NodeType, str]]=..., persistence_config: _Optional[_Union[PersistenceConfig, _Mapping]]=..., engine_version: _Optional[str]=..., engine_configs: _Optional[_Mapping[str, str]]=..., node_config: _Optional[_Union[NodeConfig, _Mapping]]=..., zone_distribution_config: _Optional[_Union[ZoneDistributionConfig, _Mapping]]=..., deletion_protection_enabled: bool=..., psc_auto_connections: _Optional[_Iterable[_Union[PscAutoConnection, _Mapping]]]=..., psc_attachment_details: _Optional[_Iterable[_Union[PscAttachmentDetail, _Mapping]]]=..., endpoints: _Optional[_Iterable[_Union[Instance.InstanceEndpoint, _Mapping]]]=..., mode: _Optional[_Union[Instance.Mode, str]]=..., ondemand_maintenance: bool=..., maintenance_policy: _Optional[_Union[MaintenancePolicy, _Mapping]]=..., maintenance_schedule: _Optional[_Union[MaintenanceSchedule, _Mapping]]=..., cross_instance_replication_config: _Optional[_Union[CrossInstanceReplicationConfig, _Mapping]]=..., async_instance_endpoints_deletion_enabled: bool=..., backup_collection: _Optional[str]=..., automated_backup_config: _Optional[_Union[AutomatedBackupConfig, _Mapping]]=...) -> None:
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
    __slots__ = ('name', 'instance_uid', 'instance', 'kms_key', 'uid', 'create_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_UID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    instance_uid: str
    instance: str
    kms_key: str
    uid: str
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., instance_uid: _Optional[str]=..., instance: _Optional[str]=..., kms_key: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Backup(_message.Message):
    __slots__ = ('name', 'create_time', 'instance', 'instance_uid', 'total_size_bytes', 'expire_time', 'engine_version', 'backup_files', 'node_type', 'replica_count', 'shard_count', 'backup_type', 'state', 'uid')

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
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_UID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENGINE_VERSION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILES_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    instance: str
    instance_uid: str
    total_size_bytes: int
    expire_time: _timestamp_pb2.Timestamp
    engine_version: str
    backup_files: _containers.RepeatedCompositeFieldContainer[BackupFile]
    node_type: Instance.NodeType
    replica_count: int
    shard_count: int
    backup_type: Backup.BackupType
    state: Backup.State
    uid: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., instance: _Optional[str]=..., instance_uid: _Optional[str]=..., total_size_bytes: _Optional[int]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., engine_version: _Optional[str]=..., backup_files: _Optional[_Iterable[_Union[BackupFile, _Mapping]]]=..., node_type: _Optional[_Union[Instance.NodeType, str]]=..., replica_count: _Optional[int]=..., shard_count: _Optional[int]=..., backup_type: _Optional[_Union[Backup.BackupType, str]]=..., state: _Optional[_Union[Backup.State, str]]=..., uid: _Optional[str]=...) -> None:
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

class CrossInstanceReplicationConfig(_message.Message):
    __slots__ = ('instance_role', 'primary_instance', 'secondary_instances', 'update_time', 'membership')

    class InstanceRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTANCE_ROLE_UNSPECIFIED: _ClassVar[CrossInstanceReplicationConfig.InstanceRole]
        NONE: _ClassVar[CrossInstanceReplicationConfig.InstanceRole]
        PRIMARY: _ClassVar[CrossInstanceReplicationConfig.InstanceRole]
        SECONDARY: _ClassVar[CrossInstanceReplicationConfig.InstanceRole]
    INSTANCE_ROLE_UNSPECIFIED: CrossInstanceReplicationConfig.InstanceRole
    NONE: CrossInstanceReplicationConfig.InstanceRole
    PRIMARY: CrossInstanceReplicationConfig.InstanceRole
    SECONDARY: CrossInstanceReplicationConfig.InstanceRole

    class RemoteInstance(_message.Message):
        __slots__ = ('instance', 'uid')
        INSTANCE_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        instance: str
        uid: str

        def __init__(self, instance: _Optional[str]=..., uid: _Optional[str]=...) -> None:
            ...

    class Membership(_message.Message):
        __slots__ = ('primary_instance', 'secondary_instances')
        PRIMARY_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_INSTANCES_FIELD_NUMBER: _ClassVar[int]
        primary_instance: CrossInstanceReplicationConfig.RemoteInstance
        secondary_instances: _containers.RepeatedCompositeFieldContainer[CrossInstanceReplicationConfig.RemoteInstance]

        def __init__(self, primary_instance: _Optional[_Union[CrossInstanceReplicationConfig.RemoteInstance, _Mapping]]=..., secondary_instances: _Optional[_Iterable[_Union[CrossInstanceReplicationConfig.RemoteInstance, _Mapping]]]=...) -> None:
            ...
    INSTANCE_ROLE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    instance_role: CrossInstanceReplicationConfig.InstanceRole
    primary_instance: CrossInstanceReplicationConfig.RemoteInstance
    secondary_instances: _containers.RepeatedCompositeFieldContainer[CrossInstanceReplicationConfig.RemoteInstance]
    update_time: _timestamp_pb2.Timestamp
    membership: CrossInstanceReplicationConfig.Membership

    def __init__(self, instance_role: _Optional[_Union[CrossInstanceReplicationConfig.InstanceRole, str]]=..., primary_instance: _Optional[_Union[CrossInstanceReplicationConfig.RemoteInstance, _Mapping]]=..., secondary_instances: _Optional[_Iterable[_Union[CrossInstanceReplicationConfig.RemoteInstance, _Mapping]]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., membership: _Optional[_Union[CrossInstanceReplicationConfig.Membership, _Mapping]]=...) -> None:
        ...

class MaintenancePolicy(_message.Message):
    __slots__ = ('create_time', 'update_time', 'weekly_maintenance_window')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    weekly_maintenance_window: _containers.RepeatedCompositeFieldContainer[WeeklyMaintenanceWindow]

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., weekly_maintenance_window: _Optional[_Iterable[_Union[WeeklyMaintenanceWindow, _Mapping]]]=...) -> None:
        ...

class WeeklyMaintenanceWindow(_message.Message):
    __slots__ = ('day', 'start_time')
    DAY_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    day: _dayofweek_pb2.DayOfWeek
    start_time: _timeofday_pb2.TimeOfDay

    def __init__(self, day: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]]=..., start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=...) -> None:
        ...

class MaintenanceSchedule(_message.Message):
    __slots__ = ('start_time', 'end_time')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class PscAttachmentDetail(_message.Message):
    __slots__ = ('service_attachment', 'connection_type')
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    service_attachment: str
    connection_type: ConnectionType

    def __init__(self, service_attachment: _Optional[str]=..., connection_type: _Optional[_Union[ConnectionType, str]]=...) -> None:
        ...

class PscAutoConnection(_message.Message):
    __slots__ = ('port', 'psc_connection_id', 'ip_address', 'forwarding_rule', 'project_id', 'network', 'service_attachment', 'psc_connection_status', 'connection_type')
    PORT_FIELD_NUMBER: _ClassVar[int]
    PSC_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    PSC_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    port: int
    psc_connection_id: str
    ip_address: str
    forwarding_rule: str
    project_id: str
    network: str
    service_attachment: str
    psc_connection_status: PscConnectionStatus
    connection_type: ConnectionType

    def __init__(self, port: _Optional[int]=..., psc_connection_id: _Optional[str]=..., ip_address: _Optional[str]=..., forwarding_rule: _Optional[str]=..., project_id: _Optional[str]=..., network: _Optional[str]=..., service_attachment: _Optional[str]=..., psc_connection_status: _Optional[_Union[PscConnectionStatus, str]]=..., connection_type: _Optional[_Union[ConnectionType, str]]=...) -> None:
        ...

class PscConnection(_message.Message):
    __slots__ = ('port', 'psc_connection_id', 'ip_address', 'forwarding_rule', 'project_id', 'network', 'service_attachment', 'psc_connection_status', 'connection_type')
    PORT_FIELD_NUMBER: _ClassVar[int]
    PSC_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    PSC_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    port: int
    psc_connection_id: str
    ip_address: str
    forwarding_rule: str
    project_id: str
    network: str
    service_attachment: str
    psc_connection_status: PscConnectionStatus
    connection_type: ConnectionType

    def __init__(self, port: _Optional[int]=..., psc_connection_id: _Optional[str]=..., ip_address: _Optional[str]=..., forwarding_rule: _Optional[str]=..., project_id: _Optional[str]=..., network: _Optional[str]=..., service_attachment: _Optional[str]=..., psc_connection_status: _Optional[_Union[PscConnectionStatus, str]]=..., connection_type: _Optional[_Union[ConnectionType, str]]=...) -> None:
        ...

class DiscoveryEndpoint(_message.Message):
    __slots__ = ('address', 'port', 'network')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    network: str

    def __init__(self, address: _Optional[str]=..., port: _Optional[int]=..., network: _Optional[str]=...) -> None:
        ...

class PersistenceConfig(_message.Message):
    __slots__ = ('mode', 'rdb_config', 'aof_config')

    class PersistenceMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERSISTENCE_MODE_UNSPECIFIED: _ClassVar[PersistenceConfig.PersistenceMode]
        DISABLED: _ClassVar[PersistenceConfig.PersistenceMode]
        RDB: _ClassVar[PersistenceConfig.PersistenceMode]
        AOF: _ClassVar[PersistenceConfig.PersistenceMode]
    PERSISTENCE_MODE_UNSPECIFIED: PersistenceConfig.PersistenceMode
    DISABLED: PersistenceConfig.PersistenceMode
    RDB: PersistenceConfig.PersistenceMode
    AOF: PersistenceConfig.PersistenceMode

    class RDBConfig(_message.Message):
        __slots__ = ('rdb_snapshot_period', 'rdb_snapshot_start_time')

        class SnapshotPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SNAPSHOT_PERIOD_UNSPECIFIED: _ClassVar[PersistenceConfig.RDBConfig.SnapshotPeriod]
            ONE_HOUR: _ClassVar[PersistenceConfig.RDBConfig.SnapshotPeriod]
            SIX_HOURS: _ClassVar[PersistenceConfig.RDBConfig.SnapshotPeriod]
            TWELVE_HOURS: _ClassVar[PersistenceConfig.RDBConfig.SnapshotPeriod]
            TWENTY_FOUR_HOURS: _ClassVar[PersistenceConfig.RDBConfig.SnapshotPeriod]
        SNAPSHOT_PERIOD_UNSPECIFIED: PersistenceConfig.RDBConfig.SnapshotPeriod
        ONE_HOUR: PersistenceConfig.RDBConfig.SnapshotPeriod
        SIX_HOURS: PersistenceConfig.RDBConfig.SnapshotPeriod
        TWELVE_HOURS: PersistenceConfig.RDBConfig.SnapshotPeriod
        TWENTY_FOUR_HOURS: PersistenceConfig.RDBConfig.SnapshotPeriod
        RDB_SNAPSHOT_PERIOD_FIELD_NUMBER: _ClassVar[int]
        RDB_SNAPSHOT_START_TIME_FIELD_NUMBER: _ClassVar[int]
        rdb_snapshot_period: PersistenceConfig.RDBConfig.SnapshotPeriod
        rdb_snapshot_start_time: _timestamp_pb2.Timestamp

        def __init__(self, rdb_snapshot_period: _Optional[_Union[PersistenceConfig.RDBConfig.SnapshotPeriod, str]]=..., rdb_snapshot_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class AOFConfig(_message.Message):
        __slots__ = ('append_fsync',)

        class AppendFsync(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            APPEND_FSYNC_UNSPECIFIED: _ClassVar[PersistenceConfig.AOFConfig.AppendFsync]
            NEVER: _ClassVar[PersistenceConfig.AOFConfig.AppendFsync]
            EVERY_SEC: _ClassVar[PersistenceConfig.AOFConfig.AppendFsync]
            ALWAYS: _ClassVar[PersistenceConfig.AOFConfig.AppendFsync]
        APPEND_FSYNC_UNSPECIFIED: PersistenceConfig.AOFConfig.AppendFsync
        NEVER: PersistenceConfig.AOFConfig.AppendFsync
        EVERY_SEC: PersistenceConfig.AOFConfig.AppendFsync
        ALWAYS: PersistenceConfig.AOFConfig.AppendFsync
        APPEND_FSYNC_FIELD_NUMBER: _ClassVar[int]
        append_fsync: PersistenceConfig.AOFConfig.AppendFsync

        def __init__(self, append_fsync: _Optional[_Union[PersistenceConfig.AOFConfig.AppendFsync, str]]=...) -> None:
            ...
    MODE_FIELD_NUMBER: _ClassVar[int]
    RDB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AOF_CONFIG_FIELD_NUMBER: _ClassVar[int]
    mode: PersistenceConfig.PersistenceMode
    rdb_config: PersistenceConfig.RDBConfig
    aof_config: PersistenceConfig.AOFConfig

    def __init__(self, mode: _Optional[_Union[PersistenceConfig.PersistenceMode, str]]=..., rdb_config: _Optional[_Union[PersistenceConfig.RDBConfig, _Mapping]]=..., aof_config: _Optional[_Union[PersistenceConfig.AOFConfig, _Mapping]]=...) -> None:
        ...

class NodeConfig(_message.Message):
    __slots__ = ('size_gb',)
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    size_gb: float

    def __init__(self, size_gb: _Optional[float]=...) -> None:
        ...

class ZoneDistributionConfig(_message.Message):
    __slots__ = ('zone', 'mode')

    class ZoneDistributionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ZONE_DISTRIBUTION_MODE_UNSPECIFIED: _ClassVar[ZoneDistributionConfig.ZoneDistributionMode]
        MULTI_ZONE: _ClassVar[ZoneDistributionConfig.ZoneDistributionMode]
        SINGLE_ZONE: _ClassVar[ZoneDistributionConfig.ZoneDistributionMode]
    ZONE_DISTRIBUTION_MODE_UNSPECIFIED: ZoneDistributionConfig.ZoneDistributionMode
    MULTI_ZONE: ZoneDistributionConfig.ZoneDistributionMode
    SINGLE_ZONE: ZoneDistributionConfig.ZoneDistributionMode
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    zone: str
    mode: ZoneDistributionConfig.ZoneDistributionMode

    def __init__(self, zone: _Optional[str]=..., mode: _Optional[_Union[ZoneDistributionConfig.ZoneDistributionMode, str]]=...) -> None:
        ...

class RescheduleMaintenanceRequest(_message.Message):
    __slots__ = ('name', 'reschedule_type', 'schedule_time')

    class RescheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESCHEDULE_TYPE_UNSPECIFIED: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
        IMMEDIATE: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
        SPECIFIC_TIME: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
    RESCHEDULE_TYPE_UNSPECIFIED: RescheduleMaintenanceRequest.RescheduleType
    IMMEDIATE: RescheduleMaintenanceRequest.RescheduleType
    SPECIFIC_TIME: RescheduleMaintenanceRequest.RescheduleType
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    reschedule_type: RescheduleMaintenanceRequest.RescheduleType
    schedule_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., reschedule_type: _Optional[_Union[RescheduleMaintenanceRequest.RescheduleType, str]]=..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token', 'unreachable')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id', 'instance', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: Instance
    request_id: str

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=..., instance: _Optional[_Union[Instance, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ('update_mask', 'instance', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    instance: Instance
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., instance: _Optional[_Union[Instance, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
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

class BackupInstanceRequest(_message.Message):
    __slots__ = ('name', 'ttl', 'backup_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    ttl: _duration_pb2.Duration
    backup_id: str

    def __init__(self, name: _Optional[str]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., backup_id: _Optional[str]=...) -> None:
        ...

class GetCertificateAuthorityRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
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