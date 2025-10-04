from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.alloydb.v1alpha import csql_resources_pb2 as _csql_resources_pb2
from google.cloud.alloydb.v1alpha import gemini_pb2 as _gemini_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import date_pb2 as _date_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InstanceView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTANCE_VIEW_UNSPECIFIED: _ClassVar[InstanceView]
    INSTANCE_VIEW_BASIC: _ClassVar[InstanceView]
    INSTANCE_VIEW_FULL: _ClassVar[InstanceView]

class ClusterView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_VIEW_UNSPECIFIED: _ClassVar[ClusterView]
    CLUSTER_VIEW_BASIC: _ClassVar[ClusterView]
    CLUSTER_VIEW_CONTINUOUS_BACKUP: _ClassVar[ClusterView]

class DatabaseVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_VERSION_UNSPECIFIED: _ClassVar[DatabaseVersion]
    POSTGRES_13: _ClassVar[DatabaseVersion]
    POSTGRES_14: _ClassVar[DatabaseVersion]
    POSTGRES_15: _ClassVar[DatabaseVersion]
    POSTGRES_16: _ClassVar[DatabaseVersion]
    POSTGRES_17: _ClassVar[DatabaseVersion]

class SubscriptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_TYPE_UNSPECIFIED: _ClassVar[SubscriptionType]
    STANDARD: _ClassVar[SubscriptionType]
    TRIAL: _ClassVar[SubscriptionType]
INSTANCE_VIEW_UNSPECIFIED: InstanceView
INSTANCE_VIEW_BASIC: InstanceView
INSTANCE_VIEW_FULL: InstanceView
CLUSTER_VIEW_UNSPECIFIED: ClusterView
CLUSTER_VIEW_BASIC: ClusterView
CLUSTER_VIEW_CONTINUOUS_BACKUP: ClusterView
DATABASE_VERSION_UNSPECIFIED: DatabaseVersion
POSTGRES_13: DatabaseVersion
POSTGRES_14: DatabaseVersion
POSTGRES_15: DatabaseVersion
POSTGRES_16: DatabaseVersion
POSTGRES_17: DatabaseVersion
SUBSCRIPTION_TYPE_UNSPECIFIED: SubscriptionType
STANDARD: SubscriptionType
TRIAL: SubscriptionType

class UserPassword(_message.Message):
    __slots__ = ('user', 'password')
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    password: str

    def __init__(self, user: _Optional[str]=..., password: _Optional[str]=...) -> None:
        ...

class MigrationSource(_message.Message):
    __slots__ = ('host_port', 'reference_id', 'source_type')

    class MigrationSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MIGRATION_SOURCE_TYPE_UNSPECIFIED: _ClassVar[MigrationSource.MigrationSourceType]
        DMS: _ClassVar[MigrationSource.MigrationSourceType]
    MIGRATION_SOURCE_TYPE_UNSPECIFIED: MigrationSource.MigrationSourceType
    DMS: MigrationSource.MigrationSourceType
    HOST_PORT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    host_port: str
    reference_id: str
    source_type: MigrationSource.MigrationSourceType

    def __init__(self, host_port: _Optional[str]=..., reference_id: _Optional[str]=..., source_type: _Optional[_Union[MigrationSource.MigrationSourceType, str]]=...) -> None:
        ...

class EncryptionConfig(_message.Message):
    __slots__ = ('kms_key_name',)
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: str

    def __init__(self, kms_key_name: _Optional[str]=...) -> None:
        ...

class EncryptionInfo(_message.Message):
    __slots__ = ('encryption_type', 'kms_key_versions')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[EncryptionInfo.Type]
        GOOGLE_DEFAULT_ENCRYPTION: _ClassVar[EncryptionInfo.Type]
        CUSTOMER_MANAGED_ENCRYPTION: _ClassVar[EncryptionInfo.Type]
    TYPE_UNSPECIFIED: EncryptionInfo.Type
    GOOGLE_DEFAULT_ENCRYPTION: EncryptionInfo.Type
    CUSTOMER_MANAGED_ENCRYPTION: EncryptionInfo.Type
    ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    encryption_type: EncryptionInfo.Type
    kms_key_versions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, encryption_type: _Optional[_Union[EncryptionInfo.Type, str]]=..., kms_key_versions: _Optional[_Iterable[str]]=...) -> None:
        ...

class SslConfig(_message.Message):
    __slots__ = ('ssl_mode', 'ca_source')

    class SslMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SSL_MODE_UNSPECIFIED: _ClassVar[SslConfig.SslMode]
        SSL_MODE_ALLOW: _ClassVar[SslConfig.SslMode]
        SSL_MODE_REQUIRE: _ClassVar[SslConfig.SslMode]
        SSL_MODE_VERIFY_CA: _ClassVar[SslConfig.SslMode]
        ALLOW_UNENCRYPTED_AND_ENCRYPTED: _ClassVar[SslConfig.SslMode]
        ENCRYPTED_ONLY: _ClassVar[SslConfig.SslMode]
    SSL_MODE_UNSPECIFIED: SslConfig.SslMode
    SSL_MODE_ALLOW: SslConfig.SslMode
    SSL_MODE_REQUIRE: SslConfig.SslMode
    SSL_MODE_VERIFY_CA: SslConfig.SslMode
    ALLOW_UNENCRYPTED_AND_ENCRYPTED: SslConfig.SslMode
    ENCRYPTED_ONLY: SslConfig.SslMode

    class CaSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CA_SOURCE_UNSPECIFIED: _ClassVar[SslConfig.CaSource]
        CA_SOURCE_MANAGED: _ClassVar[SslConfig.CaSource]
    CA_SOURCE_UNSPECIFIED: SslConfig.CaSource
    CA_SOURCE_MANAGED: SslConfig.CaSource
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    CA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ssl_mode: SslConfig.SslMode
    ca_source: SslConfig.CaSource

    def __init__(self, ssl_mode: _Optional[_Union[SslConfig.SslMode, str]]=..., ca_source: _Optional[_Union[SslConfig.CaSource, str]]=...) -> None:
        ...

class AutomatedBackupPolicy(_message.Message):
    __slots__ = ('weekly_schedule', 'time_based_retention', 'quantity_based_retention', 'enabled', 'backup_window', 'encryption_config', 'location', 'labels')

    class WeeklySchedule(_message.Message):
        __slots__ = ('start_times', 'days_of_week')
        START_TIMES_FIELD_NUMBER: _ClassVar[int]
        DAYS_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
        start_times: _containers.RepeatedCompositeFieldContainer[_timeofday_pb2.TimeOfDay]
        days_of_week: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]

        def __init__(self, start_times: _Optional[_Iterable[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]]=..., days_of_week: _Optional[_Iterable[_Union[_dayofweek_pb2.DayOfWeek, str]]]=...) -> None:
            ...

    class TimeBasedRetention(_message.Message):
        __slots__ = ('retention_period',)
        RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
        retention_period: _duration_pb2.Duration

        def __init__(self, retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class QuantityBasedRetention(_message.Message):
        __slots__ = ('count',)
        COUNT_FIELD_NUMBER: _ClassVar[int]
        count: int

        def __init__(self, count: _Optional[int]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    WEEKLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIME_BASED_RETENTION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_BASED_RETENTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_WINDOW_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    weekly_schedule: AutomatedBackupPolicy.WeeklySchedule
    time_based_retention: AutomatedBackupPolicy.TimeBasedRetention
    quantity_based_retention: AutomatedBackupPolicy.QuantityBasedRetention
    enabled: bool
    backup_window: _duration_pb2.Duration
    encryption_config: EncryptionConfig
    location: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, weekly_schedule: _Optional[_Union[AutomatedBackupPolicy.WeeklySchedule, _Mapping]]=..., time_based_retention: _Optional[_Union[AutomatedBackupPolicy.TimeBasedRetention, _Mapping]]=..., quantity_based_retention: _Optional[_Union[AutomatedBackupPolicy.QuantityBasedRetention, _Mapping]]=..., enabled: bool=..., backup_window: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., encryption_config: _Optional[_Union[EncryptionConfig, _Mapping]]=..., location: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ContinuousBackupConfig(_message.Message):
    __slots__ = ('enabled', 'recovery_window_days', 'encryption_config')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    recovery_window_days: int
    encryption_config: EncryptionConfig

    def __init__(self, enabled: bool=..., recovery_window_days: _Optional[int]=..., encryption_config: _Optional[_Union[EncryptionConfig, _Mapping]]=...) -> None:
        ...

class ContinuousBackupInfo(_message.Message):
    __slots__ = ('encryption_info', 'enabled_time', 'schedule', 'earliest_restorable_time')
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ENABLED_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_RESTORABLE_TIME_FIELD_NUMBER: _ClassVar[int]
    encryption_info: EncryptionInfo
    enabled_time: _timestamp_pb2.Timestamp
    schedule: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]
    earliest_restorable_time: _timestamp_pb2.Timestamp

    def __init__(self, encryption_info: _Optional[_Union[EncryptionInfo, _Mapping]]=..., enabled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., schedule: _Optional[_Iterable[_Union[_dayofweek_pb2.DayOfWeek, str]]]=..., earliest_restorable_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BackupSource(_message.Message):
    __slots__ = ('backup_uid', 'backup_name')
    BACKUP_UID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_NAME_FIELD_NUMBER: _ClassVar[int]
    backup_uid: str
    backup_name: str

    def __init__(self, backup_uid: _Optional[str]=..., backup_name: _Optional[str]=...) -> None:
        ...

class ContinuousBackupSource(_message.Message):
    __slots__ = ('cluster', 'point_in_time')
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    point_in_time: _timestamp_pb2.Timestamp

    def __init__(self, cluster: _Optional[str]=..., point_in_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class MaintenanceUpdatePolicy(_message.Message):
    __slots__ = ('maintenance_windows', 'deny_maintenance_periods')

    class MaintenanceWindow(_message.Message):
        __slots__ = ('day', 'start_time')
        DAY_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        day: _dayofweek_pb2.DayOfWeek
        start_time: _timeofday_pb2.TimeOfDay

        def __init__(self, day: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]]=..., start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=...) -> None:
            ...

    class DenyMaintenancePeriod(_message.Message):
        __slots__ = ('start_date', 'end_date', 'time')
        START_DATE_FIELD_NUMBER: _ClassVar[int]
        END_DATE_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        start_date: _date_pb2.Date
        end_date: _date_pb2.Date
        time: _timeofday_pb2.TimeOfDay

        def __init__(self, start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=...) -> None:
            ...
    MAINTENANCE_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    DENY_MAINTENANCE_PERIODS_FIELD_NUMBER: _ClassVar[int]
    maintenance_windows: _containers.RepeatedCompositeFieldContainer[MaintenanceUpdatePolicy.MaintenanceWindow]
    deny_maintenance_periods: _containers.RepeatedCompositeFieldContainer[MaintenanceUpdatePolicy.DenyMaintenancePeriod]

    def __init__(self, maintenance_windows: _Optional[_Iterable[_Union[MaintenanceUpdatePolicy.MaintenanceWindow, _Mapping]]]=..., deny_maintenance_periods: _Optional[_Iterable[_Union[MaintenanceUpdatePolicy.DenyMaintenancePeriod, _Mapping]]]=...) -> None:
        ...

class MaintenanceSchedule(_message.Message):
    __slots__ = ('start_time',)
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Cluster(_message.Message):
    __slots__ = ('backup_source', 'migration_source', 'cloudsql_backup_run_source', 'name', 'display_name', 'uid', 'create_time', 'update_time', 'delete_time', 'labels', 'state', 'cluster_type', 'database_version', 'network_config', 'network', 'etag', 'annotations', 'reconciling', 'initial_user', 'automated_backup_policy', 'ssl_config', 'encryption_config', 'encryption_info', 'continuous_backup_config', 'continuous_backup_info', 'secondary_config', 'primary_config', 'satisfies_pzi', 'satisfies_pzs', 'psc_config', 'maintenance_update_policy', 'maintenance_schedule', 'gemini_config', 'subscription_type', 'trial_metadata', 'tags', 'service_account_email')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Cluster.State]
        READY: _ClassVar[Cluster.State]
        STOPPED: _ClassVar[Cluster.State]
        EMPTY: _ClassVar[Cluster.State]
        CREATING: _ClassVar[Cluster.State]
        DELETING: _ClassVar[Cluster.State]
        FAILED: _ClassVar[Cluster.State]
        BOOTSTRAPPING: _ClassVar[Cluster.State]
        MAINTENANCE: _ClassVar[Cluster.State]
        PROMOTING: _ClassVar[Cluster.State]
    STATE_UNSPECIFIED: Cluster.State
    READY: Cluster.State
    STOPPED: Cluster.State
    EMPTY: Cluster.State
    CREATING: Cluster.State
    DELETING: Cluster.State
    FAILED: Cluster.State
    BOOTSTRAPPING: Cluster.State
    MAINTENANCE: Cluster.State
    PROMOTING: Cluster.State

    class ClusterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLUSTER_TYPE_UNSPECIFIED: _ClassVar[Cluster.ClusterType]
        PRIMARY: _ClassVar[Cluster.ClusterType]
        SECONDARY: _ClassVar[Cluster.ClusterType]
    CLUSTER_TYPE_UNSPECIFIED: Cluster.ClusterType
    PRIMARY: Cluster.ClusterType
    SECONDARY: Cluster.ClusterType

    class NetworkConfig(_message.Message):
        __slots__ = ('network', 'allocated_ip_range')
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        ALLOCATED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
        network: str
        allocated_ip_range: str

        def __init__(self, network: _Optional[str]=..., allocated_ip_range: _Optional[str]=...) -> None:
            ...

    class SecondaryConfig(_message.Message):
        __slots__ = ('primary_cluster_name',)
        PRIMARY_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        primary_cluster_name: str

        def __init__(self, primary_cluster_name: _Optional[str]=...) -> None:
            ...

    class PrimaryConfig(_message.Message):
        __slots__ = ('secondary_cluster_names',)
        SECONDARY_CLUSTER_NAMES_FIELD_NUMBER: _ClassVar[int]
        secondary_cluster_names: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, secondary_cluster_names: _Optional[_Iterable[str]]=...) -> None:
            ...

    class PscConfig(_message.Message):
        __slots__ = ('psc_enabled', 'service_owned_project_number')
        PSC_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SERVICE_OWNED_PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        psc_enabled: bool
        service_owned_project_number: int

        def __init__(self, psc_enabled: bool=..., service_owned_project_number: _Optional[int]=...) -> None:
            ...

    class TrialMetadata(_message.Message):
        __slots__ = ('start_time', 'end_time', 'upgrade_time', 'grace_end_time')
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_TIME_FIELD_NUMBER: _ClassVar[int]
        GRACE_END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        upgrade_time: _timestamp_pb2.Timestamp
        grace_end_time: _timestamp_pb2.Timestamp

        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., upgrade_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., grace_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class TagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    BACKUP_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CLOUDSQL_BACKUP_RUN_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    INITIAL_USER_FIELD_NUMBER: _ClassVar[int]
    AUTOMATED_BACKUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    SSL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_BACKUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    PSC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_UPDATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    GEMINI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRIAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    backup_source: BackupSource
    migration_source: MigrationSource
    cloudsql_backup_run_source: _csql_resources_pb2.CloudSQLBackupRunSource
    name: str
    display_name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Cluster.State
    cluster_type: Cluster.ClusterType
    database_version: DatabaseVersion
    network_config: Cluster.NetworkConfig
    network: str
    etag: str
    annotations: _containers.ScalarMap[str, str]
    reconciling: bool
    initial_user: UserPassword
    automated_backup_policy: AutomatedBackupPolicy
    ssl_config: SslConfig
    encryption_config: EncryptionConfig
    encryption_info: EncryptionInfo
    continuous_backup_config: ContinuousBackupConfig
    continuous_backup_info: ContinuousBackupInfo
    secondary_config: Cluster.SecondaryConfig
    primary_config: Cluster.PrimaryConfig
    satisfies_pzi: bool
    satisfies_pzs: bool
    psc_config: Cluster.PscConfig
    maintenance_update_policy: MaintenanceUpdatePolicy
    maintenance_schedule: MaintenanceSchedule
    gemini_config: _gemini_pb2.GeminiClusterConfig
    subscription_type: SubscriptionType
    trial_metadata: Cluster.TrialMetadata
    tags: _containers.ScalarMap[str, str]
    service_account_email: str

    def __init__(self, backup_source: _Optional[_Union[BackupSource, _Mapping]]=..., migration_source: _Optional[_Union[MigrationSource, _Mapping]]=..., cloudsql_backup_run_source: _Optional[_Union[_csql_resources_pb2.CloudSQLBackupRunSource, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Cluster.State, str]]=..., cluster_type: _Optional[_Union[Cluster.ClusterType, str]]=..., database_version: _Optional[_Union[DatabaseVersion, str]]=..., network_config: _Optional[_Union[Cluster.NetworkConfig, _Mapping]]=..., network: _Optional[str]=..., etag: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., reconciling: bool=..., initial_user: _Optional[_Union[UserPassword, _Mapping]]=..., automated_backup_policy: _Optional[_Union[AutomatedBackupPolicy, _Mapping]]=..., ssl_config: _Optional[_Union[SslConfig, _Mapping]]=..., encryption_config: _Optional[_Union[EncryptionConfig, _Mapping]]=..., encryption_info: _Optional[_Union[EncryptionInfo, _Mapping]]=..., continuous_backup_config: _Optional[_Union[ContinuousBackupConfig, _Mapping]]=..., continuous_backup_info: _Optional[_Union[ContinuousBackupInfo, _Mapping]]=..., secondary_config: _Optional[_Union[Cluster.SecondaryConfig, _Mapping]]=..., primary_config: _Optional[_Union[Cluster.PrimaryConfig, _Mapping]]=..., satisfies_pzi: bool=..., satisfies_pzs: bool=..., psc_config: _Optional[_Union[Cluster.PscConfig, _Mapping]]=..., maintenance_update_policy: _Optional[_Union[MaintenanceUpdatePolicy, _Mapping]]=..., maintenance_schedule: _Optional[_Union[MaintenanceSchedule, _Mapping]]=..., gemini_config: _Optional[_Union[_gemini_pb2.GeminiClusterConfig, _Mapping]]=..., subscription_type: _Optional[_Union[SubscriptionType, str]]=..., trial_metadata: _Optional[_Union[Cluster.TrialMetadata, _Mapping]]=..., tags: _Optional[_Mapping[str, str]]=..., service_account_email: _Optional[str]=...) -> None:
        ...

class Instance(_message.Message):
    __slots__ = ('name', 'display_name', 'uid', 'create_time', 'update_time', 'delete_time', 'labels', 'state', 'instance_type', 'machine_config', 'availability_type', 'gce_zone', 'database_flags', 'writable_node', 'nodes', 'query_insights_config', 'observability_config', 'read_pool_config', 'ip_address', 'public_ip_address', 'reconciling', 'etag', 'annotations', 'update_policy', 'client_connection_config', 'satisfies_pzi', 'satisfies_pzs', 'psc_instance_config', 'network_config', 'gemini_config', 'outbound_public_ip_addresses', 'activation_policy', 'connection_pool_config', 'gca_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        READY: _ClassVar[Instance.State]
        STOPPED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
        MAINTENANCE: _ClassVar[Instance.State]
        FAILED: _ClassVar[Instance.State]
        BOOTSTRAPPING: _ClassVar[Instance.State]
        PROMOTING: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    READY: Instance.State
    STOPPED: Instance.State
    CREATING: Instance.State
    DELETING: Instance.State
    MAINTENANCE: Instance.State
    FAILED: Instance.State
    BOOTSTRAPPING: Instance.State
    PROMOTING: Instance.State

    class InstanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTANCE_TYPE_UNSPECIFIED: _ClassVar[Instance.InstanceType]
        PRIMARY: _ClassVar[Instance.InstanceType]
        READ_POOL: _ClassVar[Instance.InstanceType]
        SECONDARY: _ClassVar[Instance.InstanceType]
    INSTANCE_TYPE_UNSPECIFIED: Instance.InstanceType
    PRIMARY: Instance.InstanceType
    READ_POOL: Instance.InstanceType
    SECONDARY: Instance.InstanceType

    class AvailabilityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AVAILABILITY_TYPE_UNSPECIFIED: _ClassVar[Instance.AvailabilityType]
        ZONAL: _ClassVar[Instance.AvailabilityType]
        REGIONAL: _ClassVar[Instance.AvailabilityType]
    AVAILABILITY_TYPE_UNSPECIFIED: Instance.AvailabilityType
    ZONAL: Instance.AvailabilityType
    REGIONAL: Instance.AvailabilityType

    class ActivationPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTIVATION_POLICY_UNSPECIFIED: _ClassVar[Instance.ActivationPolicy]
        ALWAYS: _ClassVar[Instance.ActivationPolicy]
        NEVER: _ClassVar[Instance.ActivationPolicy]
    ACTIVATION_POLICY_UNSPECIFIED: Instance.ActivationPolicy
    ALWAYS: Instance.ActivationPolicy
    NEVER: Instance.ActivationPolicy

    class MachineConfig(_message.Message):
        __slots__ = ('cpu_count', 'machine_type')
        CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
        MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
        cpu_count: int
        machine_type: str

        def __init__(self, cpu_count: _Optional[int]=..., machine_type: _Optional[str]=...) -> None:
            ...

    class Node(_message.Message):
        __slots__ = ('zone_id', 'id', 'ip', 'state')
        ZONE_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        zone_id: str
        id: str
        ip: str
        state: str

        def __init__(self, zone_id: _Optional[str]=..., id: _Optional[str]=..., ip: _Optional[str]=..., state: _Optional[str]=...) -> None:
            ...

    class QueryInsightsInstanceConfig(_message.Message):
        __slots__ = ('record_application_tags', 'record_client_address', 'query_string_length', 'query_plans_per_minute')
        RECORD_APPLICATION_TAGS_FIELD_NUMBER: _ClassVar[int]
        RECORD_CLIENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        QUERY_STRING_LENGTH_FIELD_NUMBER: _ClassVar[int]
        QUERY_PLANS_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
        record_application_tags: bool
        record_client_address: bool
        query_string_length: int
        query_plans_per_minute: int

        def __init__(self, record_application_tags: bool=..., record_client_address: bool=..., query_string_length: _Optional[int]=..., query_plans_per_minute: _Optional[int]=...) -> None:
            ...

    class ObservabilityInstanceConfig(_message.Message):
        __slots__ = ('enabled', 'preserve_comments', 'track_wait_events', 'track_wait_event_types', 'max_query_string_length', 'record_application_tags', 'query_plans_per_minute', 'track_active_queries', 'track_client_address', 'assistive_experiences_enabled')
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        PRESERVE_COMMENTS_FIELD_NUMBER: _ClassVar[int]
        TRACK_WAIT_EVENTS_FIELD_NUMBER: _ClassVar[int]
        TRACK_WAIT_EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
        MAX_QUERY_STRING_LENGTH_FIELD_NUMBER: _ClassVar[int]
        RECORD_APPLICATION_TAGS_FIELD_NUMBER: _ClassVar[int]
        QUERY_PLANS_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
        TRACK_ACTIVE_QUERIES_FIELD_NUMBER: _ClassVar[int]
        TRACK_CLIENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        ASSISTIVE_EXPERIENCES_ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        preserve_comments: bool
        track_wait_events: bool
        track_wait_event_types: bool
        max_query_string_length: int
        record_application_tags: bool
        query_plans_per_minute: int
        track_active_queries: bool
        track_client_address: bool
        assistive_experiences_enabled: bool

        def __init__(self, enabled: bool=..., preserve_comments: bool=..., track_wait_events: bool=..., track_wait_event_types: bool=..., max_query_string_length: _Optional[int]=..., record_application_tags: bool=..., query_plans_per_minute: _Optional[int]=..., track_active_queries: bool=..., track_client_address: bool=..., assistive_experiences_enabled: bool=...) -> None:
            ...

    class ReadPoolConfig(_message.Message):
        __slots__ = ('node_count',)
        NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
        node_count: int

        def __init__(self, node_count: _Optional[int]=...) -> None:
            ...

    class UpdatePolicy(_message.Message):
        __slots__ = ('mode',)

        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_UNSPECIFIED: _ClassVar[Instance.UpdatePolicy.Mode]
            DEFAULT: _ClassVar[Instance.UpdatePolicy.Mode]
            FORCE_APPLY: _ClassVar[Instance.UpdatePolicy.Mode]
        MODE_UNSPECIFIED: Instance.UpdatePolicy.Mode
        DEFAULT: Instance.UpdatePolicy.Mode
        FORCE_APPLY: Instance.UpdatePolicy.Mode
        MODE_FIELD_NUMBER: _ClassVar[int]
        mode: Instance.UpdatePolicy.Mode

        def __init__(self, mode: _Optional[_Union[Instance.UpdatePolicy.Mode, str]]=...) -> None:
            ...

    class ClientConnectionConfig(_message.Message):
        __slots__ = ('require_connectors', 'ssl_config')
        REQUIRE_CONNECTORS_FIELD_NUMBER: _ClassVar[int]
        SSL_CONFIG_FIELD_NUMBER: _ClassVar[int]
        require_connectors: bool
        ssl_config: SslConfig

        def __init__(self, require_connectors: bool=..., ssl_config: _Optional[_Union[SslConfig, _Mapping]]=...) -> None:
            ...

    class PscInterfaceConfig(_message.Message):
        __slots__ = ('network_attachment_resource',)
        NETWORK_ATTACHMENT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        network_attachment_resource: str

        def __init__(self, network_attachment_resource: _Optional[str]=...) -> None:
            ...

    class PscAutoConnectionConfig(_message.Message):
        __slots__ = ('consumer_project', 'consumer_network', 'ip_address', 'status', 'consumer_network_status')
        CONSUMER_PROJECT_FIELD_NUMBER: _ClassVar[int]
        CONSUMER_NETWORK_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CONSUMER_NETWORK_STATUS_FIELD_NUMBER: _ClassVar[int]
        consumer_project: str
        consumer_network: str
        ip_address: str
        status: str
        consumer_network_status: str

        def __init__(self, consumer_project: _Optional[str]=..., consumer_network: _Optional[str]=..., ip_address: _Optional[str]=..., status: _Optional[str]=..., consumer_network_status: _Optional[str]=...) -> None:
            ...

    class PscInstanceConfig(_message.Message):
        __slots__ = ('service_attachment_link', 'allowed_consumer_projects', 'psc_dns_name', 'psc_interface_configs', 'psc_auto_connections')
        SERVICE_ATTACHMENT_LINK_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_CONSUMER_PROJECTS_FIELD_NUMBER: _ClassVar[int]
        PSC_DNS_NAME_FIELD_NUMBER: _ClassVar[int]
        PSC_INTERFACE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        PSC_AUTO_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        service_attachment_link: str
        allowed_consumer_projects: _containers.RepeatedScalarFieldContainer[str]
        psc_dns_name: str
        psc_interface_configs: _containers.RepeatedCompositeFieldContainer[Instance.PscInterfaceConfig]
        psc_auto_connections: _containers.RepeatedCompositeFieldContainer[Instance.PscAutoConnectionConfig]

        def __init__(self, service_attachment_link: _Optional[str]=..., allowed_consumer_projects: _Optional[_Iterable[str]]=..., psc_dns_name: _Optional[str]=..., psc_interface_configs: _Optional[_Iterable[_Union[Instance.PscInterfaceConfig, _Mapping]]]=..., psc_auto_connections: _Optional[_Iterable[_Union[Instance.PscAutoConnectionConfig, _Mapping]]]=...) -> None:
            ...

    class InstanceNetworkConfig(_message.Message):
        __slots__ = ('authorized_external_networks', 'enable_public_ip', 'enable_outbound_public_ip', 'network', 'allocated_ip_range_override')

        class AuthorizedNetwork(_message.Message):
            __slots__ = ('cidr_range',)
            CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
            cidr_range: str

            def __init__(self, cidr_range: _Optional[str]=...) -> None:
                ...
        AUTHORIZED_EXTERNAL_NETWORKS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
        ENABLE_OUTBOUND_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        ALLOCATED_IP_RANGE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        authorized_external_networks: _containers.RepeatedCompositeFieldContainer[Instance.InstanceNetworkConfig.AuthorizedNetwork]
        enable_public_ip: bool
        enable_outbound_public_ip: bool
        network: str
        allocated_ip_range_override: str

        def __init__(self, authorized_external_networks: _Optional[_Iterable[_Union[Instance.InstanceNetworkConfig.AuthorizedNetwork, _Mapping]]]=..., enable_public_ip: bool=..., enable_outbound_public_ip: bool=..., network: _Optional[str]=..., allocated_ip_range_override: _Optional[str]=...) -> None:
            ...

    class ConnectionPoolConfig(_message.Message):
        __slots__ = ('enabled', 'flags', 'pooler_count')

        class FlagsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        POOLER_COUNT_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        flags: _containers.ScalarMap[str, str]
        pooler_count: int

        def __init__(self, enabled: bool=..., flags: _Optional[_Mapping[str, str]]=..., pooler_count: _Optional[int]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class DatabaseFlagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    GCE_ZONE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    WRITABLE_NODE_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    QUERY_INSIGHTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OBSERVABILITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    READ_POOL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CONNECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    PSC_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GEMINI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_PUBLIC_IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_POOL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GCA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Instance.State
    instance_type: Instance.InstanceType
    machine_config: Instance.MachineConfig
    availability_type: Instance.AvailabilityType
    gce_zone: str
    database_flags: _containers.ScalarMap[str, str]
    writable_node: Instance.Node
    nodes: _containers.RepeatedCompositeFieldContainer[Instance.Node]
    query_insights_config: Instance.QueryInsightsInstanceConfig
    observability_config: Instance.ObservabilityInstanceConfig
    read_pool_config: Instance.ReadPoolConfig
    ip_address: str
    public_ip_address: str
    reconciling: bool
    etag: str
    annotations: _containers.ScalarMap[str, str]
    update_policy: Instance.UpdatePolicy
    client_connection_config: Instance.ClientConnectionConfig
    satisfies_pzi: bool
    satisfies_pzs: bool
    psc_instance_config: Instance.PscInstanceConfig
    network_config: Instance.InstanceNetworkConfig
    gemini_config: _gemini_pb2.GeminiInstanceConfig
    outbound_public_ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    activation_policy: Instance.ActivationPolicy
    connection_pool_config: Instance.ConnectionPoolConfig
    gca_config: _gemini_pb2.GCAInstanceConfig

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Instance.State, str]]=..., instance_type: _Optional[_Union[Instance.InstanceType, str]]=..., machine_config: _Optional[_Union[Instance.MachineConfig, _Mapping]]=..., availability_type: _Optional[_Union[Instance.AvailabilityType, str]]=..., gce_zone: _Optional[str]=..., database_flags: _Optional[_Mapping[str, str]]=..., writable_node: _Optional[_Union[Instance.Node, _Mapping]]=..., nodes: _Optional[_Iterable[_Union[Instance.Node, _Mapping]]]=..., query_insights_config: _Optional[_Union[Instance.QueryInsightsInstanceConfig, _Mapping]]=..., observability_config: _Optional[_Union[Instance.ObservabilityInstanceConfig, _Mapping]]=..., read_pool_config: _Optional[_Union[Instance.ReadPoolConfig, _Mapping]]=..., ip_address: _Optional[str]=..., public_ip_address: _Optional[str]=..., reconciling: bool=..., etag: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., update_policy: _Optional[_Union[Instance.UpdatePolicy, _Mapping]]=..., client_connection_config: _Optional[_Union[Instance.ClientConnectionConfig, _Mapping]]=..., satisfies_pzi: bool=..., satisfies_pzs: bool=..., psc_instance_config: _Optional[_Union[Instance.PscInstanceConfig, _Mapping]]=..., network_config: _Optional[_Union[Instance.InstanceNetworkConfig, _Mapping]]=..., gemini_config: _Optional[_Union[_gemini_pb2.GeminiInstanceConfig, _Mapping]]=..., outbound_public_ip_addresses: _Optional[_Iterable[str]]=..., activation_policy: _Optional[_Union[Instance.ActivationPolicy, str]]=..., connection_pool_config: _Optional[_Union[Instance.ConnectionPoolConfig, _Mapping]]=..., gca_config: _Optional[_Union[_gemini_pb2.GCAInstanceConfig, _Mapping]]=...) -> None:
        ...

class ConnectionInfo(_message.Message):
    __slots__ = ('name', 'ip_address', 'public_ip_address', 'pem_certificate_chain', 'instance_uid', 'psc_dns_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PEM_CERTIFICATE_CHAIN_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_UID_FIELD_NUMBER: _ClassVar[int]
    PSC_DNS_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    ip_address: str
    public_ip_address: str
    pem_certificate_chain: _containers.RepeatedScalarFieldContainer[str]
    instance_uid: str
    psc_dns_name: str

    def __init__(self, name: _Optional[str]=..., ip_address: _Optional[str]=..., public_ip_address: _Optional[str]=..., pem_certificate_chain: _Optional[_Iterable[str]]=..., instance_uid: _Optional[str]=..., psc_dns_name: _Optional[str]=...) -> None:
        ...

class Backup(_message.Message):
    __slots__ = ('name', 'display_name', 'uid', 'create_time', 'update_time', 'delete_time', 'create_completion_time', 'labels', 'state', 'type', 'description', 'cluster_uid', 'cluster_name', 'reconciling', 'encryption_config', 'encryption_info', 'etag', 'annotations', 'size_bytes', 'expiry_time', 'expiry_quantity', 'satisfies_pzi', 'satisfies_pzs', 'database_version', 'tags')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Backup.State]
        READY: _ClassVar[Backup.State]
        CREATING: _ClassVar[Backup.State]
        FAILED: _ClassVar[Backup.State]
        DELETING: _ClassVar[Backup.State]
    STATE_UNSPECIFIED: Backup.State
    READY: Backup.State
    CREATING: Backup.State
    FAILED: Backup.State
    DELETING: Backup.State

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Backup.Type]
        ON_DEMAND: _ClassVar[Backup.Type]
        AUTOMATED: _ClassVar[Backup.Type]
        CONTINUOUS: _ClassVar[Backup.Type]
    TYPE_UNSPECIFIED: Backup.Type
    ON_DEMAND: Backup.Type
    AUTOMATED: Backup.Type
    CONTINUOUS: Backup.Type

    class QuantityBasedExpiry(_message.Message):
        __slots__ = ('retention_count', 'total_retention_count')
        RETENTION_COUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_RETENTION_COUNT_FIELD_NUMBER: _ClassVar[int]
        retention_count: int
        total_retention_count: int

        def __init__(self, retention_count: _Optional[int]=..., total_retention_count: _Optional[int]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class TagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    create_completion_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Backup.State
    type: Backup.Type
    description: str
    cluster_uid: str
    cluster_name: str
    reconciling: bool
    encryption_config: EncryptionConfig
    encryption_info: EncryptionInfo
    etag: str
    annotations: _containers.ScalarMap[str, str]
    size_bytes: int
    expiry_time: _timestamp_pb2.Timestamp
    expiry_quantity: Backup.QuantityBasedExpiry
    satisfies_pzi: bool
    satisfies_pzs: bool
    database_version: DatabaseVersion
    tags: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Backup.State, str]]=..., type: _Optional[_Union[Backup.Type, str]]=..., description: _Optional[str]=..., cluster_uid: _Optional[str]=..., cluster_name: _Optional[str]=..., reconciling: bool=..., encryption_config: _Optional[_Union[EncryptionConfig, _Mapping]]=..., encryption_info: _Optional[_Union[EncryptionInfo, _Mapping]]=..., etag: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., size_bytes: _Optional[int]=..., expiry_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expiry_quantity: _Optional[_Union[Backup.QuantityBasedExpiry, _Mapping]]=..., satisfies_pzi: bool=..., satisfies_pzs: bool=..., database_version: _Optional[_Union[DatabaseVersion, str]]=..., tags: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class SupportedDatabaseFlag(_message.Message):
    __slots__ = ('string_restrictions', 'integer_restrictions', 'recommended_string_value', 'recommended_integer_value', 'name', 'flag_name', 'value_type', 'accepts_multiple_values', 'supported_db_versions', 'requires_db_restart', 'scope')

    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALUE_TYPE_UNSPECIFIED: _ClassVar[SupportedDatabaseFlag.ValueType]
        STRING: _ClassVar[SupportedDatabaseFlag.ValueType]
        INTEGER: _ClassVar[SupportedDatabaseFlag.ValueType]
        FLOAT: _ClassVar[SupportedDatabaseFlag.ValueType]
        NONE: _ClassVar[SupportedDatabaseFlag.ValueType]
    VALUE_TYPE_UNSPECIFIED: SupportedDatabaseFlag.ValueType
    STRING: SupportedDatabaseFlag.ValueType
    INTEGER: SupportedDatabaseFlag.ValueType
    FLOAT: SupportedDatabaseFlag.ValueType
    NONE: SupportedDatabaseFlag.ValueType

    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCOPE_UNSPECIFIED: _ClassVar[SupportedDatabaseFlag.Scope]
        DATABASE: _ClassVar[SupportedDatabaseFlag.Scope]
        CONNECTION_POOL: _ClassVar[SupportedDatabaseFlag.Scope]
    SCOPE_UNSPECIFIED: SupportedDatabaseFlag.Scope
    DATABASE: SupportedDatabaseFlag.Scope
    CONNECTION_POOL: SupportedDatabaseFlag.Scope

    class StringRestrictions(_message.Message):
        __slots__ = ('allowed_values',)
        ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
        allowed_values: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, allowed_values: _Optional[_Iterable[str]]=...) -> None:
            ...

    class IntegerRestrictions(_message.Message):
        __slots__ = ('min_value', 'max_value')
        MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
        MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
        min_value: _wrappers_pb2.Int64Value
        max_value: _wrappers_pb2.Int64Value

        def __init__(self, min_value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., max_value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
            ...
    STRING_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    INTEGER_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FLAG_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTS_MULTIPLE_VALUES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_DB_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_DB_RESTART_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    string_restrictions: SupportedDatabaseFlag.StringRestrictions
    integer_restrictions: SupportedDatabaseFlag.IntegerRestrictions
    recommended_string_value: str
    recommended_integer_value: _wrappers_pb2.Int64Value
    name: str
    flag_name: str
    value_type: SupportedDatabaseFlag.ValueType
    accepts_multiple_values: bool
    supported_db_versions: _containers.RepeatedScalarFieldContainer[DatabaseVersion]
    requires_db_restart: bool
    scope: SupportedDatabaseFlag.Scope

    def __init__(self, string_restrictions: _Optional[_Union[SupportedDatabaseFlag.StringRestrictions, _Mapping]]=..., integer_restrictions: _Optional[_Union[SupportedDatabaseFlag.IntegerRestrictions, _Mapping]]=..., recommended_string_value: _Optional[str]=..., recommended_integer_value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., name: _Optional[str]=..., flag_name: _Optional[str]=..., value_type: _Optional[_Union[SupportedDatabaseFlag.ValueType, str]]=..., accepts_multiple_values: bool=..., supported_db_versions: _Optional[_Iterable[_Union[DatabaseVersion, str]]]=..., requires_db_restart: bool=..., scope: _Optional[_Union[SupportedDatabaseFlag.Scope, str]]=...) -> None:
        ...

class User(_message.Message):
    __slots__ = ('name', 'password', 'database_roles', 'user_type', 'keep_extra_roles')

    class UserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER_TYPE_UNSPECIFIED: _ClassVar[User.UserType]
        ALLOYDB_BUILT_IN: _ClassVar[User.UserType]
        ALLOYDB_IAM_USER: _ClassVar[User.UserType]
    USER_TYPE_UNSPECIFIED: User.UserType
    ALLOYDB_BUILT_IN: User.UserType
    ALLOYDB_IAM_USER: User.UserType
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ROLES_FIELD_NUMBER: _ClassVar[int]
    USER_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEEP_EXTRA_ROLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    password: str
    database_roles: _containers.RepeatedScalarFieldContainer[str]
    user_type: User.UserType
    keep_extra_roles: bool

    def __init__(self, name: _Optional[str]=..., password: _Optional[str]=..., database_roles: _Optional[_Iterable[str]]=..., user_type: _Optional[_Union[User.UserType, str]]=..., keep_extra_roles: bool=...) -> None:
        ...

class Database(_message.Message):
    __slots__ = ('name', 'charset', 'collation', 'character_type', 'is_template', 'database_template', 'is_template_database')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHARSET_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    IS_TEMPLATE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    name: str
    charset: str
    collation: str
    character_type: str
    is_template: bool
    database_template: str
    is_template_database: bool

    def __init__(self, name: _Optional[str]=..., charset: _Optional[str]=..., collation: _Optional[str]=..., character_type: _Optional[str]=..., is_template: bool=..., database_template: _Optional[str]=..., is_template_database: bool=...) -> None:
        ...