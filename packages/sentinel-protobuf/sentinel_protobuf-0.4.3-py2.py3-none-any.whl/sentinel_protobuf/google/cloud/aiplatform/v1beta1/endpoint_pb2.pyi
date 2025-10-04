from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import explanation_pb2 as _explanation_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as _machine_resources_pb2
from google.cloud.aiplatform.v1beta1 import service_networking_pb2 as _service_networking_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Endpoint(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'deployed_models', 'traffic_split', 'etag', 'labels', 'create_time', 'update_time', 'encryption_spec', 'network', 'enable_private_service_connect', 'private_service_connect_config', 'model_deployment_monitoring_job', 'predict_request_response_logging_config', 'dedicated_endpoint_enabled', 'dedicated_endpoint_dns', 'client_connection_config', 'satisfies_pzs', 'satisfies_pzi', 'gen_ai_advanced_features_config', 'private_model_server_enabled')

    class TrafficSplitEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...

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
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODELS_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_SPLIT_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRIVATE_SERVICE_CONNECT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_SERVICE_CONNECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODEL_DEPLOYMENT_MONITORING_JOB_FIELD_NUMBER: _ClassVar[int]
    PREDICT_REQUEST_RESPONSE_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_ENDPOINT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_ENDPOINT_DNS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CONNECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    GEN_AI_ADVANCED_FEATURES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_MODEL_SERVER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    deployed_models: _containers.RepeatedCompositeFieldContainer[DeployedModel]
    traffic_split: _containers.ScalarMap[str, int]
    etag: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    network: str
    enable_private_service_connect: bool
    private_service_connect_config: _service_networking_pb2.PrivateServiceConnectConfig
    model_deployment_monitoring_job: str
    predict_request_response_logging_config: PredictRequestResponseLoggingConfig
    dedicated_endpoint_enabled: bool
    dedicated_endpoint_dns: str
    client_connection_config: ClientConnectionConfig
    satisfies_pzs: bool
    satisfies_pzi: bool
    gen_ai_advanced_features_config: GenAiAdvancedFeaturesConfig
    private_model_server_enabled: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., deployed_models: _Optional[_Iterable[_Union[DeployedModel, _Mapping]]]=..., traffic_split: _Optional[_Mapping[str, int]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., network: _Optional[str]=..., enable_private_service_connect: bool=..., private_service_connect_config: _Optional[_Union[_service_networking_pb2.PrivateServiceConnectConfig, _Mapping]]=..., model_deployment_monitoring_job: _Optional[str]=..., predict_request_response_logging_config: _Optional[_Union[PredictRequestResponseLoggingConfig, _Mapping]]=..., dedicated_endpoint_enabled: bool=..., dedicated_endpoint_dns: _Optional[str]=..., client_connection_config: _Optional[_Union[ClientConnectionConfig, _Mapping]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=..., gen_ai_advanced_features_config: _Optional[_Union[GenAiAdvancedFeaturesConfig, _Mapping]]=..., private_model_server_enabled: bool=...) -> None:
        ...

class DeployedModel(_message.Message):
    __slots__ = ('dedicated_resources', 'automatic_resources', 'shared_resources', 'id', 'model', 'model_version_id', 'display_name', 'create_time', 'explanation_spec', 'disable_explanations', 'service_account', 'enable_container_logging', 'disable_container_logging', 'enable_access_logging', 'private_endpoints', 'faster_deployment_config', 'rollout_options', 'status', 'system_labels', 'checkpoint_id', 'speculative_decoding_spec')

    class Status(_message.Message):
        __slots__ = ('message', 'last_update_time', 'available_replica_count')
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
        message: str
        last_update_time: _timestamp_pb2.Timestamp
        available_replica_count: int

        def __init__(self, message: _Optional[str]=..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., available_replica_count: _Optional[int]=...) -> None:
            ...

    class SystemLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DEDICATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SHARED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    DISABLE_EXPLANATIONS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CONTAINER_LOGGING_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CONTAINER_LOGGING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ACCESS_LOGGING_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    FASTER_DEPLOYMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_LABELS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    SPECULATIVE_DECODING_SPEC_FIELD_NUMBER: _ClassVar[int]
    dedicated_resources: _machine_resources_pb2.DedicatedResources
    automatic_resources: _machine_resources_pb2.AutomaticResources
    shared_resources: str
    id: str
    model: str
    model_version_id: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    explanation_spec: _explanation_pb2.ExplanationSpec
    disable_explanations: bool
    service_account: str
    enable_container_logging: bool
    disable_container_logging: bool
    enable_access_logging: bool
    private_endpoints: PrivateEndpoints
    faster_deployment_config: FasterDeploymentConfig
    rollout_options: RolloutOptions
    status: DeployedModel.Status
    system_labels: _containers.ScalarMap[str, str]
    checkpoint_id: str
    speculative_decoding_spec: SpeculativeDecodingSpec

    def __init__(self, dedicated_resources: _Optional[_Union[_machine_resources_pb2.DedicatedResources, _Mapping]]=..., automatic_resources: _Optional[_Union[_machine_resources_pb2.AutomaticResources, _Mapping]]=..., shared_resources: _Optional[str]=..., id: _Optional[str]=..., model: _Optional[str]=..., model_version_id: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., explanation_spec: _Optional[_Union[_explanation_pb2.ExplanationSpec, _Mapping]]=..., disable_explanations: bool=..., service_account: _Optional[str]=..., enable_container_logging: bool=..., disable_container_logging: bool=..., enable_access_logging: bool=..., private_endpoints: _Optional[_Union[PrivateEndpoints, _Mapping]]=..., faster_deployment_config: _Optional[_Union[FasterDeploymentConfig, _Mapping]]=..., rollout_options: _Optional[_Union[RolloutOptions, _Mapping]]=..., status: _Optional[_Union[DeployedModel.Status, _Mapping]]=..., system_labels: _Optional[_Mapping[str, str]]=..., checkpoint_id: _Optional[str]=..., speculative_decoding_spec: _Optional[_Union[SpeculativeDecodingSpec, _Mapping]]=...) -> None:
        ...

class PrivateEndpoints(_message.Message):
    __slots__ = ('predict_http_uri', 'explain_http_uri', 'health_http_uri', 'service_attachment')
    PREDICT_HTTP_URI_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_HTTP_URI_FIELD_NUMBER: _ClassVar[int]
    HEALTH_HTTP_URI_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    predict_http_uri: str
    explain_http_uri: str
    health_http_uri: str
    service_attachment: str

    def __init__(self, predict_http_uri: _Optional[str]=..., explain_http_uri: _Optional[str]=..., health_http_uri: _Optional[str]=..., service_attachment: _Optional[str]=...) -> None:
        ...

class PredictRequestResponseLoggingConfig(_message.Message):
    __slots__ = ('enabled', 'sampling_rate', 'bigquery_destination', 'request_response_logging_schema_version', 'enable_otel_logging')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_RATE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_RESPONSE_LOGGING_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OTEL_LOGGING_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    sampling_rate: float
    bigquery_destination: _io_pb2.BigQueryDestination
    request_response_logging_schema_version: str
    enable_otel_logging: bool

    def __init__(self, enabled: bool=..., sampling_rate: _Optional[float]=..., bigquery_destination: _Optional[_Union[_io_pb2.BigQueryDestination, _Mapping]]=..., request_response_logging_schema_version: _Optional[str]=..., enable_otel_logging: bool=...) -> None:
        ...

class PublisherModelConfig(_message.Message):
    __slots__ = ('logging_config',)
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    logging_config: PredictRequestResponseLoggingConfig

    def __init__(self, logging_config: _Optional[_Union[PredictRequestResponseLoggingConfig, _Mapping]]=...) -> None:
        ...

class ClientConnectionConfig(_message.Message):
    __slots__ = ('inference_timeout',)
    INFERENCE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    inference_timeout: _duration_pb2.Duration

    def __init__(self, inference_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class FasterDeploymentConfig(_message.Message):
    __slots__ = ('fast_tryout_enabled',)
    FAST_TRYOUT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    fast_tryout_enabled: bool

    def __init__(self, fast_tryout_enabled: bool=...) -> None:
        ...

class RolloutOptions(_message.Message):
    __slots__ = ('max_unavailable_replicas', 'max_unavailable_percentage', 'max_surge_replicas', 'max_surge_percentage', 'previous_deployed_model', 'revision_number')
    MAX_UNAVAILABLE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    MAX_UNAVAILABLE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_SURGE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    MAX_SURGE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_DEPLOYED_MODEL_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    max_unavailable_replicas: int
    max_unavailable_percentage: int
    max_surge_replicas: int
    max_surge_percentage: int
    previous_deployed_model: str
    revision_number: int

    def __init__(self, max_unavailable_replicas: _Optional[int]=..., max_unavailable_percentage: _Optional[int]=..., max_surge_replicas: _Optional[int]=..., max_surge_percentage: _Optional[int]=..., previous_deployed_model: _Optional[str]=..., revision_number: _Optional[int]=...) -> None:
        ...

class GenAiAdvancedFeaturesConfig(_message.Message):
    __slots__ = ('rag_config',)

    class RagConfig(_message.Message):
        __slots__ = ('enable_rag',)
        ENABLE_RAG_FIELD_NUMBER: _ClassVar[int]
        enable_rag: bool

        def __init__(self, enable_rag: bool=...) -> None:
            ...
    RAG_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rag_config: GenAiAdvancedFeaturesConfig.RagConfig

    def __init__(self, rag_config: _Optional[_Union[GenAiAdvancedFeaturesConfig.RagConfig, _Mapping]]=...) -> None:
        ...

class SpeculativeDecodingSpec(_message.Message):
    __slots__ = ('draft_model_speculation', 'ngram_speculation', 'speculative_token_count')

    class DraftModelSpeculation(_message.Message):
        __slots__ = ('draft_model',)
        DRAFT_MODEL_FIELD_NUMBER: _ClassVar[int]
        draft_model: str

        def __init__(self, draft_model: _Optional[str]=...) -> None:
            ...

    class NgramSpeculation(_message.Message):
        __slots__ = ('ngram_size',)
        NGRAM_SIZE_FIELD_NUMBER: _ClassVar[int]
        ngram_size: int

        def __init__(self, ngram_size: _Optional[int]=...) -> None:
            ...
    DRAFT_MODEL_SPECULATION_FIELD_NUMBER: _ClassVar[int]
    NGRAM_SPECULATION_FIELD_NUMBER: _ClassVar[int]
    SPECULATIVE_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    draft_model_speculation: SpeculativeDecodingSpec.DraftModelSpeculation
    ngram_speculation: SpeculativeDecodingSpec.NgramSpeculation
    speculative_token_count: int

    def __init__(self, draft_model_speculation: _Optional[_Union[SpeculativeDecodingSpec.DraftModelSpeculation, _Mapping]]=..., ngram_speculation: _Optional[_Union[SpeculativeDecodingSpec.NgramSpeculation, _Mapping]]=..., speculative_token_count: _Optional[int]=...) -> None:
        ...