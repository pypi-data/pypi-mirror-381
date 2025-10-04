from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.saasplatform.saasservicemgmt.v1beta1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RolloutAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLLOUT_ACTION_UNSPECIFIED: _ClassVar[RolloutAction]
    ROLLOUT_ACTION_RUN: _ClassVar[RolloutAction]
    ROLLOUT_ACTION_PAUSE: _ClassVar[RolloutAction]
    ROLLOUT_ACTION_CANCEL: _ClassVar[RolloutAction]
ROLLOUT_ACTION_UNSPECIFIED: RolloutAction
ROLLOUT_ACTION_RUN: RolloutAction
ROLLOUT_ACTION_PAUSE: RolloutAction
ROLLOUT_ACTION_CANCEL: RolloutAction

class Rollout(_message.Message):
    __slots__ = ('name', 'release', 'start_time', 'end_time', 'state', 'state_message', 'state_transition_time', 'root_rollout', 'parent_rollout', 'rollout_orchestration_strategy', 'unit_filter', 'rollout_kind', 'stats', 'control', 'labels', 'annotations', 'uid', 'etag', 'create_time', 'update_time')

    class RolloutState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLLOUT_STATE_UNSPECIFIED: _ClassVar[Rollout.RolloutState]
        ROLLOUT_STATE_RUNNING: _ClassVar[Rollout.RolloutState]
        ROLLOUT_STATE_PAUSED: _ClassVar[Rollout.RolloutState]
        ROLLOUT_STATE_SUCCEEDED: _ClassVar[Rollout.RolloutState]
        ROLLOUT_STATE_FAILED: _ClassVar[Rollout.RolloutState]
        ROLLOUT_STATE_CANCELLED: _ClassVar[Rollout.RolloutState]
        ROLLOUT_STATE_WAITING: _ClassVar[Rollout.RolloutState]
        ROLLOUT_STATE_CANCELLING: _ClassVar[Rollout.RolloutState]
        ROLLOUT_STATE_RESUMING: _ClassVar[Rollout.RolloutState]
        ROLLOUT_STATE_PAUSING: _ClassVar[Rollout.RolloutState]
    ROLLOUT_STATE_UNSPECIFIED: Rollout.RolloutState
    ROLLOUT_STATE_RUNNING: Rollout.RolloutState
    ROLLOUT_STATE_PAUSED: Rollout.RolloutState
    ROLLOUT_STATE_SUCCEEDED: Rollout.RolloutState
    ROLLOUT_STATE_FAILED: Rollout.RolloutState
    ROLLOUT_STATE_CANCELLED: Rollout.RolloutState
    ROLLOUT_STATE_WAITING: Rollout.RolloutState
    ROLLOUT_STATE_CANCELLING: Rollout.RolloutState
    ROLLOUT_STATE_RESUMING: Rollout.RolloutState
    ROLLOUT_STATE_PAUSING: Rollout.RolloutState

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
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_TRANSITION_TIME_FIELD_NUMBER: _ClassVar[int]
    ROOT_ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    PARENT_ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_ORCHESTRATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    UNIT_FILTER_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_KIND_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    release: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: Rollout.RolloutState
    state_message: str
    state_transition_time: _timestamp_pb2.Timestamp
    root_rollout: str
    parent_rollout: str
    rollout_orchestration_strategy: str
    unit_filter: str
    rollout_kind: str
    stats: RolloutStats
    control: RolloutControl
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    uid: str
    etag: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., release: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Rollout.RolloutState, str]]=..., state_message: _Optional[str]=..., state_transition_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., root_rollout: _Optional[str]=..., parent_rollout: _Optional[str]=..., rollout_orchestration_strategy: _Optional[str]=..., unit_filter: _Optional[str]=..., rollout_kind: _Optional[str]=..., stats: _Optional[_Union[RolloutStats, _Mapping]]=..., control: _Optional[_Union[RolloutControl, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., etag: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class RolloutKind(_message.Message):
    __slots__ = ('name', 'unit_kind', 'rollout_orchestration_strategy', 'unit_filter', 'update_unit_kind_strategy', 'error_budget', 'labels', 'annotations', 'uid', 'etag', 'create_time', 'update_time')

    class UpdateUnitKindStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UPDATE_UNIT_KIND_STRATEGY_UNSPECIFIED: _ClassVar[RolloutKind.UpdateUnitKindStrategy]
        UPDATE_UNIT_KIND_STRATEGY_ON_START: _ClassVar[RolloutKind.UpdateUnitKindStrategy]
        UPDATE_UNIT_KIND_STRATEGY_NEVER: _ClassVar[RolloutKind.UpdateUnitKindStrategy]
    UPDATE_UNIT_KIND_STRATEGY_UNSPECIFIED: RolloutKind.UpdateUnitKindStrategy
    UPDATE_UNIT_KIND_STRATEGY_ON_START: RolloutKind.UpdateUnitKindStrategy
    UPDATE_UNIT_KIND_STRATEGY_NEVER: RolloutKind.UpdateUnitKindStrategy

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
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_KIND_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_ORCHESTRATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    UNIT_FILTER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_UNIT_KIND_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    ERROR_BUDGET_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    unit_kind: str
    rollout_orchestration_strategy: str
    unit_filter: str
    update_unit_kind_strategy: RolloutKind.UpdateUnitKindStrategy
    error_budget: ErrorBudget
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    uid: str
    etag: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., unit_kind: _Optional[str]=..., rollout_orchestration_strategy: _Optional[str]=..., unit_filter: _Optional[str]=..., update_unit_kind_strategy: _Optional[_Union[RolloutKind.UpdateUnitKindStrategy, str]]=..., error_budget: _Optional[_Union[ErrorBudget, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., etag: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ErrorBudget(_message.Message):
    __slots__ = ('allowed_count', 'allowed_percentage')
    ALLOWED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    allowed_count: int
    allowed_percentage: int

    def __init__(self, allowed_count: _Optional[int]=..., allowed_percentage: _Optional[int]=...) -> None:
        ...

class RolloutStats(_message.Message):
    __slots__ = ('operations_by_state',)
    OPERATIONS_BY_STATE_FIELD_NUMBER: _ClassVar[int]
    operations_by_state: _containers.RepeatedCompositeFieldContainer[_common_pb2.Aggregate]

    def __init__(self, operations_by_state: _Optional[_Iterable[_Union[_common_pb2.Aggregate, _Mapping]]]=...) -> None:
        ...

class RolloutControl(_message.Message):
    __slots__ = ('run_params', 'action')

    class RunRolloutActionParams(_message.Message):
        __slots__ = ('retry_failed_operations',)
        RETRY_FAILED_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        retry_failed_operations: bool

        def __init__(self, retry_failed_operations: bool=...) -> None:
            ...
    RUN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    run_params: RolloutControl.RunRolloutActionParams
    action: RolloutAction

    def __init__(self, run_params: _Optional[_Union[RolloutControl.RunRolloutActionParams, _Mapping]]=..., action: _Optional[_Union[RolloutAction, str]]=...) -> None:
        ...