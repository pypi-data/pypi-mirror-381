from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RunFrequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RUN_FREQUENCY_UNSPECIFIED: _ClassVar[RunFrequency]
    LIVE: _ClassVar[RunFrequency]
    HOURLY: _ClassVar[RunFrequency]
    DAILY: _ClassVar[RunFrequency]

class RuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RULE_TYPE_UNSPECIFIED: _ClassVar[RuleType]
    SINGLE_EVENT: _ClassVar[RuleType]
    MULTI_EVENT: _ClassVar[RuleType]

class RuleView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RULE_VIEW_UNSPECIFIED: _ClassVar[RuleView]
    BASIC: _ClassVar[RuleView]
    FULL: _ClassVar[RuleView]
    REVISION_METADATA_ONLY: _ClassVar[RuleView]
RUN_FREQUENCY_UNSPECIFIED: RunFrequency
LIVE: RunFrequency
HOURLY: RunFrequency
DAILY: RunFrequency
RULE_TYPE_UNSPECIFIED: RuleType
SINGLE_EVENT: RuleType
MULTI_EVENT: RuleType
RULE_VIEW_UNSPECIFIED: RuleView
BASIC: RuleView
FULL: RuleView
REVISION_METADATA_ONLY: RuleView

class Rule(_message.Message):
    __slots__ = ('name', 'revision_id', 'display_name', 'text', 'author', 'severity', 'metadata', 'create_time', 'revision_create_time', 'compilation_state', 'type', 'reference_lists', 'allowed_run_frequencies', 'etag', 'scope', 'compilation_diagnostics', 'near_real_time_live_rule_eligible', 'inputs_used')

    class CompilationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPILATION_STATE_UNSPECIFIED: _ClassVar[Rule.CompilationState]
        SUCCEEDED: _ClassVar[Rule.CompilationState]
        FAILED: _ClassVar[Rule.CompilationState]
    COMPILATION_STATE_UNSPECIFIED: Rule.CompilationState
    SUCCEEDED: Rule.CompilationState
    FAILED: Rule.CompilationState

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPILATION_STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_LISTS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_RUN_FREQUENCIES_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    COMPILATION_DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    NEAR_REAL_TIME_LIVE_RULE_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    INPUTS_USED_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str
    display_name: str
    text: str
    author: str
    severity: Severity
    metadata: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    revision_create_time: _timestamp_pb2.Timestamp
    compilation_state: Rule.CompilationState
    type: RuleType
    reference_lists: _containers.RepeatedScalarFieldContainer[str]
    allowed_run_frequencies: _containers.RepeatedScalarFieldContainer[RunFrequency]
    etag: str
    scope: str
    compilation_diagnostics: _containers.RepeatedCompositeFieldContainer[CompilationDiagnostic]
    near_real_time_live_rule_eligible: bool
    inputs_used: InputsUsed

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=..., display_name: _Optional[str]=..., text: _Optional[str]=..., author: _Optional[str]=..., severity: _Optional[_Union[Severity, _Mapping]]=..., metadata: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., compilation_state: _Optional[_Union[Rule.CompilationState, str]]=..., type: _Optional[_Union[RuleType, str]]=..., reference_lists: _Optional[_Iterable[str]]=..., allowed_run_frequencies: _Optional[_Iterable[_Union[RunFrequency, str]]]=..., etag: _Optional[str]=..., scope: _Optional[str]=..., compilation_diagnostics: _Optional[_Iterable[_Union[CompilationDiagnostic, _Mapping]]]=..., near_real_time_live_rule_eligible: bool=..., inputs_used: _Optional[_Union[InputsUsed, _Mapping]]=...) -> None:
        ...

class RuleDeployment(_message.Message):
    __slots__ = ('name', 'enabled', 'alerting', 'archived', 'archive_time', 'run_frequency', 'execution_state', 'producer_rules', 'consumer_rules', 'last_alert_status_change_time')

    class ExecutionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXECUTION_STATE_UNSPECIFIED: _ClassVar[RuleDeployment.ExecutionState]
        DEFAULT: _ClassVar[RuleDeployment.ExecutionState]
        LIMITED: _ClassVar[RuleDeployment.ExecutionState]
        PAUSED: _ClassVar[RuleDeployment.ExecutionState]
    EXECUTION_STATE_UNSPECIFIED: RuleDeployment.ExecutionState
    DEFAULT: RuleDeployment.ExecutionState
    LIMITED: RuleDeployment.ExecutionState
    PAUSED: RuleDeployment.ExecutionState
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALERTING_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    RUN_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_RULES_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_RULES_FIELD_NUMBER: _ClassVar[int]
    LAST_ALERT_STATUS_CHANGE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    enabled: bool
    alerting: bool
    archived: bool
    archive_time: _timestamp_pb2.Timestamp
    run_frequency: RunFrequency
    execution_state: RuleDeployment.ExecutionState
    producer_rules: _containers.RepeatedScalarFieldContainer[str]
    consumer_rules: _containers.RepeatedScalarFieldContainer[str]
    last_alert_status_change_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., enabled: bool=..., alerting: bool=..., archived: bool=..., archive_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., run_frequency: _Optional[_Union[RunFrequency, str]]=..., execution_state: _Optional[_Union[RuleDeployment.ExecutionState, str]]=..., producer_rules: _Optional[_Iterable[str]]=..., consumer_rules: _Optional[_Iterable[str]]=..., last_alert_status_change_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Retrohunt(_message.Message):
    __slots__ = ('name', 'process_interval', 'execution_interval', 'state', 'progress_percentage')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Retrohunt.State]
        RUNNING: _ClassVar[Retrohunt.State]
        DONE: _ClassVar[Retrohunt.State]
        CANCELLED: _ClassVar[Retrohunt.State]
        FAILED: _ClassVar[Retrohunt.State]
    STATE_UNSPECIFIED: Retrohunt.State
    RUNNING: Retrohunt.State
    DONE: Retrohunt.State
    CANCELLED: Retrohunt.State
    FAILED: Retrohunt.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    process_interval: _interval_pb2.Interval
    execution_interval: _interval_pb2.Interval
    state: Retrohunt.State
    progress_percentage: float

    def __init__(self, name: _Optional[str]=..., process_interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., execution_interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., state: _Optional[_Union[Retrohunt.State, str]]=..., progress_percentage: _Optional[float]=...) -> None:
        ...

class CreateRuleRequest(_message.Message):
    __slots__ = ('parent', 'rule')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rule: Rule

    def __init__(self, parent: _Optional[str]=..., rule: _Optional[_Union[Rule, _Mapping]]=...) -> None:
        ...

class GetRuleRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: RuleView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[RuleView, str]]=...) -> None:
        ...

class ListRulesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: RuleView
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[RuleView, str]]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRulesResponse(_message.Message):
    __slots__ = ('rules', 'next_page_token')
    RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    next_page_token: str

    def __init__(self, rules: _Optional[_Iterable[_Union[Rule, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateRuleRequest(_message.Message):
    __slots__ = ('rule', 'update_mask')
    RULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    rule: Rule
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, rule: _Optional[_Union[Rule, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteRuleRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListRuleRevisionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    view: RuleView

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[RuleView, str]]=...) -> None:
        ...

class ListRuleRevisionsResponse(_message.Message):
    __slots__ = ('rules', 'next_page_token')
    RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    next_page_token: str

    def __init__(self, rules: _Optional[_Iterable[_Union[Rule, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateRetrohuntRequest(_message.Message):
    __slots__ = ('parent', 'retrohunt')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RETROHUNT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    retrohunt: Retrohunt

    def __init__(self, parent: _Optional[str]=..., retrohunt: _Optional[_Union[Retrohunt, _Mapping]]=...) -> None:
        ...

class GetRetrohuntRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListRetrohuntsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRetrohuntsResponse(_message.Message):
    __slots__ = ('retrohunts', 'next_page_token')
    RETROHUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    retrohunts: _containers.RepeatedCompositeFieldContainer[Retrohunt]
    next_page_token: str

    def __init__(self, retrohunts: _Optional[_Iterable[_Union[Retrohunt, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRuleDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListRuleDeploymentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRuleDeploymentsResponse(_message.Message):
    __slots__ = ('rule_deployments', 'next_page_token')
    RULE_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rule_deployments: _containers.RepeatedCompositeFieldContainer[RuleDeployment]
    next_page_token: str

    def __init__(self, rule_deployments: _Optional[_Iterable[_Union[RuleDeployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateRuleDeploymentRequest(_message.Message):
    __slots__ = ('rule_deployment', 'update_mask')
    RULE_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    rule_deployment: RuleDeployment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, rule_deployment: _Optional[_Union[RuleDeployment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class CompilationPosition(_message.Message):
    __slots__ = ('start_line', 'start_column', 'end_line', 'end_column')
    START_LINE_FIELD_NUMBER: _ClassVar[int]
    START_COLUMN_FIELD_NUMBER: _ClassVar[int]
    END_LINE_FIELD_NUMBER: _ClassVar[int]
    END_COLUMN_FIELD_NUMBER: _ClassVar[int]
    start_line: int
    start_column: int
    end_line: int
    end_column: int

    def __init__(self, start_line: _Optional[int]=..., start_column: _Optional[int]=..., end_line: _Optional[int]=..., end_column: _Optional[int]=...) -> None:
        ...

class CompilationDiagnostic(_message.Message):
    __slots__ = ('message', 'position', 'severity', 'uri')

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[CompilationDiagnostic.Severity]
        WARNING: _ClassVar[CompilationDiagnostic.Severity]
        ERROR: _ClassVar[CompilationDiagnostic.Severity]
    SEVERITY_UNSPECIFIED: CompilationDiagnostic.Severity
    WARNING: CompilationDiagnostic.Severity
    ERROR: CompilationDiagnostic.Severity
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    message: str
    position: CompilationPosition
    severity: CompilationDiagnostic.Severity
    uri: str

    def __init__(self, message: _Optional[str]=..., position: _Optional[_Union[CompilationPosition, _Mapping]]=..., severity: _Optional[_Union[CompilationDiagnostic.Severity, str]]=..., uri: _Optional[str]=...) -> None:
        ...

class Severity(_message.Message):
    __slots__ = ('display_name',)
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    display_name: str

    def __init__(self, display_name: _Optional[str]=...) -> None:
        ...

class RetrohuntMetadata(_message.Message):
    __slots__ = ('retrohunt', 'execution_interval', 'progress_percentage')
    RETROHUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    retrohunt: str
    execution_interval: _interval_pb2.Interval
    progress_percentage: float

    def __init__(self, retrohunt: _Optional[str]=..., execution_interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., progress_percentage: _Optional[float]=...) -> None:
        ...

class InputsUsed(_message.Message):
    __slots__ = ('uses_udm', 'uses_entity', 'uses_detection')
    USES_UDM_FIELD_NUMBER: _ClassVar[int]
    USES_ENTITY_FIELD_NUMBER: _ClassVar[int]
    USES_DETECTION_FIELD_NUMBER: _ClassVar[int]
    uses_udm: bool
    uses_entity: bool
    uses_detection: bool

    def __init__(self, uses_udm: bool=..., uses_entity: bool=..., uses_detection: bool=...) -> None:
        ...