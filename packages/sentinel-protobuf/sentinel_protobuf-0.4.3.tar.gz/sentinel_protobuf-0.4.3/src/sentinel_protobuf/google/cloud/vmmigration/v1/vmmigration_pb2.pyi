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
from google.rpc import error_details_pb2 as _error_details_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ComputeEngineDiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED: _ClassVar[ComputeEngineDiskType]
    COMPUTE_ENGINE_DISK_TYPE_STANDARD: _ClassVar[ComputeEngineDiskType]
    COMPUTE_ENGINE_DISK_TYPE_SSD: _ClassVar[ComputeEngineDiskType]
    COMPUTE_ENGINE_DISK_TYPE_BALANCED: _ClassVar[ComputeEngineDiskType]
    COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED: _ClassVar[ComputeEngineDiskType]

class ComputeEngineLicenseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT: _ClassVar[ComputeEngineLicenseType]
    COMPUTE_ENGINE_LICENSE_TYPE_PAYG: _ClassVar[ComputeEngineLicenseType]
    COMPUTE_ENGINE_LICENSE_TYPE_BYOL: _ClassVar[ComputeEngineLicenseType]

class ComputeEngineBootOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPUTE_ENGINE_BOOT_OPTION_UNSPECIFIED: _ClassVar[ComputeEngineBootOption]
    COMPUTE_ENGINE_BOOT_OPTION_EFI: _ClassVar[ComputeEngineBootOption]
    COMPUTE_ENGINE_BOOT_OPTION_BIOS: _ClassVar[ComputeEngineBootOption]

class OsCapability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OS_CAPABILITY_UNSPECIFIED: _ClassVar[OsCapability]
    OS_CAPABILITY_NVME_STORAGE_ACCESS: _ClassVar[OsCapability]
    OS_CAPABILITY_GVNIC_NETWORK_INTERFACE: _ClassVar[OsCapability]
    OS_CAPABILITY_IDPF_NETWORK_INTERFACE: _ClassVar[OsCapability]

class BootConversion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BOOT_CONVERSION_UNSPECIFIED: _ClassVar[BootConversion]
    NONE: _ClassVar[BootConversion]
    BIOS_TO_EFI: _ClassVar[BootConversion]

class UtilizationReportView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UTILIZATION_REPORT_VIEW_UNSPECIFIED: _ClassVar[UtilizationReportView]
    BASIC: _ClassVar[UtilizationReportView]
    FULL: _ClassVar[UtilizationReportView]

class MigratingVmView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MIGRATING_VM_VIEW_UNSPECIFIED: _ClassVar[MigratingVmView]
    MIGRATING_VM_VIEW_BASIC: _ClassVar[MigratingVmView]
    MIGRATING_VM_VIEW_FULL: _ClassVar[MigratingVmView]

class VmArchitecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VM_ARCHITECTURE_UNSPECIFIED: _ClassVar[VmArchitecture]
    VM_ARCHITECTURE_X86_FAMILY: _ClassVar[VmArchitecture]
    VM_ARCHITECTURE_ARM64: _ClassVar[VmArchitecture]

class ComputeEngineNetworkTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPUTE_ENGINE_NETWORK_TIER_UNSPECIFIED: _ClassVar[ComputeEngineNetworkTier]
    NETWORK_TIER_STANDARD: _ClassVar[ComputeEngineNetworkTier]
    NETWORK_TIER_PREMIUM: _ClassVar[ComputeEngineNetworkTier]
COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED: ComputeEngineDiskType
COMPUTE_ENGINE_DISK_TYPE_STANDARD: ComputeEngineDiskType
COMPUTE_ENGINE_DISK_TYPE_SSD: ComputeEngineDiskType
COMPUTE_ENGINE_DISK_TYPE_BALANCED: ComputeEngineDiskType
COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED: ComputeEngineDiskType
COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT: ComputeEngineLicenseType
COMPUTE_ENGINE_LICENSE_TYPE_PAYG: ComputeEngineLicenseType
COMPUTE_ENGINE_LICENSE_TYPE_BYOL: ComputeEngineLicenseType
COMPUTE_ENGINE_BOOT_OPTION_UNSPECIFIED: ComputeEngineBootOption
COMPUTE_ENGINE_BOOT_OPTION_EFI: ComputeEngineBootOption
COMPUTE_ENGINE_BOOT_OPTION_BIOS: ComputeEngineBootOption
OS_CAPABILITY_UNSPECIFIED: OsCapability
OS_CAPABILITY_NVME_STORAGE_ACCESS: OsCapability
OS_CAPABILITY_GVNIC_NETWORK_INTERFACE: OsCapability
OS_CAPABILITY_IDPF_NETWORK_INTERFACE: OsCapability
BOOT_CONVERSION_UNSPECIFIED: BootConversion
NONE: BootConversion
BIOS_TO_EFI: BootConversion
UTILIZATION_REPORT_VIEW_UNSPECIFIED: UtilizationReportView
BASIC: UtilizationReportView
FULL: UtilizationReportView
MIGRATING_VM_VIEW_UNSPECIFIED: MigratingVmView
MIGRATING_VM_VIEW_BASIC: MigratingVmView
MIGRATING_VM_VIEW_FULL: MigratingVmView
VM_ARCHITECTURE_UNSPECIFIED: VmArchitecture
VM_ARCHITECTURE_X86_FAMILY: VmArchitecture
VM_ARCHITECTURE_ARM64: VmArchitecture
COMPUTE_ENGINE_NETWORK_TIER_UNSPECIFIED: ComputeEngineNetworkTier
NETWORK_TIER_STANDARD: ComputeEngineNetworkTier
NETWORK_TIER_PREMIUM: ComputeEngineNetworkTier

class ReplicationCycle(_message.Message):
    __slots__ = ('name', 'cycle_number', 'start_time', 'end_time', 'total_pause_duration', 'progress_percent', 'steps', 'state', 'error', 'warnings')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ReplicationCycle.State]
        RUNNING: _ClassVar[ReplicationCycle.State]
        PAUSED: _ClassVar[ReplicationCycle.State]
        FAILED: _ClassVar[ReplicationCycle.State]
        SUCCEEDED: _ClassVar[ReplicationCycle.State]
    STATE_UNSPECIFIED: ReplicationCycle.State
    RUNNING: ReplicationCycle.State
    PAUSED: ReplicationCycle.State
    FAILED: ReplicationCycle.State
    SUCCEEDED: ReplicationCycle.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CYCLE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAUSE_DURATION_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    cycle_number: int
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    total_pause_duration: _duration_pb2.Duration
    progress_percent: int
    steps: _containers.RepeatedCompositeFieldContainer[CycleStep]
    state: ReplicationCycle.State
    error: _status_pb2.Status
    warnings: _containers.RepeatedCompositeFieldContainer[MigrationWarning]

    def __init__(self, name: _Optional[str]=..., cycle_number: _Optional[int]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., total_pause_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., progress_percent: _Optional[int]=..., steps: _Optional[_Iterable[_Union[CycleStep, _Mapping]]]=..., state: _Optional[_Union[ReplicationCycle.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., warnings: _Optional[_Iterable[_Union[MigrationWarning, _Mapping]]]=...) -> None:
        ...

class CycleStep(_message.Message):
    __slots__ = ('initializing_replication', 'replicating', 'post_processing', 'start_time', 'end_time')
    INITIALIZING_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    REPLICATING_FIELD_NUMBER: _ClassVar[int]
    POST_PROCESSING_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    initializing_replication: InitializingReplicationStep
    replicating: ReplicatingStep
    post_processing: PostProcessingStep
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, initializing_replication: _Optional[_Union[InitializingReplicationStep, _Mapping]]=..., replicating: _Optional[_Union[ReplicatingStep, _Mapping]]=..., post_processing: _Optional[_Union[PostProcessingStep, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class InitializingReplicationStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReplicatingStep(_message.Message):
    __slots__ = ('total_bytes', 'replicated_bytes', 'last_two_minutes_average_bytes_per_second', 'last_thirty_minutes_average_bytes_per_second')
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    REPLICATED_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_TWO_MINUTES_AVERAGE_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    LAST_THIRTY_MINUTES_AVERAGE_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    total_bytes: int
    replicated_bytes: int
    last_two_minutes_average_bytes_per_second: int
    last_thirty_minutes_average_bytes_per_second: int

    def __init__(self, total_bytes: _Optional[int]=..., replicated_bytes: _Optional[int]=..., last_two_minutes_average_bytes_per_second: _Optional[int]=..., last_thirty_minutes_average_bytes_per_second: _Optional[int]=...) -> None:
        ...

class PostProcessingStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReplicationSync(_message.Message):
    __slots__ = ('last_sync_time',)
    LAST_SYNC_TIME_FIELD_NUMBER: _ClassVar[int]
    last_sync_time: _timestamp_pb2.Timestamp

    def __init__(self, last_sync_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class MigratingVm(_message.Message):
    __slots__ = ('compute_engine_target_defaults', 'compute_engine_disks_target_defaults', 'vmware_source_vm_details', 'aws_source_vm_details', 'azure_source_vm_details', 'name', 'source_vm_id', 'display_name', 'description', 'policy', 'create_time', 'update_time', 'last_sync', 'state', 'state_time', 'current_sync_info', 'last_replication_cycle', 'group', 'labels', 'recent_clone_jobs', 'error', 'recent_cutover_jobs', 'cutover_forecast', 'expiration')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MigratingVm.State]
        PENDING: _ClassVar[MigratingVm.State]
        READY: _ClassVar[MigratingVm.State]
        FIRST_SYNC: _ClassVar[MigratingVm.State]
        ACTIVE: _ClassVar[MigratingVm.State]
        CUTTING_OVER: _ClassVar[MigratingVm.State]
        CUTOVER: _ClassVar[MigratingVm.State]
        FINAL_SYNC: _ClassVar[MigratingVm.State]
        PAUSED: _ClassVar[MigratingVm.State]
        FINALIZING: _ClassVar[MigratingVm.State]
        FINALIZED: _ClassVar[MigratingVm.State]
        ERROR: _ClassVar[MigratingVm.State]
        EXPIRED: _ClassVar[MigratingVm.State]
        FINALIZED_EXPIRED: _ClassVar[MigratingVm.State]
    STATE_UNSPECIFIED: MigratingVm.State
    PENDING: MigratingVm.State
    READY: MigratingVm.State
    FIRST_SYNC: MigratingVm.State
    ACTIVE: MigratingVm.State
    CUTTING_OVER: MigratingVm.State
    CUTOVER: MigratingVm.State
    FINAL_SYNC: MigratingVm.State
    PAUSED: MigratingVm.State
    FINALIZING: MigratingVm.State
    FINALIZED: MigratingVm.State
    ERROR: MigratingVm.State
    EXPIRED: MigratingVm.State
    FINALIZED_EXPIRED: MigratingVm.State

    class Expiration(_message.Message):
        __slots__ = ('expire_time', 'extension_count', 'extendable')
        EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
        EXTENSION_COUNT_FIELD_NUMBER: _ClassVar[int]
        EXTENDABLE_FIELD_NUMBER: _ClassVar[int]
        expire_time: _timestamp_pb2.Timestamp
        extension_count: int
        extendable: bool

        def __init__(self, expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., extension_count: _Optional[int]=..., extendable: bool=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    COMPUTE_ENGINE_TARGET_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ENGINE_DISKS_TARGET_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_SOURCE_VM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    AWS_SOURCE_VM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    AZURE_SOURCE_VM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VM_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SYNC_INFO_FIELD_NUMBER: _ClassVar[int]
    LAST_REPLICATION_CYCLE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RECENT_CLONE_JOBS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RECENT_CUTOVER_JOBS_FIELD_NUMBER: _ClassVar[int]
    CUTOVER_FORECAST_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    compute_engine_target_defaults: ComputeEngineTargetDefaults
    compute_engine_disks_target_defaults: ComputeEngineDisksTargetDefaults
    vmware_source_vm_details: VmwareSourceVmDetails
    aws_source_vm_details: AwsSourceVmDetails
    azure_source_vm_details: AzureSourceVmDetails
    name: str
    source_vm_id: str
    display_name: str
    description: str
    policy: SchedulePolicy
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    last_sync: ReplicationSync
    state: MigratingVm.State
    state_time: _timestamp_pb2.Timestamp
    current_sync_info: ReplicationCycle
    last_replication_cycle: ReplicationCycle
    group: str
    labels: _containers.ScalarMap[str, str]
    recent_clone_jobs: _containers.RepeatedCompositeFieldContainer[CloneJob]
    error: _status_pb2.Status
    recent_cutover_jobs: _containers.RepeatedCompositeFieldContainer[CutoverJob]
    cutover_forecast: CutoverForecast
    expiration: MigratingVm.Expiration

    def __init__(self, compute_engine_target_defaults: _Optional[_Union[ComputeEngineTargetDefaults, _Mapping]]=..., compute_engine_disks_target_defaults: _Optional[_Union[ComputeEngineDisksTargetDefaults, _Mapping]]=..., vmware_source_vm_details: _Optional[_Union[VmwareSourceVmDetails, _Mapping]]=..., aws_source_vm_details: _Optional[_Union[AwsSourceVmDetails, _Mapping]]=..., azure_source_vm_details: _Optional[_Union[AzureSourceVmDetails, _Mapping]]=..., name: _Optional[str]=..., source_vm_id: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., policy: _Optional[_Union[SchedulePolicy, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_sync: _Optional[_Union[ReplicationSync, _Mapping]]=..., state: _Optional[_Union[MigratingVm.State, str]]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., current_sync_info: _Optional[_Union[ReplicationCycle, _Mapping]]=..., last_replication_cycle: _Optional[_Union[ReplicationCycle, _Mapping]]=..., group: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., recent_clone_jobs: _Optional[_Iterable[_Union[CloneJob, _Mapping]]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., recent_cutover_jobs: _Optional[_Iterable[_Union[CutoverJob, _Mapping]]]=..., cutover_forecast: _Optional[_Union[CutoverForecast, _Mapping]]=..., expiration: _Optional[_Union[MigratingVm.Expiration, _Mapping]]=...) -> None:
        ...

class CutoverForecast(_message.Message):
    __slots__ = ('estimated_cutover_job_duration',)
    ESTIMATED_CUTOVER_JOB_DURATION_FIELD_NUMBER: _ClassVar[int]
    estimated_cutover_job_duration: _duration_pb2.Duration

    def __init__(self, estimated_cutover_job_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class CloneJob(_message.Message):
    __slots__ = ('compute_engine_target_details', 'compute_engine_disks_target_details', 'create_time', 'end_time', 'name', 'state', 'state_time', 'error', 'steps')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CloneJob.State]
        PENDING: _ClassVar[CloneJob.State]
        ACTIVE: _ClassVar[CloneJob.State]
        FAILED: _ClassVar[CloneJob.State]
        SUCCEEDED: _ClassVar[CloneJob.State]
        CANCELLED: _ClassVar[CloneJob.State]
        CANCELLING: _ClassVar[CloneJob.State]
        ADAPTING_OS: _ClassVar[CloneJob.State]
    STATE_UNSPECIFIED: CloneJob.State
    PENDING: CloneJob.State
    ACTIVE: CloneJob.State
    FAILED: CloneJob.State
    SUCCEEDED: CloneJob.State
    CANCELLED: CloneJob.State
    CANCELLING: CloneJob.State
    ADAPTING_OS: CloneJob.State
    COMPUTE_ENGINE_TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ENGINE_DISKS_TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    compute_engine_target_details: ComputeEngineTargetDetails
    compute_engine_disks_target_details: ComputeEngineDisksTargetDetails
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    name: str
    state: CloneJob.State
    state_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    steps: _containers.RepeatedCompositeFieldContainer[CloneStep]

    def __init__(self, compute_engine_target_details: _Optional[_Union[ComputeEngineTargetDetails, _Mapping]]=..., compute_engine_disks_target_details: _Optional[_Union[ComputeEngineDisksTargetDetails, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., name: _Optional[str]=..., state: _Optional[_Union[CloneJob.State, str]]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., steps: _Optional[_Iterable[_Union[CloneStep, _Mapping]]]=...) -> None:
        ...

class CloneStep(_message.Message):
    __slots__ = ('adapting_os', 'preparing_vm_disks', 'instantiating_migrated_vm', 'start_time', 'end_time')
    ADAPTING_OS_FIELD_NUMBER: _ClassVar[int]
    PREPARING_VM_DISKS_FIELD_NUMBER: _ClassVar[int]
    INSTANTIATING_MIGRATED_VM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    adapting_os: AdaptingOSStep
    preparing_vm_disks: PreparingVMDisksStep
    instantiating_migrated_vm: InstantiatingMigratedVMStep
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, adapting_os: _Optional[_Union[AdaptingOSStep, _Mapping]]=..., preparing_vm_disks: _Optional[_Union[PreparingVMDisksStep, _Mapping]]=..., instantiating_migrated_vm: _Optional[_Union[InstantiatingMigratedVMStep, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AdaptingOSStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PreparingVMDisksStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class InstantiatingMigratedVMStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CutoverJob(_message.Message):
    __slots__ = ('compute_engine_target_details', 'compute_engine_disks_target_details', 'create_time', 'end_time', 'name', 'state', 'state_time', 'progress_percent', 'error', 'state_message', 'steps')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CutoverJob.State]
        PENDING: _ClassVar[CutoverJob.State]
        FAILED: _ClassVar[CutoverJob.State]
        SUCCEEDED: _ClassVar[CutoverJob.State]
        CANCELLED: _ClassVar[CutoverJob.State]
        CANCELLING: _ClassVar[CutoverJob.State]
        ACTIVE: _ClassVar[CutoverJob.State]
        ADAPTING_OS: _ClassVar[CutoverJob.State]
    STATE_UNSPECIFIED: CutoverJob.State
    PENDING: CutoverJob.State
    FAILED: CutoverJob.State
    SUCCEEDED: CutoverJob.State
    CANCELLED: CutoverJob.State
    CANCELLING: CutoverJob.State
    ACTIVE: CutoverJob.State
    ADAPTING_OS: CutoverJob.State
    COMPUTE_ENGINE_TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ENGINE_DISKS_TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    compute_engine_target_details: ComputeEngineTargetDetails
    compute_engine_disks_target_details: ComputeEngineDisksTargetDetails
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    name: str
    state: CutoverJob.State
    state_time: _timestamp_pb2.Timestamp
    progress_percent: int
    error: _status_pb2.Status
    state_message: str
    steps: _containers.RepeatedCompositeFieldContainer[CutoverStep]

    def __init__(self, compute_engine_target_details: _Optional[_Union[ComputeEngineTargetDetails, _Mapping]]=..., compute_engine_disks_target_details: _Optional[_Union[ComputeEngineDisksTargetDetails, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., name: _Optional[str]=..., state: _Optional[_Union[CutoverJob.State, str]]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., progress_percent: _Optional[int]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., state_message: _Optional[str]=..., steps: _Optional[_Iterable[_Union[CutoverStep, _Mapping]]]=...) -> None:
        ...

class CutoverStep(_message.Message):
    __slots__ = ('previous_replication_cycle', 'shutting_down_source_vm', 'final_sync', 'preparing_vm_disks', 'instantiating_migrated_vm', 'start_time', 'end_time')
    PREVIOUS_REPLICATION_CYCLE_FIELD_NUMBER: _ClassVar[int]
    SHUTTING_DOWN_SOURCE_VM_FIELD_NUMBER: _ClassVar[int]
    FINAL_SYNC_FIELD_NUMBER: _ClassVar[int]
    PREPARING_VM_DISKS_FIELD_NUMBER: _ClassVar[int]
    INSTANTIATING_MIGRATED_VM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    previous_replication_cycle: ReplicationCycle
    shutting_down_source_vm: ShuttingDownSourceVMStep
    final_sync: ReplicationCycle
    preparing_vm_disks: PreparingVMDisksStep
    instantiating_migrated_vm: InstantiatingMigratedVMStep
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, previous_replication_cycle: _Optional[_Union[ReplicationCycle, _Mapping]]=..., shutting_down_source_vm: _Optional[_Union[ShuttingDownSourceVMStep, _Mapping]]=..., final_sync: _Optional[_Union[ReplicationCycle, _Mapping]]=..., preparing_vm_disks: _Optional[_Union[PreparingVMDisksStep, _Mapping]]=..., instantiating_migrated_vm: _Optional[_Union[InstantiatingMigratedVMStep, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ShuttingDownSourceVMStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateCloneJobRequest(_message.Message):
    __slots__ = ('parent', 'clone_job_id', 'clone_job', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLONE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CLONE_JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    clone_job_id: str
    clone_job: CloneJob
    request_id: str

    def __init__(self, parent: _Optional[str]=..., clone_job_id: _Optional[str]=..., clone_job: _Optional[_Union[CloneJob, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class CancelCloneJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelCloneJobResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListCloneJobsRequest(_message.Message):
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

class ListCloneJobsResponse(_message.Message):
    __slots__ = ('clone_jobs', 'next_page_token', 'unreachable')
    CLONE_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    clone_jobs: _containers.RepeatedCompositeFieldContainer[CloneJob]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, clone_jobs: _Optional[_Iterable[_Union[CloneJob, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCloneJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Source(_message.Message):
    __slots__ = ('vmware', 'aws', 'azure', 'name', 'create_time', 'update_time', 'labels', 'description', 'encryption')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VMWARE_FIELD_NUMBER: _ClassVar[int]
    AWS_FIELD_NUMBER: _ClassVar[int]
    AZURE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    vmware: VmwareSourceDetails
    aws: AwsSourceDetails
    azure: AzureSourceDetails
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    encryption: Encryption

    def __init__(self, vmware: _Optional[_Union[VmwareSourceDetails, _Mapping]]=..., aws: _Optional[_Union[AwsSourceDetails, _Mapping]]=..., azure: _Optional[_Union[AzureSourceDetails, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., encryption: _Optional[_Union[Encryption, _Mapping]]=...) -> None:
        ...

class Encryption(_message.Message):
    __slots__ = ('kms_key',)
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    kms_key: str

    def __init__(self, kms_key: _Optional[str]=...) -> None:
        ...

class VmwareSourceDetails(_message.Message):
    __slots__ = ('username', 'password', 'vcenter_ip', 'thumbprint', 'resolved_vcenter_host')
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    VCENTER_IP_FIELD_NUMBER: _ClassVar[int]
    THUMBPRINT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_VCENTER_HOST_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    vcenter_ip: str
    thumbprint: str
    resolved_vcenter_host: str

    def __init__(self, username: _Optional[str]=..., password: _Optional[str]=..., vcenter_ip: _Optional[str]=..., thumbprint: _Optional[str]=..., resolved_vcenter_host: _Optional[str]=...) -> None:
        ...

class AwsSourceDetails(_message.Message):
    __slots__ = ('access_key_creds', 'aws_region', 'state', 'error', 'inventory_tag_list', 'inventory_security_group_names', 'migration_resources_user_tags', 'public_ip')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AwsSourceDetails.State]
        PENDING: _ClassVar[AwsSourceDetails.State]
        FAILED: _ClassVar[AwsSourceDetails.State]
        ACTIVE: _ClassVar[AwsSourceDetails.State]
    STATE_UNSPECIFIED: AwsSourceDetails.State
    PENDING: AwsSourceDetails.State
    FAILED: AwsSourceDetails.State
    ACTIVE: AwsSourceDetails.State

    class AccessKeyCredentials(_message.Message):
        __slots__ = ('access_key_id', 'secret_access_key', 'session_token')
        ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        access_key_id: str
        secret_access_key: str
        session_token: str

        def __init__(self, access_key_id: _Optional[str]=..., secret_access_key: _Optional[str]=..., session_token: _Optional[str]=...) -> None:
            ...

    class Tag(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class MigrationResourcesUserTagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ACCESS_KEY_CREDS_FIELD_NUMBER: _ClassVar[int]
    AWS_REGION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_TAG_LIST_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_SECURITY_GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_RESOURCES_USER_TAGS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    access_key_creds: AwsSourceDetails.AccessKeyCredentials
    aws_region: str
    state: AwsSourceDetails.State
    error: _status_pb2.Status
    inventory_tag_list: _containers.RepeatedCompositeFieldContainer[AwsSourceDetails.Tag]
    inventory_security_group_names: _containers.RepeatedScalarFieldContainer[str]
    migration_resources_user_tags: _containers.ScalarMap[str, str]
    public_ip: str

    def __init__(self, access_key_creds: _Optional[_Union[AwsSourceDetails.AccessKeyCredentials, _Mapping]]=..., aws_region: _Optional[str]=..., state: _Optional[_Union[AwsSourceDetails.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., inventory_tag_list: _Optional[_Iterable[_Union[AwsSourceDetails.Tag, _Mapping]]]=..., inventory_security_group_names: _Optional[_Iterable[str]]=..., migration_resources_user_tags: _Optional[_Mapping[str, str]]=..., public_ip: _Optional[str]=...) -> None:
        ...

class AzureSourceDetails(_message.Message):
    __slots__ = ('client_secret_creds', 'subscription_id', 'azure_location', 'state', 'error', 'migration_resources_user_tags', 'resource_group_id')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AzureSourceDetails.State]
        PENDING: _ClassVar[AzureSourceDetails.State]
        FAILED: _ClassVar[AzureSourceDetails.State]
        ACTIVE: _ClassVar[AzureSourceDetails.State]
    STATE_UNSPECIFIED: AzureSourceDetails.State
    PENDING: AzureSourceDetails.State
    FAILED: AzureSourceDetails.State
    ACTIVE: AzureSourceDetails.State

    class ClientSecretCredentials(_message.Message):
        __slots__ = ('tenant_id', 'client_id', 'client_secret')
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        client_id: str
        client_secret: str

        def __init__(self, tenant_id: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=...) -> None:
            ...

    class MigrationResourcesUserTagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CLIENT_SECRET_CREDS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    AZURE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_RESOURCES_USER_TAGS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    client_secret_creds: AzureSourceDetails.ClientSecretCredentials
    subscription_id: str
    azure_location: str
    state: AzureSourceDetails.State
    error: _status_pb2.Status
    migration_resources_user_tags: _containers.ScalarMap[str, str]
    resource_group_id: str

    def __init__(self, client_secret_creds: _Optional[_Union[AzureSourceDetails.ClientSecretCredentials, _Mapping]]=..., subscription_id: _Optional[str]=..., azure_location: _Optional[str]=..., state: _Optional[_Union[AzureSourceDetails.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., migration_resources_user_tags: _Optional[_Mapping[str, str]]=..., resource_group_id: _Optional[str]=...) -> None:
        ...

class DatacenterConnector(_message.Message):
    __slots__ = ('create_time', 'update_time', 'name', 'registration_id', 'service_account', 'version', 'bucket', 'state', 'state_time', 'error', 'appliance_infrastructure_version', 'appliance_software_version', 'available_versions', 'upgrade_status')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DatacenterConnector.State]
        PENDING: _ClassVar[DatacenterConnector.State]
        OFFLINE: _ClassVar[DatacenterConnector.State]
        FAILED: _ClassVar[DatacenterConnector.State]
        ACTIVE: _ClassVar[DatacenterConnector.State]
    STATE_UNSPECIFIED: DatacenterConnector.State
    PENDING: DatacenterConnector.State
    OFFLINE: DatacenterConnector.State
    FAILED: DatacenterConnector.State
    ACTIVE: DatacenterConnector.State
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_INFRASTRUCTURE_VERSION_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_STATUS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    name: str
    registration_id: str
    service_account: str
    version: str
    bucket: str
    state: DatacenterConnector.State
    state_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    appliance_infrastructure_version: str
    appliance_software_version: str
    available_versions: AvailableUpdates
    upgrade_status: UpgradeStatus

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., name: _Optional[str]=..., registration_id: _Optional[str]=..., service_account: _Optional[str]=..., version: _Optional[str]=..., bucket: _Optional[str]=..., state: _Optional[_Union[DatacenterConnector.State, str]]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., appliance_infrastructure_version: _Optional[str]=..., appliance_software_version: _Optional[str]=..., available_versions: _Optional[_Union[AvailableUpdates, _Mapping]]=..., upgrade_status: _Optional[_Union[UpgradeStatus, _Mapping]]=...) -> None:
        ...

class UpgradeStatus(_message.Message):
    __slots__ = ('version', 'state', 'error', 'start_time', 'previous_version')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[UpgradeStatus.State]
        RUNNING: _ClassVar[UpgradeStatus.State]
        FAILED: _ClassVar[UpgradeStatus.State]
        SUCCEEDED: _ClassVar[UpgradeStatus.State]
    STATE_UNSPECIFIED: UpgradeStatus.State
    RUNNING: UpgradeStatus.State
    FAILED: UpgradeStatus.State
    SUCCEEDED: UpgradeStatus.State
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    state: UpgradeStatus.State
    error: _status_pb2.Status
    start_time: _timestamp_pb2.Timestamp
    previous_version: str

    def __init__(self, version: _Optional[str]=..., state: _Optional[_Union[UpgradeStatus.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., previous_version: _Optional[str]=...) -> None:
        ...

class AvailableUpdates(_message.Message):
    __slots__ = ('new_deployable_appliance', 'in_place_update')
    NEW_DEPLOYABLE_APPLIANCE_FIELD_NUMBER: _ClassVar[int]
    IN_PLACE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    new_deployable_appliance: ApplianceVersion
    in_place_update: ApplianceVersion

    def __init__(self, new_deployable_appliance: _Optional[_Union[ApplianceVersion, _Mapping]]=..., in_place_update: _Optional[_Union[ApplianceVersion, _Mapping]]=...) -> None:
        ...

class ApplianceVersion(_message.Message):
    __slots__ = ('version', 'uri', 'critical', 'release_notes_uri')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NOTES_URI_FIELD_NUMBER: _ClassVar[int]
    version: str
    uri: str
    critical: bool
    release_notes_uri: str

    def __init__(self, version: _Optional[str]=..., uri: _Optional[str]=..., critical: bool=..., release_notes_uri: _Optional[str]=...) -> None:
        ...

class ListSourcesRequest(_message.Message):
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

class ListSourcesResponse(_message.Message):
    __slots__ = ('sources', 'next_page_token', 'unreachable')
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[Source]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, sources: _Optional[_Iterable[_Union[Source, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetSourceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSourceRequest(_message.Message):
    __slots__ = ('parent', 'source_id', 'source', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source_id: str
    source: Source
    request_id: str

    def __init__(self, parent: _Optional[str]=..., source_id: _Optional[str]=..., source: _Optional[_Union[Source, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateSourceRequest(_message.Message):
    __slots__ = ('update_mask', 'source', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    source: Source
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., source: _Optional[_Union[Source, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteSourceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class FetchInventoryRequest(_message.Message):
    __slots__ = ('source', 'force_refresh')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FORCE_REFRESH_FIELD_NUMBER: _ClassVar[int]
    source: str
    force_refresh: bool

    def __init__(self, source: _Optional[str]=..., force_refresh: bool=...) -> None:
        ...

class VmwareVmDetails(_message.Message):
    __slots__ = ('vm_id', 'datacenter_id', 'datacenter_description', 'uuid', 'display_name', 'power_state', 'cpu_count', 'memory_mb', 'disk_count', 'committed_storage_mb', 'guest_description', 'boot_option', 'architecture')

    class PowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POWER_STATE_UNSPECIFIED: _ClassVar[VmwareVmDetails.PowerState]
        ON: _ClassVar[VmwareVmDetails.PowerState]
        OFF: _ClassVar[VmwareVmDetails.PowerState]
        SUSPENDED: _ClassVar[VmwareVmDetails.PowerState]
    POWER_STATE_UNSPECIFIED: VmwareVmDetails.PowerState
    ON: VmwareVmDetails.PowerState
    OFF: VmwareVmDetails.PowerState
    SUSPENDED: VmwareVmDetails.PowerState

    class BootOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BOOT_OPTION_UNSPECIFIED: _ClassVar[VmwareVmDetails.BootOption]
        EFI: _ClassVar[VmwareVmDetails.BootOption]
        BIOS: _ClassVar[VmwareVmDetails.BootOption]
    BOOT_OPTION_UNSPECIFIED: VmwareVmDetails.BootOption
    EFI: VmwareVmDetails.BootOption
    BIOS: VmwareVmDetails.BootOption

    class VmArchitecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VM_ARCHITECTURE_UNSPECIFIED: _ClassVar[VmwareVmDetails.VmArchitecture]
        VM_ARCHITECTURE_X86_FAMILY: _ClassVar[VmwareVmDetails.VmArchitecture]
        VM_ARCHITECTURE_ARM64: _ClassVar[VmwareVmDetails.VmArchitecture]
    VM_ARCHITECTURE_UNSPECIFIED: VmwareVmDetails.VmArchitecture
    VM_ARCHITECTURE_X86_FAMILY: VmwareVmDetails.VmArchitecture
    VM_ARCHITECTURE_ARM64: VmwareVmDetails.VmArchitecture
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_ID_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    DISK_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_STORAGE_MB_FIELD_NUMBER: _ClassVar[int]
    GUEST_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BOOT_OPTION_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    datacenter_id: str
    datacenter_description: str
    uuid: str
    display_name: str
    power_state: VmwareVmDetails.PowerState
    cpu_count: int
    memory_mb: int
    disk_count: int
    committed_storage_mb: int
    guest_description: str
    boot_option: VmwareVmDetails.BootOption
    architecture: VmwareVmDetails.VmArchitecture

    def __init__(self, vm_id: _Optional[str]=..., datacenter_id: _Optional[str]=..., datacenter_description: _Optional[str]=..., uuid: _Optional[str]=..., display_name: _Optional[str]=..., power_state: _Optional[_Union[VmwareVmDetails.PowerState, str]]=..., cpu_count: _Optional[int]=..., memory_mb: _Optional[int]=..., disk_count: _Optional[int]=..., committed_storage_mb: _Optional[int]=..., guest_description: _Optional[str]=..., boot_option: _Optional[_Union[VmwareVmDetails.BootOption, str]]=..., architecture: _Optional[_Union[VmwareVmDetails.VmArchitecture, str]]=...) -> None:
        ...

class AwsVmDetails(_message.Message):
    __slots__ = ('vm_id', 'display_name', 'source_id', 'source_description', 'power_state', 'cpu_count', 'memory_mb', 'disk_count', 'committed_storage_mb', 'os_description', 'boot_option', 'instance_type', 'vpc_id', 'security_groups', 'tags', 'zone', 'virtualization_type', 'architecture', 'vcpu_count')

    class PowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POWER_STATE_UNSPECIFIED: _ClassVar[AwsVmDetails.PowerState]
        ON: _ClassVar[AwsVmDetails.PowerState]
        OFF: _ClassVar[AwsVmDetails.PowerState]
        SUSPENDED: _ClassVar[AwsVmDetails.PowerState]
        PENDING: _ClassVar[AwsVmDetails.PowerState]
    POWER_STATE_UNSPECIFIED: AwsVmDetails.PowerState
    ON: AwsVmDetails.PowerState
    OFF: AwsVmDetails.PowerState
    SUSPENDED: AwsVmDetails.PowerState
    PENDING: AwsVmDetails.PowerState

    class BootOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BOOT_OPTION_UNSPECIFIED: _ClassVar[AwsVmDetails.BootOption]
        EFI: _ClassVar[AwsVmDetails.BootOption]
        BIOS: _ClassVar[AwsVmDetails.BootOption]
    BOOT_OPTION_UNSPECIFIED: AwsVmDetails.BootOption
    EFI: AwsVmDetails.BootOption
    BIOS: AwsVmDetails.BootOption

    class VmVirtualizationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VM_VIRTUALIZATION_TYPE_UNSPECIFIED: _ClassVar[AwsVmDetails.VmVirtualizationType]
        HVM: _ClassVar[AwsVmDetails.VmVirtualizationType]
        PARAVIRTUAL: _ClassVar[AwsVmDetails.VmVirtualizationType]
    VM_VIRTUALIZATION_TYPE_UNSPECIFIED: AwsVmDetails.VmVirtualizationType
    HVM: AwsVmDetails.VmVirtualizationType
    PARAVIRTUAL: AwsVmDetails.VmVirtualizationType

    class VmArchitecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VM_ARCHITECTURE_UNSPECIFIED: _ClassVar[AwsVmDetails.VmArchitecture]
        I386: _ClassVar[AwsVmDetails.VmArchitecture]
        X86_64: _ClassVar[AwsVmDetails.VmArchitecture]
        ARM64: _ClassVar[AwsVmDetails.VmArchitecture]
        X86_64_MAC: _ClassVar[AwsVmDetails.VmArchitecture]
    VM_ARCHITECTURE_UNSPECIFIED: AwsVmDetails.VmArchitecture
    I386: AwsVmDetails.VmArchitecture
    X86_64: AwsVmDetails.VmArchitecture
    ARM64: AwsVmDetails.VmArchitecture
    X86_64_MAC: AwsVmDetails.VmArchitecture

    class TagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    DISK_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_STORAGE_MB_FIELD_NUMBER: _ClassVar[int]
    OS_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BOOT_OPTION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    VIRTUALIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    VCPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    display_name: str
    source_id: str
    source_description: str
    power_state: AwsVmDetails.PowerState
    cpu_count: int
    memory_mb: int
    disk_count: int
    committed_storage_mb: int
    os_description: str
    boot_option: AwsVmDetails.BootOption
    instance_type: str
    vpc_id: str
    security_groups: _containers.RepeatedCompositeFieldContainer[AwsSecurityGroup]
    tags: _containers.ScalarMap[str, str]
    zone: str
    virtualization_type: AwsVmDetails.VmVirtualizationType
    architecture: AwsVmDetails.VmArchitecture
    vcpu_count: int

    def __init__(self, vm_id: _Optional[str]=..., display_name: _Optional[str]=..., source_id: _Optional[str]=..., source_description: _Optional[str]=..., power_state: _Optional[_Union[AwsVmDetails.PowerState, str]]=..., cpu_count: _Optional[int]=..., memory_mb: _Optional[int]=..., disk_count: _Optional[int]=..., committed_storage_mb: _Optional[int]=..., os_description: _Optional[str]=..., boot_option: _Optional[_Union[AwsVmDetails.BootOption, str]]=..., instance_type: _Optional[str]=..., vpc_id: _Optional[str]=..., security_groups: _Optional[_Iterable[_Union[AwsSecurityGroup, _Mapping]]]=..., tags: _Optional[_Mapping[str, str]]=..., zone: _Optional[str]=..., virtualization_type: _Optional[_Union[AwsVmDetails.VmVirtualizationType, str]]=..., architecture: _Optional[_Union[AwsVmDetails.VmArchitecture, str]]=..., vcpu_count: _Optional[int]=...) -> None:
        ...

class AwsSecurityGroup(_message.Message):
    __slots__ = ('id', 'name')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class AzureVmDetails(_message.Message):
    __slots__ = ('vm_id', 'power_state', 'vm_size', 'cpu_count', 'memory_mb', 'disk_count', 'committed_storage_mb', 'os_disk', 'disks', 'os_description', 'boot_option', 'tags', 'computer_name', 'architecture')

    class PowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POWER_STATE_UNSPECIFIED: _ClassVar[AzureVmDetails.PowerState]
        STARTING: _ClassVar[AzureVmDetails.PowerState]
        RUNNING: _ClassVar[AzureVmDetails.PowerState]
        STOPPING: _ClassVar[AzureVmDetails.PowerState]
        STOPPED: _ClassVar[AzureVmDetails.PowerState]
        DEALLOCATING: _ClassVar[AzureVmDetails.PowerState]
        DEALLOCATED: _ClassVar[AzureVmDetails.PowerState]
        UNKNOWN: _ClassVar[AzureVmDetails.PowerState]
    POWER_STATE_UNSPECIFIED: AzureVmDetails.PowerState
    STARTING: AzureVmDetails.PowerState
    RUNNING: AzureVmDetails.PowerState
    STOPPING: AzureVmDetails.PowerState
    STOPPED: AzureVmDetails.PowerState
    DEALLOCATING: AzureVmDetails.PowerState
    DEALLOCATED: AzureVmDetails.PowerState
    UNKNOWN: AzureVmDetails.PowerState

    class BootOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BOOT_OPTION_UNSPECIFIED: _ClassVar[AzureVmDetails.BootOption]
        EFI: _ClassVar[AzureVmDetails.BootOption]
        BIOS: _ClassVar[AzureVmDetails.BootOption]
    BOOT_OPTION_UNSPECIFIED: AzureVmDetails.BootOption
    EFI: AzureVmDetails.BootOption
    BIOS: AzureVmDetails.BootOption

    class VmArchitecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VM_ARCHITECTURE_UNSPECIFIED: _ClassVar[AzureVmDetails.VmArchitecture]
        VM_ARCHITECTURE_X86_FAMILY: _ClassVar[AzureVmDetails.VmArchitecture]
        VM_ARCHITECTURE_ARM64: _ClassVar[AzureVmDetails.VmArchitecture]
    VM_ARCHITECTURE_UNSPECIFIED: AzureVmDetails.VmArchitecture
    VM_ARCHITECTURE_X86_FAMILY: AzureVmDetails.VmArchitecture
    VM_ARCHITECTURE_ARM64: AzureVmDetails.VmArchitecture

    class OSDisk(_message.Message):
        __slots__ = ('type', 'name', 'size_gb')
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        type: str
        name: str
        size_gb: int

        def __init__(self, type: _Optional[str]=..., name: _Optional[str]=..., size_gb: _Optional[int]=...) -> None:
            ...

    class Disk(_message.Message):
        __slots__ = ('name', 'size_gb', 'lun')
        NAME_FIELD_NUMBER: _ClassVar[int]
        SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        LUN_FIELD_NUMBER: _ClassVar[int]
        name: str
        size_gb: int
        lun: int

        def __init__(self, name: _Optional[str]=..., size_gb: _Optional[int]=..., lun: _Optional[int]=...) -> None:
            ...

    class OSDescription(_message.Message):
        __slots__ = ('type', 'publisher', 'offer', 'plan')
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PUBLISHER_FIELD_NUMBER: _ClassVar[int]
        OFFER_FIELD_NUMBER: _ClassVar[int]
        PLAN_FIELD_NUMBER: _ClassVar[int]
        type: str
        publisher: str
        offer: str
        plan: str

        def __init__(self, type: _Optional[str]=..., publisher: _Optional[str]=..., offer: _Optional[str]=..., plan: _Optional[str]=...) -> None:
            ...

    class TagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    VM_SIZE_FIELD_NUMBER: _ClassVar[int]
    CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    DISK_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_STORAGE_MB_FIELD_NUMBER: _ClassVar[int]
    OS_DISK_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    OS_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BOOT_OPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_NAME_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    power_state: AzureVmDetails.PowerState
    vm_size: str
    cpu_count: int
    memory_mb: int
    disk_count: int
    committed_storage_mb: int
    os_disk: AzureVmDetails.OSDisk
    disks: _containers.RepeatedCompositeFieldContainer[AzureVmDetails.Disk]
    os_description: AzureVmDetails.OSDescription
    boot_option: AzureVmDetails.BootOption
    tags: _containers.ScalarMap[str, str]
    computer_name: str
    architecture: AzureVmDetails.VmArchitecture

    def __init__(self, vm_id: _Optional[str]=..., power_state: _Optional[_Union[AzureVmDetails.PowerState, str]]=..., vm_size: _Optional[str]=..., cpu_count: _Optional[int]=..., memory_mb: _Optional[int]=..., disk_count: _Optional[int]=..., committed_storage_mb: _Optional[int]=..., os_disk: _Optional[_Union[AzureVmDetails.OSDisk, _Mapping]]=..., disks: _Optional[_Iterable[_Union[AzureVmDetails.Disk, _Mapping]]]=..., os_description: _Optional[_Union[AzureVmDetails.OSDescription, _Mapping]]=..., boot_option: _Optional[_Union[AzureVmDetails.BootOption, str]]=..., tags: _Optional[_Mapping[str, str]]=..., computer_name: _Optional[str]=..., architecture: _Optional[_Union[AzureVmDetails.VmArchitecture, str]]=...) -> None:
        ...

class VmwareVmsDetails(_message.Message):
    __slots__ = ('details',)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[VmwareVmDetails]

    def __init__(self, details: _Optional[_Iterable[_Union[VmwareVmDetails, _Mapping]]]=...) -> None:
        ...

class AwsVmsDetails(_message.Message):
    __slots__ = ('details',)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[AwsVmDetails]

    def __init__(self, details: _Optional[_Iterable[_Union[AwsVmDetails, _Mapping]]]=...) -> None:
        ...

class AzureVmsDetails(_message.Message):
    __slots__ = ('details',)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[AzureVmDetails]

    def __init__(self, details: _Optional[_Iterable[_Union[AzureVmDetails, _Mapping]]]=...) -> None:
        ...

class FetchInventoryResponse(_message.Message):
    __slots__ = ('vmware_vms', 'aws_vms', 'azure_vms', 'update_time')
    VMWARE_VMS_FIELD_NUMBER: _ClassVar[int]
    AWS_VMS_FIELD_NUMBER: _ClassVar[int]
    AZURE_VMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    vmware_vms: VmwareVmsDetails
    aws_vms: AwsVmsDetails
    azure_vms: AzureVmsDetails
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, vmware_vms: _Optional[_Union[VmwareVmsDetails, _Mapping]]=..., aws_vms: _Optional[_Union[AwsVmsDetails, _Mapping]]=..., azure_vms: _Optional[_Union[AzureVmsDetails, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class FetchStorageInventoryRequest(_message.Message):
    __slots__ = ('source', 'type', 'force_refresh', 'page_size', 'page_token')

    class StorageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_TYPE_UNSPECIFIED: _ClassVar[FetchStorageInventoryRequest.StorageType]
        DISKS: _ClassVar[FetchStorageInventoryRequest.StorageType]
        SNAPSHOTS: _ClassVar[FetchStorageInventoryRequest.StorageType]
    STORAGE_TYPE_UNSPECIFIED: FetchStorageInventoryRequest.StorageType
    DISKS: FetchStorageInventoryRequest.StorageType
    SNAPSHOTS: FetchStorageInventoryRequest.StorageType
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FORCE_REFRESH_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    source: str
    type: FetchStorageInventoryRequest.StorageType
    force_refresh: bool
    page_size: int
    page_token: str

    def __init__(self, source: _Optional[str]=..., type: _Optional[_Union[FetchStorageInventoryRequest.StorageType, str]]=..., force_refresh: bool=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchStorageInventoryResponse(_message.Message):
    __slots__ = ('resources', 'update_time', 'next_page_token')
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[SourceStorageResource]
    update_time: _timestamp_pb2.Timestamp
    next_page_token: str

    def __init__(self, resources: _Optional[_Iterable[_Union[SourceStorageResource, _Mapping]]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SourceStorageResource(_message.Message):
    __slots__ = ('aws_disk_details',)
    AWS_DISK_DETAILS_FIELD_NUMBER: _ClassVar[int]
    aws_disk_details: AwsSourceDiskDetails

    def __init__(self, aws_disk_details: _Optional[_Union[AwsSourceDiskDetails, _Mapping]]=...) -> None:
        ...

class UtilizationReport(_message.Message):
    __slots__ = ('name', 'display_name', 'state', 'state_time', 'error', 'create_time', 'time_frame', 'frame_end_time', 'vm_count', 'vms')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[UtilizationReport.State]
        CREATING: _ClassVar[UtilizationReport.State]
        SUCCEEDED: _ClassVar[UtilizationReport.State]
        FAILED: _ClassVar[UtilizationReport.State]
    STATE_UNSPECIFIED: UtilizationReport.State
    CREATING: UtilizationReport.State
    SUCCEEDED: UtilizationReport.State
    FAILED: UtilizationReport.State

    class TimeFrame(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIME_FRAME_UNSPECIFIED: _ClassVar[UtilizationReport.TimeFrame]
        WEEK: _ClassVar[UtilizationReport.TimeFrame]
        MONTH: _ClassVar[UtilizationReport.TimeFrame]
        YEAR: _ClassVar[UtilizationReport.TimeFrame]
    TIME_FRAME_UNSPECIFIED: UtilizationReport.TimeFrame
    WEEK: UtilizationReport.TimeFrame
    MONTH: UtilizationReport.TimeFrame
    YEAR: UtilizationReport.TimeFrame
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_FRAME_FIELD_NUMBER: _ClassVar[int]
    FRAME_END_TIME_FIELD_NUMBER: _ClassVar[int]
    VM_COUNT_FIELD_NUMBER: _ClassVar[int]
    VMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    state: UtilizationReport.State
    state_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    create_time: _timestamp_pb2.Timestamp
    time_frame: UtilizationReport.TimeFrame
    frame_end_time: _timestamp_pb2.Timestamp
    vm_count: int
    vms: _containers.RepeatedCompositeFieldContainer[VmUtilizationInfo]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[UtilizationReport.State, str]]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., time_frame: _Optional[_Union[UtilizationReport.TimeFrame, str]]=..., frame_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., vm_count: _Optional[int]=..., vms: _Optional[_Iterable[_Union[VmUtilizationInfo, _Mapping]]]=...) -> None:
        ...

class VmUtilizationInfo(_message.Message):
    __slots__ = ('vmware_vm_details', 'vm_id', 'utilization')
    VMWARE_VM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    vmware_vm_details: VmwareVmDetails
    vm_id: str
    utilization: VmUtilizationMetrics

    def __init__(self, vmware_vm_details: _Optional[_Union[VmwareVmDetails, _Mapping]]=..., vm_id: _Optional[str]=..., utilization: _Optional[_Union[VmUtilizationMetrics, _Mapping]]=...) -> None:
        ...

class VmUtilizationMetrics(_message.Message):
    __slots__ = ('cpu_max_percent', 'cpu_average_percent', 'memory_max_percent', 'memory_average_percent', 'disk_io_rate_max_kbps', 'disk_io_rate_average_kbps', 'network_throughput_max_kbps', 'network_throughput_average_kbps')
    CPU_MAX_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CPU_AVERAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MAX_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_AVERAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DISK_IO_RATE_MAX_KBPS_FIELD_NUMBER: _ClassVar[int]
    DISK_IO_RATE_AVERAGE_KBPS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_THROUGHPUT_MAX_KBPS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_THROUGHPUT_AVERAGE_KBPS_FIELD_NUMBER: _ClassVar[int]
    cpu_max_percent: int
    cpu_average_percent: int
    memory_max_percent: int
    memory_average_percent: int
    disk_io_rate_max_kbps: int
    disk_io_rate_average_kbps: int
    network_throughput_max_kbps: int
    network_throughput_average_kbps: int

    def __init__(self, cpu_max_percent: _Optional[int]=..., cpu_average_percent: _Optional[int]=..., memory_max_percent: _Optional[int]=..., memory_average_percent: _Optional[int]=..., disk_io_rate_max_kbps: _Optional[int]=..., disk_io_rate_average_kbps: _Optional[int]=..., network_throughput_max_kbps: _Optional[int]=..., network_throughput_average_kbps: _Optional[int]=...) -> None:
        ...

class ListUtilizationReportsRequest(_message.Message):
    __slots__ = ('parent', 'view', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    view: UtilizationReportView
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., view: _Optional[_Union[UtilizationReportView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListUtilizationReportsResponse(_message.Message):
    __slots__ = ('utilization_reports', 'next_page_token', 'unreachable')
    UTILIZATION_REPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    utilization_reports: _containers.RepeatedCompositeFieldContainer[UtilizationReport]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, utilization_reports: _Optional[_Iterable[_Union[UtilizationReport, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetUtilizationReportRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: UtilizationReportView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[UtilizationReportView, str]]=...) -> None:
        ...

class CreateUtilizationReportRequest(_message.Message):
    __slots__ = ('parent', 'utilization_report', 'utilization_report_id', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_REPORT_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    utilization_report: UtilizationReport
    utilization_report_id: str
    request_id: str

    def __init__(self, parent: _Optional[str]=..., utilization_report: _Optional[_Union[UtilizationReport, _Mapping]]=..., utilization_report_id: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteUtilizationReportRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListDatacenterConnectorsResponse(_message.Message):
    __slots__ = ('datacenter_connectors', 'next_page_token', 'unreachable')
    DATACENTER_CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    datacenter_connectors: _containers.RepeatedCompositeFieldContainer[DatacenterConnector]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, datacenter_connectors: _Optional[_Iterable[_Union[DatacenterConnector, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDatacenterConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDatacenterConnectorRequest(_message.Message):
    __slots__ = ('parent', 'datacenter_connector_id', 'datacenter_connector', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    datacenter_connector_id: str
    datacenter_connector: DatacenterConnector
    request_id: str

    def __init__(self, parent: _Optional[str]=..., datacenter_connector_id: _Optional[str]=..., datacenter_connector: _Optional[_Union[DatacenterConnector, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteDatacenterConnectorRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpgradeApplianceRequest(_message.Message):
    __slots__ = ('datacenter_connector', 'request_id')
    DATACENTER_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    datacenter_connector: str
    request_id: str

    def __init__(self, datacenter_connector: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpgradeApplianceResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListDatacenterConnectorsRequest(_message.Message):
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

class ComputeEngineTargetDefaults(_message.Message):
    __slots__ = ('vm_name', 'target_project', 'zone', 'machine_type_series', 'machine_type', 'network_tags', 'network_interfaces', 'service_account', 'disk_type', 'labels', 'license_type', 'applied_license', 'compute_scheduling', 'secure_boot', 'enable_vtpm', 'enable_integrity_monitoring', 'boot_option', 'metadata', 'additional_licenses', 'hostname', 'encryption', 'boot_conversion', 'disk_replica_zones')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_SERIES_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LICENSE_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VTPM_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INTEGRITY_MONITORING_FIELD_NUMBER: _ClassVar[int]
    BOOT_OPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LICENSES_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    BOOT_CONVERSION_FIELD_NUMBER: _ClassVar[int]
    DISK_REPLICA_ZONES_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    target_project: str
    zone: str
    machine_type_series: str
    machine_type: str
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    service_account: str
    disk_type: ComputeEngineDiskType
    labels: _containers.ScalarMap[str, str]
    license_type: ComputeEngineLicenseType
    applied_license: AppliedLicense
    compute_scheduling: ComputeScheduling
    secure_boot: bool
    enable_vtpm: bool
    enable_integrity_monitoring: bool
    boot_option: ComputeEngineBootOption
    metadata: _containers.ScalarMap[str, str]
    additional_licenses: _containers.RepeatedScalarFieldContainer[str]
    hostname: str
    encryption: Encryption
    boot_conversion: BootConversion
    disk_replica_zones: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, vm_name: _Optional[str]=..., target_project: _Optional[str]=..., zone: _Optional[str]=..., machine_type_series: _Optional[str]=..., machine_type: _Optional[str]=..., network_tags: _Optional[_Iterable[str]]=..., network_interfaces: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]]=..., service_account: _Optional[str]=..., disk_type: _Optional[_Union[ComputeEngineDiskType, str]]=..., labels: _Optional[_Mapping[str, str]]=..., license_type: _Optional[_Union[ComputeEngineLicenseType, str]]=..., applied_license: _Optional[_Union[AppliedLicense, _Mapping]]=..., compute_scheduling: _Optional[_Union[ComputeScheduling, _Mapping]]=..., secure_boot: bool=..., enable_vtpm: bool=..., enable_integrity_monitoring: bool=..., boot_option: _Optional[_Union[ComputeEngineBootOption, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., additional_licenses: _Optional[_Iterable[str]]=..., hostname: _Optional[str]=..., encryption: _Optional[_Union[Encryption, _Mapping]]=..., boot_conversion: _Optional[_Union[BootConversion, str]]=..., disk_replica_zones: _Optional[_Iterable[str]]=...) -> None:
        ...

class ComputeEngineTargetDetails(_message.Message):
    __slots__ = ('vm_name', 'project', 'zone', 'machine_type_series', 'machine_type', 'network_tags', 'network_interfaces', 'service_account', 'disk_type', 'labels', 'license_type', 'applied_license', 'compute_scheduling', 'secure_boot', 'enable_vtpm', 'enable_integrity_monitoring', 'boot_option', 'metadata', 'additional_licenses', 'hostname', 'encryption', 'boot_conversion', 'disk_replica_zones')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_SERIES_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LICENSE_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VTPM_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INTEGRITY_MONITORING_FIELD_NUMBER: _ClassVar[int]
    BOOT_OPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LICENSES_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    BOOT_CONVERSION_FIELD_NUMBER: _ClassVar[int]
    DISK_REPLICA_ZONES_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    project: str
    zone: str
    machine_type_series: str
    machine_type: str
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    service_account: str
    disk_type: ComputeEngineDiskType
    labels: _containers.ScalarMap[str, str]
    license_type: ComputeEngineLicenseType
    applied_license: AppliedLicense
    compute_scheduling: ComputeScheduling
    secure_boot: bool
    enable_vtpm: bool
    enable_integrity_monitoring: bool
    boot_option: ComputeEngineBootOption
    metadata: _containers.ScalarMap[str, str]
    additional_licenses: _containers.RepeatedScalarFieldContainer[str]
    hostname: str
    encryption: Encryption
    boot_conversion: BootConversion
    disk_replica_zones: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, vm_name: _Optional[str]=..., project: _Optional[str]=..., zone: _Optional[str]=..., machine_type_series: _Optional[str]=..., machine_type: _Optional[str]=..., network_tags: _Optional[_Iterable[str]]=..., network_interfaces: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]]=..., service_account: _Optional[str]=..., disk_type: _Optional[_Union[ComputeEngineDiskType, str]]=..., labels: _Optional[_Mapping[str, str]]=..., license_type: _Optional[_Union[ComputeEngineLicenseType, str]]=..., applied_license: _Optional[_Union[AppliedLicense, _Mapping]]=..., compute_scheduling: _Optional[_Union[ComputeScheduling, _Mapping]]=..., secure_boot: bool=..., enable_vtpm: bool=..., enable_integrity_monitoring: bool=..., boot_option: _Optional[_Union[ComputeEngineBootOption, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., additional_licenses: _Optional[_Iterable[str]]=..., hostname: _Optional[str]=..., encryption: _Optional[_Union[Encryption, _Mapping]]=..., boot_conversion: _Optional[_Union[BootConversion, str]]=..., disk_replica_zones: _Optional[_Iterable[str]]=...) -> None:
        ...

class NetworkInterface(_message.Message):
    __slots__ = ('network', 'subnetwork', 'internal_ip', 'external_ip', 'network_tier')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TIER_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str
    internal_ip: str
    external_ip: str
    network_tier: ComputeEngineNetworkTier

    def __init__(self, network: _Optional[str]=..., subnetwork: _Optional[str]=..., internal_ip: _Optional[str]=..., external_ip: _Optional[str]=..., network_tier: _Optional[_Union[ComputeEngineNetworkTier, str]]=...) -> None:
        ...

class AppliedLicense(_message.Message):
    __slots__ = ('type', 'os_license')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AppliedLicense.Type]
        NONE: _ClassVar[AppliedLicense.Type]
        PAYG: _ClassVar[AppliedLicense.Type]
        BYOL: _ClassVar[AppliedLicense.Type]
    TYPE_UNSPECIFIED: AppliedLicense.Type
    NONE: AppliedLicense.Type
    PAYG: AppliedLicense.Type
    BYOL: AppliedLicense.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_LICENSE_FIELD_NUMBER: _ClassVar[int]
    type: AppliedLicense.Type
    os_license: str

    def __init__(self, type: _Optional[_Union[AppliedLicense.Type, str]]=..., os_license: _Optional[str]=...) -> None:
        ...

class SchedulingNodeAffinity(_message.Message):
    __slots__ = ('key', 'operator', 'values')

    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATOR_UNSPECIFIED: _ClassVar[SchedulingNodeAffinity.Operator]
        IN: _ClassVar[SchedulingNodeAffinity.Operator]
        NOT_IN: _ClassVar[SchedulingNodeAffinity.Operator]
    OPERATOR_UNSPECIFIED: SchedulingNodeAffinity.Operator
    IN: SchedulingNodeAffinity.Operator
    NOT_IN: SchedulingNodeAffinity.Operator
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    operator: SchedulingNodeAffinity.Operator
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, key: _Optional[str]=..., operator: _Optional[_Union[SchedulingNodeAffinity.Operator, str]]=..., values: _Optional[_Iterable[str]]=...) -> None:
        ...

class ComputeScheduling(_message.Message):
    __slots__ = ('on_host_maintenance', 'restart_type', 'node_affinities', 'min_node_cpus')

    class OnHostMaintenance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ON_HOST_MAINTENANCE_UNSPECIFIED: _ClassVar[ComputeScheduling.OnHostMaintenance]
        TERMINATE: _ClassVar[ComputeScheduling.OnHostMaintenance]
        MIGRATE: _ClassVar[ComputeScheduling.OnHostMaintenance]
    ON_HOST_MAINTENANCE_UNSPECIFIED: ComputeScheduling.OnHostMaintenance
    TERMINATE: ComputeScheduling.OnHostMaintenance
    MIGRATE: ComputeScheduling.OnHostMaintenance

    class RestartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESTART_TYPE_UNSPECIFIED: _ClassVar[ComputeScheduling.RestartType]
        AUTOMATIC_RESTART: _ClassVar[ComputeScheduling.RestartType]
        NO_AUTOMATIC_RESTART: _ClassVar[ComputeScheduling.RestartType]
    RESTART_TYPE_UNSPECIFIED: ComputeScheduling.RestartType
    AUTOMATIC_RESTART: ComputeScheduling.RestartType
    NO_AUTOMATIC_RESTART: ComputeScheduling.RestartType
    ON_HOST_MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    RESTART_TYPE_FIELD_NUMBER: _ClassVar[int]
    NODE_AFFINITIES_FIELD_NUMBER: _ClassVar[int]
    MIN_NODE_CPUS_FIELD_NUMBER: _ClassVar[int]
    on_host_maintenance: ComputeScheduling.OnHostMaintenance
    restart_type: ComputeScheduling.RestartType
    node_affinities: _containers.RepeatedCompositeFieldContainer[SchedulingNodeAffinity]
    min_node_cpus: int

    def __init__(self, on_host_maintenance: _Optional[_Union[ComputeScheduling.OnHostMaintenance, str]]=..., restart_type: _Optional[_Union[ComputeScheduling.RestartType, str]]=..., node_affinities: _Optional[_Iterable[_Union[SchedulingNodeAffinity, _Mapping]]]=..., min_node_cpus: _Optional[int]=...) -> None:
        ...

class ComputeEngineDisksTargetDefaults(_message.Message):
    __slots__ = ('zone', 'disks_target_defaults', 'vm_target_defaults', 'target_project', 'disks')
    ZONE_FIELD_NUMBER: _ClassVar[int]
    DISKS_TARGET_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    VM_TARGET_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    zone: str
    disks_target_defaults: DisksMigrationDisksTargetDefaults
    vm_target_defaults: DisksMigrationVmTargetDefaults
    target_project: str
    disks: _containers.RepeatedCompositeFieldContainer[PersistentDiskDefaults]

    def __init__(self, zone: _Optional[str]=..., disks_target_defaults: _Optional[_Union[DisksMigrationDisksTargetDefaults, _Mapping]]=..., vm_target_defaults: _Optional[_Union[DisksMigrationVmTargetDefaults, _Mapping]]=..., target_project: _Optional[str]=..., disks: _Optional[_Iterable[_Union[PersistentDiskDefaults, _Mapping]]]=...) -> None:
        ...

class PersistentDiskDefaults(_message.Message):
    __slots__ = ('source_disk_number', 'disk_name', 'disk_type', 'additional_labels', 'encryption', 'vm_attachment_details')

    class AdditionalLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    SOURCE_DISK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LABELS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    VM_ATTACHMENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    source_disk_number: int
    disk_name: str
    disk_type: ComputeEngineDiskType
    additional_labels: _containers.ScalarMap[str, str]
    encryption: Encryption
    vm_attachment_details: VmAttachmentDetails

    def __init__(self, source_disk_number: _Optional[int]=..., disk_name: _Optional[str]=..., disk_type: _Optional[_Union[ComputeEngineDiskType, str]]=..., additional_labels: _Optional[_Mapping[str, str]]=..., encryption: _Optional[_Union[Encryption, _Mapping]]=..., vm_attachment_details: _Optional[_Union[VmAttachmentDetails, _Mapping]]=...) -> None:
        ...

class VmAttachmentDetails(_message.Message):
    __slots__ = ('device_name',)
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    device_name: str

    def __init__(self, device_name: _Optional[str]=...) -> None:
        ...

class DisksMigrationDisksTargetDefaults(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DisksMigrationVmTargetDefaults(_message.Message):
    __slots__ = ('vm_name', 'machine_type_series', 'machine_type', 'network_tags', 'network_interfaces', 'service_account', 'compute_scheduling', 'secure_boot', 'enable_vtpm', 'enable_integrity_monitoring', 'metadata', 'additional_licenses', 'hostname', 'labels', 'boot_disk_defaults', 'encryption')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_SERIES_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VTPM_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INTEGRITY_MONITORING_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LICENSES_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    machine_type_series: str
    machine_type: str
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    service_account: str
    compute_scheduling: ComputeScheduling
    secure_boot: bool
    enable_vtpm: bool
    enable_integrity_monitoring: bool
    metadata: _containers.ScalarMap[str, str]
    additional_licenses: _containers.RepeatedScalarFieldContainer[str]
    hostname: str
    labels: _containers.ScalarMap[str, str]
    boot_disk_defaults: BootDiskDefaults
    encryption: Encryption

    def __init__(self, vm_name: _Optional[str]=..., machine_type_series: _Optional[str]=..., machine_type: _Optional[str]=..., network_tags: _Optional[_Iterable[str]]=..., network_interfaces: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]]=..., service_account: _Optional[str]=..., compute_scheduling: _Optional[_Union[ComputeScheduling, _Mapping]]=..., secure_boot: bool=..., enable_vtpm: bool=..., enable_integrity_monitoring: bool=..., metadata: _Optional[_Mapping[str, str]]=..., additional_licenses: _Optional[_Iterable[str]]=..., hostname: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., boot_disk_defaults: _Optional[_Union[BootDiskDefaults, _Mapping]]=..., encryption: _Optional[_Union[Encryption, _Mapping]]=...) -> None:
        ...

class BootDiskDefaults(_message.Message):
    __slots__ = ('image', 'disk_name', 'disk_type', 'device_name', 'encryption')

    class DiskImageDefaults(_message.Message):
        __slots__ = ('source_image',)
        SOURCE_IMAGE_FIELD_NUMBER: _ClassVar[int]
        source_image: str

        def __init__(self, source_image: _Optional[str]=...) -> None:
            ...
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    image: BootDiskDefaults.DiskImageDefaults
    disk_name: str
    disk_type: ComputeEngineDiskType
    device_name: str
    encryption: Encryption

    def __init__(self, image: _Optional[_Union[BootDiskDefaults.DiskImageDefaults, _Mapping]]=..., disk_name: _Optional[str]=..., disk_type: _Optional[_Union[ComputeEngineDiskType, str]]=..., device_name: _Optional[str]=..., encryption: _Optional[_Union[Encryption, _Mapping]]=...) -> None:
        ...

class ComputeEngineDisksTargetDetails(_message.Message):
    __slots__ = ('disks_target_details', 'vm_target_details', 'disks')
    DISKS_TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VM_TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    disks_target_details: DisksMigrationDisksTargetDetails
    vm_target_details: DisksMigrationVmTargetDetails
    disks: _containers.RepeatedCompositeFieldContainer[PersistentDisk]

    def __init__(self, disks_target_details: _Optional[_Union[DisksMigrationDisksTargetDetails, _Mapping]]=..., vm_target_details: _Optional[_Union[DisksMigrationVmTargetDetails, _Mapping]]=..., disks: _Optional[_Iterable[_Union[PersistentDisk, _Mapping]]]=...) -> None:
        ...

class PersistentDisk(_message.Message):
    __slots__ = ('source_disk_number', 'disk_uri')
    SOURCE_DISK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DISK_URI_FIELD_NUMBER: _ClassVar[int]
    source_disk_number: int
    disk_uri: str

    def __init__(self, source_disk_number: _Optional[int]=..., disk_uri: _Optional[str]=...) -> None:
        ...

class DisksMigrationDisksTargetDetails(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DisksMigrationVmTargetDetails(_message.Message):
    __slots__ = ('vm_uri',)
    VM_URI_FIELD_NUMBER: _ClassVar[int]
    vm_uri: str

    def __init__(self, vm_uri: _Optional[str]=...) -> None:
        ...

class SchedulePolicy(_message.Message):
    __slots__ = ('idle_duration', 'skip_os_adaptation')
    IDLE_DURATION_FIELD_NUMBER: _ClassVar[int]
    SKIP_OS_ADAPTATION_FIELD_NUMBER: _ClassVar[int]
    idle_duration: _duration_pb2.Duration
    skip_os_adaptation: bool

    def __init__(self, idle_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., skip_os_adaptation: bool=...) -> None:
        ...

class CreateMigratingVmRequest(_message.Message):
    __slots__ = ('parent', 'migrating_vm_id', 'migrating_vm', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_VM_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    migrating_vm_id: str
    migrating_vm: MigratingVm
    request_id: str

    def __init__(self, parent: _Optional[str]=..., migrating_vm_id: _Optional[str]=..., migrating_vm: _Optional[_Union[MigratingVm, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListMigratingVmsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    view: MigratingVmView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., view: _Optional[_Union[MigratingVmView, str]]=...) -> None:
        ...

class ListMigratingVmsResponse(_message.Message):
    __slots__ = ('migrating_vms', 'next_page_token', 'unreachable')
    MIGRATING_VMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    migrating_vms: _containers.RepeatedCompositeFieldContainer[MigratingVm]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, migrating_vms: _Optional[_Iterable[_Union[MigratingVm, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetMigratingVmRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: MigratingVmView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[MigratingVmView, str]]=...) -> None:
        ...

class UpdateMigratingVmRequest(_message.Message):
    __slots__ = ('update_mask', 'migrating_vm', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    migrating_vm: MigratingVm
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., migrating_vm: _Optional[_Union[MigratingVm, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteMigratingVmRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StartMigrationRequest(_message.Message):
    __slots__ = ('migrating_vm',)
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    migrating_vm: str

    def __init__(self, migrating_vm: _Optional[str]=...) -> None:
        ...

class StartMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PauseMigrationRequest(_message.Message):
    __slots__ = ('migrating_vm',)
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    migrating_vm: str

    def __init__(self, migrating_vm: _Optional[str]=...) -> None:
        ...

class PauseMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ResumeMigrationRequest(_message.Message):
    __slots__ = ('migrating_vm',)
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    migrating_vm: str

    def __init__(self, migrating_vm: _Optional[str]=...) -> None:
        ...

class ResumeMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class FinalizeMigrationRequest(_message.Message):
    __slots__ = ('migrating_vm',)
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    migrating_vm: str

    def __init__(self, migrating_vm: _Optional[str]=...) -> None:
        ...

class ExtendMigrationRequest(_message.Message):
    __slots__ = ('migrating_vm',)
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    migrating_vm: str

    def __init__(self, migrating_vm: _Optional[str]=...) -> None:
        ...

class ExtendMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class FinalizeMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TargetProject(_message.Message):
    __slots__ = ('name', 'project', 'description', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    project: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., project: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetTargetProjectRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTargetProjectsRequest(_message.Message):
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

class ListTargetProjectsResponse(_message.Message):
    __slots__ = ('target_projects', 'next_page_token', 'unreachable')
    TARGET_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    target_projects: _containers.RepeatedCompositeFieldContainer[TargetProject]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, target_projects: _Optional[_Iterable[_Union[TargetProject, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateTargetProjectRequest(_message.Message):
    __slots__ = ('parent', 'target_project_id', 'target_project', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    target_project_id: str
    target_project: TargetProject
    request_id: str

    def __init__(self, parent: _Optional[str]=..., target_project_id: _Optional[str]=..., target_project: _Optional[_Union[TargetProject, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateTargetProjectRequest(_message.Message):
    __slots__ = ('update_mask', 'target_project', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    target_project: TargetProject
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., target_project: _Optional[_Union[TargetProject, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteTargetProjectRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class Group(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'description', 'display_name', 'migration_target_type')

    class MigrationTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MIGRATION_TARGET_TYPE_UNSPECIFIED: _ClassVar[Group.MigrationTargetType]
        MIGRATION_TARGET_TYPE_GCE: _ClassVar[Group.MigrationTargetType]
        MIGRATION_TARGET_TYPE_DISKS: _ClassVar[Group.MigrationTargetType]
    MIGRATION_TARGET_TYPE_UNSPECIFIED: Group.MigrationTargetType
    MIGRATION_TARGET_TYPE_GCE: Group.MigrationTargetType
    MIGRATION_TARGET_TYPE_DISKS: Group.MigrationTargetType
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    display_name: str
    migration_target_type: Group.MigrationTargetType

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., display_name: _Optional[str]=..., migration_target_type: _Optional[_Union[Group.MigrationTargetType, str]]=...) -> None:
        ...

class ListGroupsRequest(_message.Message):
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

class ListGroupsResponse(_message.Message):
    __slots__ = ('groups', 'next_page_token', 'unreachable')
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[Group]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, groups: _Optional[_Iterable[_Union[Group, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetGroupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateGroupRequest(_message.Message):
    __slots__ = ('parent', 'group_id', 'group', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    group_id: str
    group: Group
    request_id: str

    def __init__(self, parent: _Optional[str]=..., group_id: _Optional[str]=..., group: _Optional[_Union[Group, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateGroupRequest(_message.Message):
    __slots__ = ('update_mask', 'group', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    group: Group
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., group: _Optional[_Union[Group, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteGroupRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class AddGroupMigrationRequest(_message.Message):
    __slots__ = ('group', 'migrating_vm')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    group: str
    migrating_vm: str

    def __init__(self, group: _Optional[str]=..., migrating_vm: _Optional[str]=...) -> None:
        ...

class AddGroupMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RemoveGroupMigrationRequest(_message.Message):
    __slots__ = ('group', 'migrating_vm')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    group: str
    migrating_vm: str

    def __init__(self, group: _Optional[str]=..., migrating_vm: _Optional[str]=...) -> None:
        ...

class RemoveGroupMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateCutoverJobRequest(_message.Message):
    __slots__ = ('parent', 'cutover_job_id', 'cutover_job', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUTOVER_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CUTOVER_JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cutover_job_id: str
    cutover_job: CutoverJob
    request_id: str

    def __init__(self, parent: _Optional[str]=..., cutover_job_id: _Optional[str]=..., cutover_job: _Optional[_Union[CutoverJob, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class CancelCutoverJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelCutoverJobResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListCutoverJobsRequest(_message.Message):
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

class ListCutoverJobsResponse(_message.Message):
    __slots__ = ('cutover_jobs', 'next_page_token', 'unreachable')
    CUTOVER_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    cutover_jobs: _containers.RepeatedCompositeFieldContainer[CutoverJob]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, cutover_jobs: _Optional[_Iterable[_Union[CutoverJob, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCutoverJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
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

class MigrationError(_message.Message):
    __slots__ = ('code', 'error_message', 'action_item', 'help_links', 'error_time')

    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CODE_UNSPECIFIED: _ClassVar[MigrationError.ErrorCode]
        UNKNOWN_ERROR: _ClassVar[MigrationError.ErrorCode]
        SOURCE_VALIDATION_ERROR: _ClassVar[MigrationError.ErrorCode]
        SOURCE_REPLICATION_ERROR: _ClassVar[MigrationError.ErrorCode]
        TARGET_REPLICATION_ERROR: _ClassVar[MigrationError.ErrorCode]
        OS_ADAPTATION_ERROR: _ClassVar[MigrationError.ErrorCode]
        CLONE_ERROR: _ClassVar[MigrationError.ErrorCode]
        CUTOVER_ERROR: _ClassVar[MigrationError.ErrorCode]
        UTILIZATION_REPORT_ERROR: _ClassVar[MigrationError.ErrorCode]
        APPLIANCE_UPGRADE_ERROR: _ClassVar[MigrationError.ErrorCode]
        IMAGE_IMPORT_ERROR: _ClassVar[MigrationError.ErrorCode]
        DISK_MIGRATION_ERROR: _ClassVar[MigrationError.ErrorCode]
    ERROR_CODE_UNSPECIFIED: MigrationError.ErrorCode
    UNKNOWN_ERROR: MigrationError.ErrorCode
    SOURCE_VALIDATION_ERROR: MigrationError.ErrorCode
    SOURCE_REPLICATION_ERROR: MigrationError.ErrorCode
    TARGET_REPLICATION_ERROR: MigrationError.ErrorCode
    OS_ADAPTATION_ERROR: MigrationError.ErrorCode
    CLONE_ERROR: MigrationError.ErrorCode
    CUTOVER_ERROR: MigrationError.ErrorCode
    UTILIZATION_REPORT_ERROR: MigrationError.ErrorCode
    APPLIANCE_UPGRADE_ERROR: MigrationError.ErrorCode
    IMAGE_IMPORT_ERROR: MigrationError.ErrorCode
    DISK_MIGRATION_ERROR: MigrationError.ErrorCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTION_ITEM_FIELD_NUMBER: _ClassVar[int]
    HELP_LINKS_FIELD_NUMBER: _ClassVar[int]
    ERROR_TIME_FIELD_NUMBER: _ClassVar[int]
    code: MigrationError.ErrorCode
    error_message: _error_details_pb2.LocalizedMessage
    action_item: _error_details_pb2.LocalizedMessage
    help_links: _containers.RepeatedCompositeFieldContainer[_error_details_pb2.Help.Link]
    error_time: _timestamp_pb2.Timestamp

    def __init__(self, code: _Optional[_Union[MigrationError.ErrorCode, str]]=..., error_message: _Optional[_Union[_error_details_pb2.LocalizedMessage, _Mapping]]=..., action_item: _Optional[_Union[_error_details_pb2.LocalizedMessage, _Mapping]]=..., help_links: _Optional[_Iterable[_Union[_error_details_pb2.Help.Link, _Mapping]]]=..., error_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class MigrationWarning(_message.Message):
    __slots__ = ('code', 'warning_message', 'action_item', 'help_links', 'warning_time')

    class WarningCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WARNING_CODE_UNSPECIFIED: _ClassVar[MigrationWarning.WarningCode]
        ADAPTATION_WARNING: _ClassVar[MigrationWarning.WarningCode]
    WARNING_CODE_UNSPECIFIED: MigrationWarning.WarningCode
    ADAPTATION_WARNING: MigrationWarning.WarningCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    WARNING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTION_ITEM_FIELD_NUMBER: _ClassVar[int]
    HELP_LINKS_FIELD_NUMBER: _ClassVar[int]
    WARNING_TIME_FIELD_NUMBER: _ClassVar[int]
    code: MigrationWarning.WarningCode
    warning_message: _error_details_pb2.LocalizedMessage
    action_item: _error_details_pb2.LocalizedMessage
    help_links: _containers.RepeatedCompositeFieldContainer[_error_details_pb2.Help.Link]
    warning_time: _timestamp_pb2.Timestamp

    def __init__(self, code: _Optional[_Union[MigrationWarning.WarningCode, str]]=..., warning_message: _Optional[_Union[_error_details_pb2.LocalizedMessage, _Mapping]]=..., action_item: _Optional[_Union[_error_details_pb2.LocalizedMessage, _Mapping]]=..., help_links: _Optional[_Iterable[_Union[_error_details_pb2.Help.Link, _Mapping]]]=..., warning_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class VmwareSourceVmDetails(_message.Message):
    __slots__ = ('firmware', 'committed_storage_bytes', 'disks', 'vm_capabilities_info', 'architecture')

    class Firmware(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIRMWARE_UNSPECIFIED: _ClassVar[VmwareSourceVmDetails.Firmware]
        EFI: _ClassVar[VmwareSourceVmDetails.Firmware]
        BIOS: _ClassVar[VmwareSourceVmDetails.Firmware]
    FIRMWARE_UNSPECIFIED: VmwareSourceVmDetails.Firmware
    EFI: VmwareSourceVmDetails.Firmware
    BIOS: VmwareSourceVmDetails.Firmware

    class VmwareDiskDetails(_message.Message):
        __slots__ = ('disk_number', 'size_gb', 'label')
        DISK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        disk_number: int
        size_gb: int
        label: str

        def __init__(self, disk_number: _Optional[int]=..., size_gb: _Optional[int]=..., label: _Optional[str]=...) -> None:
            ...
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    VM_CAPABILITIES_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    firmware: VmwareSourceVmDetails.Firmware
    committed_storage_bytes: int
    disks: _containers.RepeatedCompositeFieldContainer[VmwareSourceVmDetails.VmwareDiskDetails]
    vm_capabilities_info: VmCapabilities
    architecture: VmArchitecture

    def __init__(self, firmware: _Optional[_Union[VmwareSourceVmDetails.Firmware, str]]=..., committed_storage_bytes: _Optional[int]=..., disks: _Optional[_Iterable[_Union[VmwareSourceVmDetails.VmwareDiskDetails, _Mapping]]]=..., vm_capabilities_info: _Optional[_Union[VmCapabilities, _Mapping]]=..., architecture: _Optional[_Union[VmArchitecture, str]]=...) -> None:
        ...

class AwsSourceVmDetails(_message.Message):
    __slots__ = ('firmware', 'committed_storage_bytes', 'disks', 'vm_capabilities_info', 'architecture')

    class Firmware(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIRMWARE_UNSPECIFIED: _ClassVar[AwsSourceVmDetails.Firmware]
        EFI: _ClassVar[AwsSourceVmDetails.Firmware]
        BIOS: _ClassVar[AwsSourceVmDetails.Firmware]
    FIRMWARE_UNSPECIFIED: AwsSourceVmDetails.Firmware
    EFI: AwsSourceVmDetails.Firmware
    BIOS: AwsSourceVmDetails.Firmware

    class AwsDiskDetails(_message.Message):
        __slots__ = ('disk_number', 'volume_id', 'size_gb')
        DISK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        disk_number: int
        volume_id: str
        size_gb: int

        def __init__(self, disk_number: _Optional[int]=..., volume_id: _Optional[str]=..., size_gb: _Optional[int]=...) -> None:
            ...
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    VM_CAPABILITIES_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    firmware: AwsSourceVmDetails.Firmware
    committed_storage_bytes: int
    disks: _containers.RepeatedCompositeFieldContainer[AwsSourceVmDetails.AwsDiskDetails]
    vm_capabilities_info: VmCapabilities
    architecture: VmArchitecture

    def __init__(self, firmware: _Optional[_Union[AwsSourceVmDetails.Firmware, str]]=..., committed_storage_bytes: _Optional[int]=..., disks: _Optional[_Iterable[_Union[AwsSourceVmDetails.AwsDiskDetails, _Mapping]]]=..., vm_capabilities_info: _Optional[_Union[VmCapabilities, _Mapping]]=..., architecture: _Optional[_Union[VmArchitecture, str]]=...) -> None:
        ...

class AzureSourceVmDetails(_message.Message):
    __slots__ = ('firmware', 'committed_storage_bytes', 'disks', 'vm_capabilities_info', 'architecture')

    class Firmware(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIRMWARE_UNSPECIFIED: _ClassVar[AzureSourceVmDetails.Firmware]
        EFI: _ClassVar[AzureSourceVmDetails.Firmware]
        BIOS: _ClassVar[AzureSourceVmDetails.Firmware]
    FIRMWARE_UNSPECIFIED: AzureSourceVmDetails.Firmware
    EFI: AzureSourceVmDetails.Firmware
    BIOS: AzureSourceVmDetails.Firmware

    class AzureDiskDetails(_message.Message):
        __slots__ = ('disk_number', 'disk_id', 'size_gb')
        DISK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        disk_number: int
        disk_id: str
        size_gb: int

        def __init__(self, disk_number: _Optional[int]=..., disk_id: _Optional[str]=..., size_gb: _Optional[int]=...) -> None:
            ...
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    VM_CAPABILITIES_INFO_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    firmware: AzureSourceVmDetails.Firmware
    committed_storage_bytes: int
    disks: _containers.RepeatedCompositeFieldContainer[AzureSourceVmDetails.AzureDiskDetails]
    vm_capabilities_info: VmCapabilities
    architecture: VmArchitecture

    def __init__(self, firmware: _Optional[_Union[AzureSourceVmDetails.Firmware, str]]=..., committed_storage_bytes: _Optional[int]=..., disks: _Optional[_Iterable[_Union[AzureSourceVmDetails.AzureDiskDetails, _Mapping]]]=..., vm_capabilities_info: _Optional[_Union[VmCapabilities, _Mapping]]=..., architecture: _Optional[_Union[VmArchitecture, str]]=...) -> None:
        ...

class ListReplicationCyclesRequest(_message.Message):
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

class ListReplicationCyclesResponse(_message.Message):
    __slots__ = ('replication_cycles', 'next_page_token', 'unreachable')
    REPLICATION_CYCLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    replication_cycles: _containers.RepeatedCompositeFieldContainer[ReplicationCycle]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, replication_cycles: _Optional[_Iterable[_Union[ReplicationCycle, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetReplicationCycleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class VmCapabilities(_message.Message):
    __slots__ = ('os_capabilities', 'last_os_capabilities_update_time')
    OS_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    LAST_OS_CAPABILITIES_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    os_capabilities: _containers.RepeatedScalarFieldContainer[OsCapability]
    last_os_capabilities_update_time: _timestamp_pb2.Timestamp

    def __init__(self, os_capabilities: _Optional[_Iterable[_Union[OsCapability, str]]]=..., last_os_capabilities_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ImageImport(_message.Message):
    __slots__ = ('cloud_storage_uri', 'disk_image_target_defaults', 'machine_image_target_defaults', 'name', 'create_time', 'recent_image_import_jobs', 'encryption')
    CLOUD_STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
    DISK_IMAGE_TARGET_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    MACHINE_IMAGE_TARGET_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RECENT_IMAGE_IMPORT_JOBS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    cloud_storage_uri: str
    disk_image_target_defaults: DiskImageTargetDetails
    machine_image_target_defaults: MachineImageTargetDetails
    name: str
    create_time: _timestamp_pb2.Timestamp
    recent_image_import_jobs: _containers.RepeatedCompositeFieldContainer[ImageImportJob]
    encryption: Encryption

    def __init__(self, cloud_storage_uri: _Optional[str]=..., disk_image_target_defaults: _Optional[_Union[DiskImageTargetDetails, _Mapping]]=..., machine_image_target_defaults: _Optional[_Union[MachineImageTargetDetails, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., recent_image_import_jobs: _Optional[_Iterable[_Union[ImageImportJob, _Mapping]]]=..., encryption: _Optional[_Union[Encryption, _Mapping]]=...) -> None:
        ...

class ImageImportJob(_message.Message):
    __slots__ = ('cloud_storage_uri', 'disk_image_target_details', 'machine_image_target_details', 'name', 'created_resources', 'state', 'create_time', 'end_time', 'errors', 'warnings', 'steps')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ImageImportJob.State]
        PENDING: _ClassVar[ImageImportJob.State]
        RUNNING: _ClassVar[ImageImportJob.State]
        SUCCEEDED: _ClassVar[ImageImportJob.State]
        FAILED: _ClassVar[ImageImportJob.State]
        CANCELLING: _ClassVar[ImageImportJob.State]
        CANCELLED: _ClassVar[ImageImportJob.State]
    STATE_UNSPECIFIED: ImageImportJob.State
    PENDING: ImageImportJob.State
    RUNNING: ImageImportJob.State
    SUCCEEDED: ImageImportJob.State
    FAILED: ImageImportJob.State
    CANCELLING: ImageImportJob.State
    CANCELLED: ImageImportJob.State
    CLOUD_STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
    DISK_IMAGE_TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MACHINE_IMAGE_TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    cloud_storage_uri: str
    disk_image_target_details: DiskImageTargetDetails
    machine_image_target_details: MachineImageTargetDetails
    name: str
    created_resources: _containers.RepeatedScalarFieldContainer[str]
    state: ImageImportJob.State
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    warnings: _containers.RepeatedCompositeFieldContainer[MigrationWarning]
    steps: _containers.RepeatedCompositeFieldContainer[ImageImportStep]

    def __init__(self, cloud_storage_uri: _Optional[str]=..., disk_image_target_details: _Optional[_Union[DiskImageTargetDetails, _Mapping]]=..., machine_image_target_details: _Optional[_Union[MachineImageTargetDetails, _Mapping]]=..., name: _Optional[str]=..., created_resources: _Optional[_Iterable[str]]=..., state: _Optional[_Union[ImageImportJob.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., warnings: _Optional[_Iterable[_Union[MigrationWarning, _Mapping]]]=..., steps: _Optional[_Iterable[_Union[ImageImportStep, _Mapping]]]=...) -> None:
        ...

class ImageImportStep(_message.Message):
    __slots__ = ('initializing', 'loading_source_files', 'adapting_os', 'creating_image', 'start_time', 'end_time')
    INITIALIZING_FIELD_NUMBER: _ClassVar[int]
    LOADING_SOURCE_FILES_FIELD_NUMBER: _ClassVar[int]
    ADAPTING_OS_FIELD_NUMBER: _ClassVar[int]
    CREATING_IMAGE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    initializing: InitializingImageImportStep
    loading_source_files: LoadingImageSourceFilesStep
    adapting_os: AdaptingOSStep
    creating_image: CreatingImageStep
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, initializing: _Optional[_Union[InitializingImageImportStep, _Mapping]]=..., loading_source_files: _Optional[_Union[LoadingImageSourceFilesStep, _Mapping]]=..., adapting_os: _Optional[_Union[AdaptingOSStep, _Mapping]]=..., creating_image: _Optional[_Union[CreatingImageStep, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class InitializingImageImportStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LoadingImageSourceFilesStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreatingImageStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DiskImageTargetDetails(_message.Message):
    __slots__ = ('os_adaptation_parameters', 'data_disk_image_import', 'image_name', 'target_project', 'description', 'family_name', 'labels', 'additional_licenses', 'single_region_storage', 'encryption')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    OS_ADAPTATION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_IMAGE_IMPORT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LICENSES_FIELD_NUMBER: _ClassVar[int]
    SINGLE_REGION_STORAGE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    os_adaptation_parameters: ImageImportOsAdaptationParameters
    data_disk_image_import: DataDiskImageImport
    image_name: str
    target_project: str
    description: str
    family_name: str
    labels: _containers.ScalarMap[str, str]
    additional_licenses: _containers.RepeatedScalarFieldContainer[str]
    single_region_storage: bool
    encryption: Encryption

    def __init__(self, os_adaptation_parameters: _Optional[_Union[ImageImportOsAdaptationParameters, _Mapping]]=..., data_disk_image_import: _Optional[_Union[DataDiskImageImport, _Mapping]]=..., image_name: _Optional[str]=..., target_project: _Optional[str]=..., description: _Optional[str]=..., family_name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., additional_licenses: _Optional[_Iterable[str]]=..., single_region_storage: bool=..., encryption: _Optional[_Union[Encryption, _Mapping]]=...) -> None:
        ...

class MachineImageTargetDetails(_message.Message):
    __slots__ = ('os_adaptation_parameters', 'skip_os_adaptation', 'machine_image_name', 'target_project', 'description', 'single_region_storage', 'encryption', 'machine_image_parameters_overrides', 'service_account', 'additional_licenses', 'labels', 'tags', 'shielded_instance_config', 'network_interfaces')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    OS_ADAPTATION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SKIP_OS_ADAPTATION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SINGLE_REGION_STORAGE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_IMAGE_PARAMETERS_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LICENSES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    os_adaptation_parameters: ImageImportOsAdaptationParameters
    skip_os_adaptation: SkipOsAdaptation
    machine_image_name: str
    target_project: str
    description: str
    single_region_storage: bool
    encryption: Encryption
    machine_image_parameters_overrides: MachineImageParametersOverrides
    service_account: ServiceAccount
    additional_licenses: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.ScalarMap[str, str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    shielded_instance_config: ShieldedInstanceConfig
    network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterface]

    def __init__(self, os_adaptation_parameters: _Optional[_Union[ImageImportOsAdaptationParameters, _Mapping]]=..., skip_os_adaptation: _Optional[_Union[SkipOsAdaptation, _Mapping]]=..., machine_image_name: _Optional[str]=..., target_project: _Optional[str]=..., description: _Optional[str]=..., single_region_storage: bool=..., encryption: _Optional[_Union[Encryption, _Mapping]]=..., machine_image_parameters_overrides: _Optional[_Union[MachineImageParametersOverrides, _Mapping]]=..., service_account: _Optional[_Union[ServiceAccount, _Mapping]]=..., additional_licenses: _Optional[_Iterable[str]]=..., labels: _Optional[_Mapping[str, str]]=..., tags: _Optional[_Iterable[str]]=..., shielded_instance_config: _Optional[_Union[ShieldedInstanceConfig, _Mapping]]=..., network_interfaces: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]]=...) -> None:
        ...

class ServiceAccount(_message.Message):
    __slots__ = ('email', 'scopes')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    email: str
    scopes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, email: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=...) -> None:
        ...

class ShieldedInstanceConfig(_message.Message):
    __slots__ = ('secure_boot', 'enable_vtpm', 'enable_integrity_monitoring')

    class SecureBoot(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SECURE_BOOT_UNSPECIFIED: _ClassVar[ShieldedInstanceConfig.SecureBoot]
        TRUE: _ClassVar[ShieldedInstanceConfig.SecureBoot]
        FALSE: _ClassVar[ShieldedInstanceConfig.SecureBoot]
    SECURE_BOOT_UNSPECIFIED: ShieldedInstanceConfig.SecureBoot
    TRUE: ShieldedInstanceConfig.SecureBoot
    FALSE: ShieldedInstanceConfig.SecureBoot
    SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VTPM_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INTEGRITY_MONITORING_FIELD_NUMBER: _ClassVar[int]
    secure_boot: ShieldedInstanceConfig.SecureBoot
    enable_vtpm: bool
    enable_integrity_monitoring: bool

    def __init__(self, secure_boot: _Optional[_Union[ShieldedInstanceConfig.SecureBoot, str]]=..., enable_vtpm: bool=..., enable_integrity_monitoring: bool=...) -> None:
        ...

class MachineImageParametersOverrides(_message.Message):
    __slots__ = ('machine_type',)
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    machine_type: str

    def __init__(self, machine_type: _Optional[str]=...) -> None:
        ...

class ImageImportOsAdaptationParameters(_message.Message):
    __slots__ = ('generalize', 'license_type', 'boot_conversion')
    GENERALIZE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BOOT_CONVERSION_FIELD_NUMBER: _ClassVar[int]
    generalize: bool
    license_type: ComputeEngineLicenseType
    boot_conversion: BootConversion

    def __init__(self, generalize: bool=..., license_type: _Optional[_Union[ComputeEngineLicenseType, str]]=..., boot_conversion: _Optional[_Union[BootConversion, str]]=...) -> None:
        ...

class DataDiskImageImport(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SkipOsAdaptation(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetImageImportRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListImageImportsRequest(_message.Message):
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

class ListImageImportsResponse(_message.Message):
    __slots__ = ('image_imports', 'next_page_token', 'unreachable')
    IMAGE_IMPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    image_imports: _containers.RepeatedCompositeFieldContainer[ImageImport]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, image_imports: _Optional[_Iterable[_Union[ImageImport, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateImageImportRequest(_message.Message):
    __slots__ = ('parent', 'image_import_id', 'image_import', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_IMPORT_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_IMPORT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    image_import_id: str
    image_import: ImageImport
    request_id: str

    def __init__(self, parent: _Optional[str]=..., image_import_id: _Optional[str]=..., image_import: _Optional[_Union[ImageImport, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteImageImportRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetImageImportJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListImageImportJobsRequest(_message.Message):
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

class ListImageImportJobsResponse(_message.Message):
    __slots__ = ('image_import_jobs', 'next_page_token', 'unreachable')
    IMAGE_IMPORT_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    image_import_jobs: _containers.RepeatedCompositeFieldContainer[ImageImportJob]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, image_import_jobs: _Optional[_Iterable[_Union[ImageImportJob, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CancelImageImportJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelImageImportJobResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DiskMigrationJob(_message.Message):
    __slots__ = ('aws_source_disk_details', 'name', 'target_details', 'create_time', 'update_time', 'state', 'errors', 'steps')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DiskMigrationJob.State]
        READY: _ClassVar[DiskMigrationJob.State]
        RUNNING: _ClassVar[DiskMigrationJob.State]
        SUCCEEDED: _ClassVar[DiskMigrationJob.State]
        CANCELLING: _ClassVar[DiskMigrationJob.State]
        CANCELLED: _ClassVar[DiskMigrationJob.State]
        FAILED: _ClassVar[DiskMigrationJob.State]
    STATE_UNSPECIFIED: DiskMigrationJob.State
    READY: DiskMigrationJob.State
    RUNNING: DiskMigrationJob.State
    SUCCEEDED: DiskMigrationJob.State
    CANCELLING: DiskMigrationJob.State
    CANCELLED: DiskMigrationJob.State
    FAILED: DiskMigrationJob.State
    AWS_SOURCE_DISK_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    aws_source_disk_details: AwsSourceDiskDetails
    name: str
    target_details: DiskMigrationJobTargetDetails
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: DiskMigrationJob.State
    errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    steps: _containers.RepeatedCompositeFieldContainer[DiskMigrationStep]

    def __init__(self, aws_source_disk_details: _Optional[_Union[AwsSourceDiskDetails, _Mapping]]=..., name: _Optional[str]=..., target_details: _Optional[_Union[DiskMigrationJobTargetDetails, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[DiskMigrationJob.State, str]]=..., errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., steps: _Optional[_Iterable[_Union[DiskMigrationStep, _Mapping]]]=...) -> None:
        ...

class DiskMigrationJobTargetDetails(_message.Message):
    __slots__ = ('target_disk', 'target_project', 'labels', 'encryption')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TARGET_DISK_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    target_disk: ComputeEngineDisk
    target_project: str
    labels: _containers.ScalarMap[str, str]
    encryption: Encryption

    def __init__(self, target_disk: _Optional[_Union[ComputeEngineDisk, _Mapping]]=..., target_project: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., encryption: _Optional[_Union[Encryption, _Mapping]]=...) -> None:
        ...

class DiskMigrationStep(_message.Message):
    __slots__ = ('creating_source_disk_snapshot', 'copying_source_disk_snapshot', 'provisioning_target_disk', 'start_time', 'end_time')
    CREATING_SOURCE_DISK_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    COPYING_SOURCE_DISK_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_TARGET_DISK_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    creating_source_disk_snapshot: CreatingSourceDiskSnapshotStep
    copying_source_disk_snapshot: CopyingSourceDiskSnapshotStep
    provisioning_target_disk: ProvisioningTargetDiskStep
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, creating_source_disk_snapshot: _Optional[_Union[CreatingSourceDiskSnapshotStep, _Mapping]]=..., copying_source_disk_snapshot: _Optional[_Union[CopyingSourceDiskSnapshotStep, _Mapping]]=..., provisioning_target_disk: _Optional[_Union[ProvisioningTargetDiskStep, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreatingSourceDiskSnapshotStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CopyingSourceDiskSnapshotStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ProvisioningTargetDiskStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ComputeEngineDisk(_message.Message):
    __slots__ = ('disk_id', 'zone', 'replica_zones', 'disk_type')
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ZONES_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    disk_id: str
    zone: str
    replica_zones: _containers.RepeatedScalarFieldContainer[str]
    disk_type: ComputeEngineDiskType

    def __init__(self, disk_id: _Optional[str]=..., zone: _Optional[str]=..., replica_zones: _Optional[_Iterable[str]]=..., disk_type: _Optional[_Union[ComputeEngineDiskType, str]]=...) -> None:
        ...

class AwsSourceDiskDetails(_message.Message):
    __slots__ = ('volume_id', 'size_gib', 'disk_type', 'tags')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AwsSourceDiskDetails.Type]
        GP2: _ClassVar[AwsSourceDiskDetails.Type]
        GP3: _ClassVar[AwsSourceDiskDetails.Type]
        IO1: _ClassVar[AwsSourceDiskDetails.Type]
        IO2: _ClassVar[AwsSourceDiskDetails.Type]
        ST1: _ClassVar[AwsSourceDiskDetails.Type]
        SC1: _ClassVar[AwsSourceDiskDetails.Type]
        STANDARD: _ClassVar[AwsSourceDiskDetails.Type]
    TYPE_UNSPECIFIED: AwsSourceDiskDetails.Type
    GP2: AwsSourceDiskDetails.Type
    GP3: AwsSourceDiskDetails.Type
    IO1: AwsSourceDiskDetails.Type
    IO2: AwsSourceDiskDetails.Type
    ST1: AwsSourceDiskDetails.Type
    SC1: AwsSourceDiskDetails.Type
    STANDARD: AwsSourceDiskDetails.Type

    class TagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    volume_id: str
    size_gib: int
    disk_type: AwsSourceDiskDetails.Type
    tags: _containers.ScalarMap[str, str]

    def __init__(self, volume_id: _Optional[str]=..., size_gib: _Optional[int]=..., disk_type: _Optional[_Union[AwsSourceDiskDetails.Type, str]]=..., tags: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class CreateDiskMigrationJobRequest(_message.Message):
    __slots__ = ('parent', 'disk_migration_job_id', 'disk_migration_job', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISK_MIGRATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_MIGRATION_JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    disk_migration_job_id: str
    disk_migration_job: DiskMigrationJob
    request_id: str

    def __init__(self, parent: _Optional[str]=..., disk_migration_job_id: _Optional[str]=..., disk_migration_job: _Optional[_Union[DiskMigrationJob, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListDiskMigrationJobsRequest(_message.Message):
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

class ListDiskMigrationJobsResponse(_message.Message):
    __slots__ = ('disk_migration_jobs', 'next_page_token', 'unreachable')
    DISK_MIGRATION_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    disk_migration_jobs: _containers.RepeatedCompositeFieldContainer[DiskMigrationJob]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, disk_migration_jobs: _Optional[_Iterable[_Union[DiskMigrationJob, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDiskMigrationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDiskMigrationJobRequest(_message.Message):
    __slots__ = ('update_mask', 'disk_migration_job', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DISK_MIGRATION_JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    disk_migration_job: DiskMigrationJob
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., disk_migration_job: _Optional[_Union[DiskMigrationJob, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteDiskMigrationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RunDiskMigrationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RunDiskMigrationJobResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CancelDiskMigrationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelDiskMigrationJobResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...