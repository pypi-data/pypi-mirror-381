from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FetchModelsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchModelsResponse(_message.Message):
    __slots__ = ('models', 'next_page_token')
    MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str

    def __init__(self, models: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class FetchModelServersRequest(_message.Message):
    __slots__ = ('model', 'page_size', 'page_token')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model: str
    page_size: int
    page_token: str

    def __init__(self, model: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchModelServersResponse(_message.Message):
    __slots__ = ('model_servers', 'next_page_token')
    MODEL_SERVERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_servers: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str

    def __init__(self, model_servers: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class FetchModelServerVersionsRequest(_message.Message):
    __slots__ = ('model', 'model_server', 'page_size', 'page_token')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_SERVER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model: str
    model_server: str
    page_size: int
    page_token: str

    def __init__(self, model: _Optional[str]=..., model_server: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchModelServerVersionsResponse(_message.Message):
    __slots__ = ('model_server_versions', 'next_page_token')
    MODEL_SERVER_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_server_versions: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str

    def __init__(self, model_server_versions: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class FetchBenchmarkingDataRequest(_message.Message):
    __slots__ = ('model_server_info', 'instance_type', 'pricing_model')
    MODEL_SERVER_INFO_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICING_MODEL_FIELD_NUMBER: _ClassVar[int]
    model_server_info: ModelServerInfo
    instance_type: str
    pricing_model: str

    def __init__(self, model_server_info: _Optional[_Union[ModelServerInfo, _Mapping]]=..., instance_type: _Optional[str]=..., pricing_model: _Optional[str]=...) -> None:
        ...

class FetchBenchmarkingDataResponse(_message.Message):
    __slots__ = ('profile',)
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    profile: _containers.RepeatedCompositeFieldContainer[Profile]

    def __init__(self, profile: _Optional[_Iterable[_Union[Profile, _Mapping]]]=...) -> None:
        ...

class FetchProfilesRequest(_message.Message):
    __slots__ = ('model', 'model_server', 'model_server_version', 'performance_requirements', 'page_size', 'page_token')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_SERVER_FIELD_NUMBER: _ClassVar[int]
    MODEL_SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model: str
    model_server: str
    model_server_version: str
    performance_requirements: PerformanceRequirements
    page_size: int
    page_token: str

    def __init__(self, model: _Optional[str]=..., model_server: _Optional[str]=..., model_server_version: _Optional[str]=..., performance_requirements: _Optional[_Union[PerformanceRequirements, _Mapping]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class PerformanceRequirements(_message.Message):
    __slots__ = ('target_ntpot_milliseconds', 'target_ttft_milliseconds', 'target_cost')
    TARGET_NTPOT_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    TARGET_TTFT_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    TARGET_COST_FIELD_NUMBER: _ClassVar[int]
    target_ntpot_milliseconds: int
    target_ttft_milliseconds: int
    target_cost: Cost

    def __init__(self, target_ntpot_milliseconds: _Optional[int]=..., target_ttft_milliseconds: _Optional[int]=..., target_cost: _Optional[_Union[Cost, _Mapping]]=...) -> None:
        ...

class Amount(_message.Message):
    __slots__ = ('units', 'nanos')
    UNITS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    units: int
    nanos: int

    def __init__(self, units: _Optional[int]=..., nanos: _Optional[int]=...) -> None:
        ...

class Cost(_message.Message):
    __slots__ = ('cost_per_million_output_tokens', 'cost_per_million_input_tokens', 'pricing_model', 'output_input_cost_ratio')
    COST_PER_MILLION_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COST_PER_MILLION_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    PRICING_MODEL_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_INPUT_COST_RATIO_FIELD_NUMBER: _ClassVar[int]
    cost_per_million_output_tokens: Amount
    cost_per_million_input_tokens: Amount
    pricing_model: str
    output_input_cost_ratio: float

    def __init__(self, cost_per_million_output_tokens: _Optional[_Union[Amount, _Mapping]]=..., cost_per_million_input_tokens: _Optional[_Union[Amount, _Mapping]]=..., pricing_model: _Optional[str]=..., output_input_cost_ratio: _Optional[float]=...) -> None:
        ...

class TokensPerSecondRange(_message.Message):
    __slots__ = ('min', 'max')
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: int
    max: int

    def __init__(self, min: _Optional[int]=..., max: _Optional[int]=...) -> None:
        ...

class MillisecondRange(_message.Message):
    __slots__ = ('min', 'max')
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: int
    max: int

    def __init__(self, min: _Optional[int]=..., max: _Optional[int]=...) -> None:
        ...

class PerformanceRange(_message.Message):
    __slots__ = ('throughput_output_range', 'ttft_range', 'ntpot_range')
    THROUGHPUT_OUTPUT_RANGE_FIELD_NUMBER: _ClassVar[int]
    TTFT_RANGE_FIELD_NUMBER: _ClassVar[int]
    NTPOT_RANGE_FIELD_NUMBER: _ClassVar[int]
    throughput_output_range: TokensPerSecondRange
    ttft_range: MillisecondRange
    ntpot_range: MillisecondRange

    def __init__(self, throughput_output_range: _Optional[_Union[TokensPerSecondRange, _Mapping]]=..., ttft_range: _Optional[_Union[MillisecondRange, _Mapping]]=..., ntpot_range: _Optional[_Union[MillisecondRange, _Mapping]]=...) -> None:
        ...

class FetchProfilesResponse(_message.Message):
    __slots__ = ('profile', 'performance_range', 'comments', 'next_page_token')
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_RANGE_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    profile: _containers.RepeatedCompositeFieldContainer[Profile]
    performance_range: PerformanceRange
    comments: str
    next_page_token: str

    def __init__(self, profile: _Optional[_Iterable[_Union[Profile, _Mapping]]]=..., performance_range: _Optional[_Union[PerformanceRange, _Mapping]]=..., comments: _Optional[str]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ModelServerInfo(_message.Message):
    __slots__ = ('model', 'model_server', 'model_server_version')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_SERVER_FIELD_NUMBER: _ClassVar[int]
    MODEL_SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    model: str
    model_server: str
    model_server_version: str

    def __init__(self, model: _Optional[str]=..., model_server: _Optional[str]=..., model_server_version: _Optional[str]=...) -> None:
        ...

class ResourcesUsed(_message.Message):
    __slots__ = ('accelerator_count',)
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    accelerator_count: int

    def __init__(self, accelerator_count: _Optional[int]=...) -> None:
        ...

class PerformanceStats(_message.Message):
    __slots__ = ('queries_per_second', 'output_tokens_per_second', 'ntpot_milliseconds', 'ttft_milliseconds', 'cost')
    QUERIES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    NTPOT_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    TTFT_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    queries_per_second: float
    output_tokens_per_second: int
    ntpot_milliseconds: int
    ttft_milliseconds: int
    cost: _containers.RepeatedCompositeFieldContainer[Cost]

    def __init__(self, queries_per_second: _Optional[float]=..., output_tokens_per_second: _Optional[int]=..., ntpot_milliseconds: _Optional[int]=..., ttft_milliseconds: _Optional[int]=..., cost: _Optional[_Iterable[_Union[Cost, _Mapping]]]=...) -> None:
        ...

class Profile(_message.Message):
    __slots__ = ('model_server_info', 'accelerator_type', 'tpu_topology', 'instance_type', 'resources_used', 'performance_stats')
    MODEL_SERVER_INFO_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    TPU_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_USED_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_STATS_FIELD_NUMBER: _ClassVar[int]
    model_server_info: ModelServerInfo
    accelerator_type: str
    tpu_topology: str
    instance_type: str
    resources_used: ResourcesUsed
    performance_stats: _containers.RepeatedCompositeFieldContainer[PerformanceStats]

    def __init__(self, model_server_info: _Optional[_Union[ModelServerInfo, _Mapping]]=..., accelerator_type: _Optional[str]=..., tpu_topology: _Optional[str]=..., instance_type: _Optional[str]=..., resources_used: _Optional[_Union[ResourcesUsed, _Mapping]]=..., performance_stats: _Optional[_Iterable[_Union[PerformanceStats, _Mapping]]]=...) -> None:
        ...

class GenerateOptimizedManifestRequest(_message.Message):
    __slots__ = ('model_server_info', 'accelerator_type', 'kubernetes_namespace', 'performance_requirements', 'storage_config')
    MODEL_SERVER_INFO_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    model_server_info: ModelServerInfo
    accelerator_type: str
    kubernetes_namespace: str
    performance_requirements: PerformanceRequirements
    storage_config: StorageConfig

    def __init__(self, model_server_info: _Optional[_Union[ModelServerInfo, _Mapping]]=..., accelerator_type: _Optional[str]=..., kubernetes_namespace: _Optional[str]=..., performance_requirements: _Optional[_Union[PerformanceRequirements, _Mapping]]=..., storage_config: _Optional[_Union[StorageConfig, _Mapping]]=...) -> None:
        ...

class KubernetesManifest(_message.Message):
    __slots__ = ('kind', 'api_version', 'content')
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    content: str

    def __init__(self, kind: _Optional[str]=..., api_version: _Optional[str]=..., content: _Optional[str]=...) -> None:
        ...

class GenerateOptimizedManifestResponse(_message.Message):
    __slots__ = ('kubernetes_manifests', 'comments', 'manifest_version')
    KUBERNETES_MANIFESTS_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    kubernetes_manifests: _containers.RepeatedCompositeFieldContainer[KubernetesManifest]
    comments: _containers.RepeatedScalarFieldContainer[str]
    manifest_version: str

    def __init__(self, kubernetes_manifests: _Optional[_Iterable[_Union[KubernetesManifest, _Mapping]]]=..., comments: _Optional[_Iterable[str]]=..., manifest_version: _Optional[str]=...) -> None:
        ...

class StorageConfig(_message.Message):
    __slots__ = ('model_bucket_uri', 'xla_cache_bucket_uri')
    MODEL_BUCKET_URI_FIELD_NUMBER: _ClassVar[int]
    XLA_CACHE_BUCKET_URI_FIELD_NUMBER: _ClassVar[int]
    model_bucket_uri: str
    xla_cache_bucket_uri: str

    def __init__(self, model_bucket_uri: _Optional[str]=..., xla_cache_bucket_uri: _Optional[str]=...) -> None:
        ...