from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.developerconnect.v1 import developer_connect_pb2 as _developer_connect_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InsightsConfig(_message.Message):
    __slots__ = ('app_hub_application', 'name', 'create_time', 'update_time', 'runtime_configs', 'artifact_configs', 'state', 'annotations', 'labels', 'reconciling', 'errors')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[InsightsConfig.State]
        PENDING: _ClassVar[InsightsConfig.State]
        COMPLETE: _ClassVar[InsightsConfig.State]
        ERROR: _ClassVar[InsightsConfig.State]
    STATE_UNSPECIFIED: InsightsConfig.State
    PENDING: InsightsConfig.State
    COMPLETE: InsightsConfig.State
    ERROR: InsightsConfig.State

    class AnnotationsEntry(_message.Message):
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
    APP_HUB_APPLICATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    app_hub_application: str
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    runtime_configs: _containers.RepeatedCompositeFieldContainer[RuntimeConfig]
    artifact_configs: _containers.RepeatedCompositeFieldContainer[ArtifactConfig]
    state: InsightsConfig.State
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    reconciling: bool
    errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, app_hub_application: _Optional[str]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., runtime_configs: _Optional[_Iterable[_Union[RuntimeConfig, _Mapping]]]=..., artifact_configs: _Optional[_Iterable[_Union[ArtifactConfig, _Mapping]]]=..., state: _Optional[_Union[InsightsConfig.State, str]]=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., reconciling: bool=..., errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...

class RuntimeConfig(_message.Message):
    __slots__ = ('gke_workload', 'app_hub_workload', 'uri', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[RuntimeConfig.State]
        LINKED: _ClassVar[RuntimeConfig.State]
        UNLINKED: _ClassVar[RuntimeConfig.State]
    STATE_UNSPECIFIED: RuntimeConfig.State
    LINKED: RuntimeConfig.State
    UNLINKED: RuntimeConfig.State
    GKE_WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    APP_HUB_WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    gke_workload: GKEWorkload
    app_hub_workload: AppHubWorkload
    uri: str
    state: RuntimeConfig.State

    def __init__(self, gke_workload: _Optional[_Union[GKEWorkload, _Mapping]]=..., app_hub_workload: _Optional[_Union[AppHubWorkload, _Mapping]]=..., uri: _Optional[str]=..., state: _Optional[_Union[RuntimeConfig.State, str]]=...) -> None:
        ...

class GKEWorkload(_message.Message):
    __slots__ = ('cluster', 'deployment')
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    deployment: str

    def __init__(self, cluster: _Optional[str]=..., deployment: _Optional[str]=...) -> None:
        ...

class AppHubWorkload(_message.Message):
    __slots__ = ('workload', 'criticality', 'environment')
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    CRITICALITY_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    workload: str
    criticality: str
    environment: str

    def __init__(self, workload: _Optional[str]=..., criticality: _Optional[str]=..., environment: _Optional[str]=...) -> None:
        ...

class ArtifactConfig(_message.Message):
    __slots__ = ('google_artifact_registry', 'google_artifact_analysis', 'uri')
    GOOGLE_ARTIFACT_REGISTRY_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_ARTIFACT_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    google_artifact_registry: GoogleArtifactRegistry
    google_artifact_analysis: GoogleArtifactAnalysis
    uri: str

    def __init__(self, google_artifact_registry: _Optional[_Union[GoogleArtifactRegistry, _Mapping]]=..., google_artifact_analysis: _Optional[_Union[GoogleArtifactAnalysis, _Mapping]]=..., uri: _Optional[str]=...) -> None:
        ...

class GoogleArtifactAnalysis(_message.Message):
    __slots__ = ('project_id',)
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str

    def __init__(self, project_id: _Optional[str]=...) -> None:
        ...

class GoogleArtifactRegistry(_message.Message):
    __slots__ = ('project_id', 'artifact_registry_package')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_REGISTRY_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    artifact_registry_package: str

    def __init__(self, project_id: _Optional[str]=..., artifact_registry_package: _Optional[str]=...) -> None:
        ...

class CreateInsightsConfigRequest(_message.Message):
    __slots__ = ('parent', 'insights_config_id', 'insights_config', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSIGHTS_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    INSIGHTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    insights_config_id: str
    insights_config: InsightsConfig
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., insights_config_id: _Optional[str]=..., insights_config: _Optional[_Union[InsightsConfig, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class GetInsightsConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListInsightsConfigsRequest(_message.Message):
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

class ListInsightsConfigsResponse(_message.Message):
    __slots__ = ('insights_configs', 'next_page_token', 'unreachable')
    INSIGHTS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    insights_configs: _containers.RepeatedCompositeFieldContainer[InsightsConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, insights_configs: _Optional[_Iterable[_Union[InsightsConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteInsightsConfigRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class UpdateInsightsConfigRequest(_message.Message):
    __slots__ = ('insights_config', 'request_id', 'allow_missing', 'validate_only')
    INSIGHTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    insights_config: InsightsConfig
    request_id: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, insights_config: _Optional[_Union[InsightsConfig, _Mapping]]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...