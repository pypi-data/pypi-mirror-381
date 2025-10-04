from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.hypercomputecluster.v1alpha import operation_metadata_pb2 as _operation_metadata_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[State]
    STATE_ACTIVE: _ClassVar[State]
    STATE_COMPLETED: _ClassVar[State]
    STATE_FAILED: _ClassVar[State]
STATE_UNSPECIFIED: State
STATE_ACTIVE: State
STATE_COMPLETED: State
STATE_FAILED: State

class MachineLearningRun(_message.Message):
    __slots__ = ('name', 'display_name', 'run_set', 'etag', 'configs', 'tools', 'metrics', 'labels', 'state', 'create_time', 'update_time', 'artifacts', 'orchestrator', 'workload_details', 'run_phase', 'error_details', 'end_time')

    class Orchestrator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORCHESTRATOR_UNSPECIFIED: _ClassVar[MachineLearningRun.Orchestrator]
        GCE: _ClassVar[MachineLearningRun.Orchestrator]
        GKE: _ClassVar[MachineLearningRun.Orchestrator]
        SLURM: _ClassVar[MachineLearningRun.Orchestrator]
    ORCHESTRATOR_UNSPECIFIED: MachineLearningRun.Orchestrator
    GCE: MachineLearningRun.Orchestrator
    GKE: MachineLearningRun.Orchestrator
    SLURM: MachineLearningRun.Orchestrator

    class RunPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RUN_PHASE_UNSPECIFIED: _ClassVar[MachineLearningRun.RunPhase]
        ACTIVE: _ClassVar[MachineLearningRun.RunPhase]
        COMPLETED: _ClassVar[MachineLearningRun.RunPhase]
        FAILED: _ClassVar[MachineLearningRun.RunPhase]
    RUN_PHASE_UNSPECIFIED: MachineLearningRun.RunPhase
    ACTIVE: MachineLearningRun.RunPhase
    COMPLETED: MachineLearningRun.RunPhase
    FAILED: MachineLearningRun.RunPhase

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RUN_SET_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RUN_PHASE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    run_set: str
    etag: str
    configs: Configs
    tools: _containers.RepeatedCompositeFieldContainer[Tool]
    metrics: Metrics
    labels: _containers.ScalarMap[str, str]
    state: State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    artifacts: Artifacts
    orchestrator: MachineLearningRun.Orchestrator
    workload_details: WorkloadDetails
    run_phase: MachineLearningRun.RunPhase
    error_details: str
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., run_set: _Optional[str]=..., etag: _Optional[str]=..., configs: _Optional[_Union[Configs, _Mapping]]=..., tools: _Optional[_Iterable[_Union[Tool, _Mapping]]]=..., metrics: _Optional[_Union[Metrics, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., artifacts: _Optional[_Union[Artifacts, _Mapping]]=..., orchestrator: _Optional[_Union[MachineLearningRun.Orchestrator, str]]=..., workload_details: _Optional[_Union[WorkloadDetails, _Mapping]]=..., run_phase: _Optional[_Union[MachineLearningRun.RunPhase, str]]=..., error_details: _Optional[str]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateMachineLearningRunRequest(_message.Message):
    __slots__ = ('parent', 'machine_learning_run', 'machine_learning_run_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_LEARNING_RUN_FIELD_NUMBER: _ClassVar[int]
    MACHINE_LEARNING_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    machine_learning_run: MachineLearningRun
    machine_learning_run_id: str

    def __init__(self, parent: _Optional[str]=..., machine_learning_run: _Optional[_Union[MachineLearningRun, _Mapping]]=..., machine_learning_run_id: _Optional[str]=...) -> None:
        ...

class UpdateMachineLearningRunRequest(_message.Message):
    __slots__ = ('machine_learning_run', 'update_mask')
    MACHINE_LEARNING_RUN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    machine_learning_run: MachineLearningRun
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, machine_learning_run: _Optional[_Union[MachineLearningRun, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteMachineLearningRunRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class GetMachineLearningRunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListMachineLearningRunsRequest(_message.Message):
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

class ListMachineLearningRunsResponse(_message.Message):
    __slots__ = ('machine_learning_runs', 'next_page_token')
    MACHINE_LEARNING_RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    machine_learning_runs: _containers.RepeatedCompositeFieldContainer[MachineLearningRun]
    next_page_token: str

    def __init__(self, machine_learning_runs: _Optional[_Iterable[_Union[MachineLearningRun, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListProfileSessionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProfileSessionsResponse(_message.Message):
    __slots__ = ('profile_sessions', 'next_page_token')
    PROFILE_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    profile_sessions: _containers.RepeatedCompositeFieldContainer[ProfileSession]
    next_page_token: str

    def __init__(self, profile_sessions: _Optional[_Iterable[_Union[ProfileSession, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetProfileSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ProfileSession(_message.Message):
    __slots__ = ('name', 'gcs_path', 'create_time', 'dashboard_url')
    NAME_FIELD_NUMBER: _ClassVar[int]
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    gcs_path: str
    create_time: _timestamp_pb2.Timestamp
    dashboard_url: str

    def __init__(self, name: _Optional[str]=..., gcs_path: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., dashboard_url: _Optional[str]=...) -> None:
        ...

class Configs(_message.Message):
    __slots__ = ('user_configs', 'software_configs', 'hardware_configs')

    class UserConfigsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class SoftwareConfigsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class HardwareConfigsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    USER_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    user_configs: _containers.ScalarMap[str, str]
    software_configs: _containers.ScalarMap[str, str]
    hardware_configs: _containers.ScalarMap[str, str]

    def __init__(self, user_configs: _Optional[_Mapping[str, str]]=..., software_configs: _Optional[_Mapping[str, str]]=..., hardware_configs: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class Metrics(_message.Message):
    __slots__ = ('avg_step', 'avg_mfu', 'avg_throughput', 'avg_latency')
    AVG_STEP_FIELD_NUMBER: _ClassVar[int]
    AVG_MFU_FIELD_NUMBER: _ClassVar[int]
    AVG_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    AVG_LATENCY_FIELD_NUMBER: _ClassVar[int]
    avg_step: _duration_pb2.Duration
    avg_mfu: float
    avg_throughput: float
    avg_latency: _duration_pb2.Duration

    def __init__(self, avg_step: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., avg_mfu: _Optional[float]=..., avg_throughput: _Optional[float]=..., avg_latency: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class Artifacts(_message.Message):
    __slots__ = ('gcs_path',)
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    gcs_path: str

    def __init__(self, gcs_path: _Optional[str]=...) -> None:
        ...

class Tool(_message.Message):
    __slots__ = ('xprof',)
    XPROF_FIELD_NUMBER: _ClassVar[int]
    xprof: Xprof

    def __init__(self, xprof: _Optional[_Union[Xprof, _Mapping]]=...) -> None:
        ...

class WorkloadDetails(_message.Message):
    __slots__ = ('gke',)
    GKE_FIELD_NUMBER: _ClassVar[int]
    gke: GKEWorkloadDetails

    def __init__(self, gke: _Optional[_Union[GKEWorkloadDetails, _Mapping]]=...) -> None:
        ...

class GKEWorkloadDetails(_message.Message):
    __slots__ = ('id', 'kind', 'cluster', 'namespace', 'parent_workload', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: str
    cluster: str
    namespace: str
    parent_workload: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, id: _Optional[str]=..., kind: _Optional[str]=..., cluster: _Optional[str]=..., namespace: _Optional[str]=..., parent_workload: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class Xprof(_message.Message):
    __slots__ = ('session_id',)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str

    def __init__(self, session_id: _Optional[str]=...) -> None:
        ...