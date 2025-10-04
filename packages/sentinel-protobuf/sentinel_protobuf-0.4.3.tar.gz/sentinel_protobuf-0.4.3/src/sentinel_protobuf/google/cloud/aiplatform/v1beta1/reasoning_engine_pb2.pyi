from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import env_var_pb2 as _env_var_pb2
from google.cloud.aiplatform.v1beta1 import service_networking_pb2 as _service_networking_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReasoningEngineSpec(_message.Message):
    __slots__ = ('service_account', 'package_spec', 'deployment_spec', 'class_methods', 'agent_framework')

    class PackageSpec(_message.Message):
        __slots__ = ('pickle_object_gcs_uri', 'dependency_files_gcs_uri', 'requirements_gcs_uri', 'python_version')
        PICKLE_OBJECT_GCS_URI_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCY_FILES_GCS_URI_FIELD_NUMBER: _ClassVar[int]
        REQUIREMENTS_GCS_URI_FIELD_NUMBER: _ClassVar[int]
        PYTHON_VERSION_FIELD_NUMBER: _ClassVar[int]
        pickle_object_gcs_uri: str
        dependency_files_gcs_uri: str
        requirements_gcs_uri: str
        python_version: str

        def __init__(self, pickle_object_gcs_uri: _Optional[str]=..., dependency_files_gcs_uri: _Optional[str]=..., requirements_gcs_uri: _Optional[str]=..., python_version: _Optional[str]=...) -> None:
            ...

    class DeploymentSpec(_message.Message):
        __slots__ = ('env', 'secret_env', 'psc_interface_config', 'min_instances', 'max_instances', 'resource_limits', 'container_concurrency')

        class ResourceLimitsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        ENV_FIELD_NUMBER: _ClassVar[int]
        SECRET_ENV_FIELD_NUMBER: _ClassVar[int]
        PSC_INTERFACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        MIN_INSTANCES_FIELD_NUMBER: _ClassVar[int]
        MAX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_LIMITS_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
        env: _containers.RepeatedCompositeFieldContainer[_env_var_pb2.EnvVar]
        secret_env: _containers.RepeatedCompositeFieldContainer[_env_var_pb2.SecretEnvVar]
        psc_interface_config: _service_networking_pb2.PscInterfaceConfig
        min_instances: int
        max_instances: int
        resource_limits: _containers.ScalarMap[str, str]
        container_concurrency: int

        def __init__(self, env: _Optional[_Iterable[_Union[_env_var_pb2.EnvVar, _Mapping]]]=..., secret_env: _Optional[_Iterable[_Union[_env_var_pb2.SecretEnvVar, _Mapping]]]=..., psc_interface_config: _Optional[_Union[_service_networking_pb2.PscInterfaceConfig, _Mapping]]=..., min_instances: _Optional[int]=..., max_instances: _Optional[int]=..., resource_limits: _Optional[_Mapping[str, str]]=..., container_concurrency: _Optional[int]=...) -> None:
            ...
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_SPEC_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_SPEC_FIELD_NUMBER: _ClassVar[int]
    CLASS_METHODS_FIELD_NUMBER: _ClassVar[int]
    AGENT_FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    service_account: str
    package_spec: ReasoningEngineSpec.PackageSpec
    deployment_spec: ReasoningEngineSpec.DeploymentSpec
    class_methods: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    agent_framework: str

    def __init__(self, service_account: _Optional[str]=..., package_spec: _Optional[_Union[ReasoningEngineSpec.PackageSpec, _Mapping]]=..., deployment_spec: _Optional[_Union[ReasoningEngineSpec.DeploymentSpec, _Mapping]]=..., class_methods: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]]=..., agent_framework: _Optional[str]=...) -> None:
        ...

class ReasoningEngine(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'spec', 'create_time', 'update_time', 'etag', 'context_spec', 'encryption_spec')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SPEC_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    spec: ReasoningEngineSpec
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    context_spec: ReasoningEngineContextSpec
    encryption_spec: _encryption_spec_pb2.EncryptionSpec

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., spec: _Optional[_Union[ReasoningEngineSpec, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., context_spec: _Optional[_Union[ReasoningEngineContextSpec, _Mapping]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=...) -> None:
        ...

class ReasoningEngineContextSpec(_message.Message):
    __slots__ = ('memory_bank_config',)

    class MemoryBankConfig(_message.Message):
        __slots__ = ('generation_config', 'similarity_search_config', 'ttl_config')

        class TtlConfig(_message.Message):
            __slots__ = ('default_ttl', 'granular_ttl_config')

            class GranularTtlConfig(_message.Message):
                __slots__ = ('create_ttl', 'generate_created_ttl', 'generate_updated_ttl')
                CREATE_TTL_FIELD_NUMBER: _ClassVar[int]
                GENERATE_CREATED_TTL_FIELD_NUMBER: _ClassVar[int]
                GENERATE_UPDATED_TTL_FIELD_NUMBER: _ClassVar[int]
                create_ttl: _duration_pb2.Duration
                generate_created_ttl: _duration_pb2.Duration
                generate_updated_ttl: _duration_pb2.Duration

                def __init__(self, create_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., generate_created_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., generate_updated_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
                    ...
            DEFAULT_TTL_FIELD_NUMBER: _ClassVar[int]
            GRANULAR_TTL_CONFIG_FIELD_NUMBER: _ClassVar[int]
            default_ttl: _duration_pb2.Duration
            granular_ttl_config: ReasoningEngineContextSpec.MemoryBankConfig.TtlConfig.GranularTtlConfig

            def __init__(self, default_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., granular_ttl_config: _Optional[_Union[ReasoningEngineContextSpec.MemoryBankConfig.TtlConfig.GranularTtlConfig, _Mapping]]=...) -> None:
                ...

        class GenerationConfig(_message.Message):
            __slots__ = ('model',)
            MODEL_FIELD_NUMBER: _ClassVar[int]
            model: str

            def __init__(self, model: _Optional[str]=...) -> None:
                ...

        class SimilaritySearchConfig(_message.Message):
            __slots__ = ('embedding_model',)
            EMBEDDING_MODEL_FIELD_NUMBER: _ClassVar[int]
            embedding_model: str

            def __init__(self, embedding_model: _Optional[str]=...) -> None:
                ...
        GENERATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SIMILARITY_SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
        TTL_CONFIG_FIELD_NUMBER: _ClassVar[int]
        generation_config: ReasoningEngineContextSpec.MemoryBankConfig.GenerationConfig
        similarity_search_config: ReasoningEngineContextSpec.MemoryBankConfig.SimilaritySearchConfig
        ttl_config: ReasoningEngineContextSpec.MemoryBankConfig.TtlConfig

        def __init__(self, generation_config: _Optional[_Union[ReasoningEngineContextSpec.MemoryBankConfig.GenerationConfig, _Mapping]]=..., similarity_search_config: _Optional[_Union[ReasoningEngineContextSpec.MemoryBankConfig.SimilaritySearchConfig, _Mapping]]=..., ttl_config: _Optional[_Union[ReasoningEngineContextSpec.MemoryBankConfig.TtlConfig, _Mapping]]=...) -> None:
            ...
    MEMORY_BANK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    memory_bank_config: ReasoningEngineContextSpec.MemoryBankConfig

    def __init__(self, memory_bank_config: _Optional[_Union[ReasoningEngineContextSpec.MemoryBankConfig, _Mapping]]=...) -> None:
        ...