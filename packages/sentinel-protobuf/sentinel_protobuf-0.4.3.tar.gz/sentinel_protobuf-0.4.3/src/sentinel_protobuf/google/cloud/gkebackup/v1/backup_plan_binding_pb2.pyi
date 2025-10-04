from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkebackup.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BackupPlanBinding(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'backup_plan', 'cluster', 'backup_plan_details', 'etag')

    class BackupPlanDetails(_message.Message):
        __slots__ = ('protected_pod_count', 'state', 'last_successful_backup_time', 'next_scheduled_backup_time', 'rpo_risk_level', 'last_successful_backup', 'backup_config_details', 'retention_policy_details')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[BackupPlanBinding.BackupPlanDetails.State]
            CLUSTER_PENDING: _ClassVar[BackupPlanBinding.BackupPlanDetails.State]
            PROVISIONING: _ClassVar[BackupPlanBinding.BackupPlanDetails.State]
            READY: _ClassVar[BackupPlanBinding.BackupPlanDetails.State]
            FAILED: _ClassVar[BackupPlanBinding.BackupPlanDetails.State]
            DEACTIVATED: _ClassVar[BackupPlanBinding.BackupPlanDetails.State]
            DELETING: _ClassVar[BackupPlanBinding.BackupPlanDetails.State]
        STATE_UNSPECIFIED: BackupPlanBinding.BackupPlanDetails.State
        CLUSTER_PENDING: BackupPlanBinding.BackupPlanDetails.State
        PROVISIONING: BackupPlanBinding.BackupPlanDetails.State
        READY: BackupPlanBinding.BackupPlanDetails.State
        FAILED: BackupPlanBinding.BackupPlanDetails.State
        DEACTIVATED: BackupPlanBinding.BackupPlanDetails.State
        DELETING: BackupPlanBinding.BackupPlanDetails.State

        class BackupConfigDetails(_message.Message):
            __slots__ = ('all_namespaces', 'selected_namespaces', 'selected_applications', 'include_volume_data', 'include_secrets', 'encryption_key')
            ALL_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
            SELECTED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
            SELECTED_APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_VOLUME_DATA_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_SECRETS_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
            all_namespaces: bool
            selected_namespaces: _common_pb2.Namespaces
            selected_applications: _common_pb2.NamespacedNames
            include_volume_data: bool
            include_secrets: bool
            encryption_key: _common_pb2.EncryptionKey

            def __init__(self, all_namespaces: bool=..., selected_namespaces: _Optional[_Union[_common_pb2.Namespaces, _Mapping]]=..., selected_applications: _Optional[_Union[_common_pb2.NamespacedNames, _Mapping]]=..., include_volume_data: bool=..., include_secrets: bool=..., encryption_key: _Optional[_Union[_common_pb2.EncryptionKey, _Mapping]]=...) -> None:
                ...

        class RetentionPolicyDetails(_message.Message):
            __slots__ = ('backup_delete_lock_days', 'backup_retain_days')
            BACKUP_DELETE_LOCK_DAYS_FIELD_NUMBER: _ClassVar[int]
            BACKUP_RETAIN_DAYS_FIELD_NUMBER: _ClassVar[int]
            backup_delete_lock_days: int
            backup_retain_days: int

            def __init__(self, backup_delete_lock_days: _Optional[int]=..., backup_retain_days: _Optional[int]=...) -> None:
                ...
        PROTECTED_POD_COUNT_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        LAST_SUCCESSFUL_BACKUP_TIME_FIELD_NUMBER: _ClassVar[int]
        NEXT_SCHEDULED_BACKUP_TIME_FIELD_NUMBER: _ClassVar[int]
        RPO_RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
        LAST_SUCCESSFUL_BACKUP_FIELD_NUMBER: _ClassVar[int]
        BACKUP_CONFIG_DETAILS_FIELD_NUMBER: _ClassVar[int]
        RETENTION_POLICY_DETAILS_FIELD_NUMBER: _ClassVar[int]
        protected_pod_count: int
        state: BackupPlanBinding.BackupPlanDetails.State
        last_successful_backup_time: _timestamp_pb2.Timestamp
        next_scheduled_backup_time: _timestamp_pb2.Timestamp
        rpo_risk_level: int
        last_successful_backup: str
        backup_config_details: BackupPlanBinding.BackupPlanDetails.BackupConfigDetails
        retention_policy_details: BackupPlanBinding.BackupPlanDetails.RetentionPolicyDetails

        def __init__(self, protected_pod_count: _Optional[int]=..., state: _Optional[_Union[BackupPlanBinding.BackupPlanDetails.State, str]]=..., last_successful_backup_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_scheduled_backup_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., rpo_risk_level: _Optional[int]=..., last_successful_backup: _Optional[str]=..., backup_config_details: _Optional[_Union[BackupPlanBinding.BackupPlanDetails.BackupConfigDetails, _Mapping]]=..., retention_policy_details: _Optional[_Union[BackupPlanBinding.BackupPlanDetails.RetentionPolicyDetails, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    backup_plan: str
    cluster: str
    backup_plan_details: BackupPlanBinding.BackupPlanDetails
    etag: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., backup_plan: _Optional[str]=..., cluster: _Optional[str]=..., backup_plan_details: _Optional[_Union[BackupPlanBinding.BackupPlanDetails, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...