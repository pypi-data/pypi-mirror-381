from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.financialservices.v1 import bigquery_destination_pb2 as _bigquery_destination_pb2
from google.cloud.financialservices.v1 import line_of_business_pb2 as _line_of_business_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EngineConfig(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'state', 'engine_version', 'tuning', 'performance_target', 'line_of_business', 'hyperparameter_source_type', 'hyperparameter_source')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[EngineConfig.State]
        CREATING: _ClassVar[EngineConfig.State]
        ACTIVE: _ClassVar[EngineConfig.State]
        UPDATING: _ClassVar[EngineConfig.State]
        DELETING: _ClassVar[EngineConfig.State]
    STATE_UNSPECIFIED: EngineConfig.State
    CREATING: EngineConfig.State
    ACTIVE: EngineConfig.State
    UPDATING: EngineConfig.State
    DELETING: EngineConfig.State

    class HyperparameterSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HYPERPARAMETER_SOURCE_TYPE_UNSPECIFIED: _ClassVar[EngineConfig.HyperparameterSourceType]
        TUNING: _ClassVar[EngineConfig.HyperparameterSourceType]
        INHERITED: _ClassVar[EngineConfig.HyperparameterSourceType]
    HYPERPARAMETER_SOURCE_TYPE_UNSPECIFIED: EngineConfig.HyperparameterSourceType
    TUNING: EngineConfig.HyperparameterSourceType
    INHERITED: EngineConfig.HyperparameterSourceType

    class Tuning(_message.Message):
        __slots__ = ('primary_dataset', 'end_time')
        PRIMARY_DATASET_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        primary_dataset: str
        end_time: _timestamp_pb2.Timestamp

        def __init__(self, primary_dataset: _Optional[str]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class PerformanceTarget(_message.Message):
        __slots__ = ('party_investigations_per_period_hint',)
        PARTY_INVESTIGATIONS_PER_PERIOD_HINT_FIELD_NUMBER: _ClassVar[int]
        party_investigations_per_period_hint: int

        def __init__(self, party_investigations_per_period_hint: _Optional[int]=...) -> None:
            ...

    class HyperparameterSource(_message.Message):
        __slots__ = ('source_engine_config', 'source_engine_version')
        SOURCE_ENGINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ENGINE_VERSION_FIELD_NUMBER: _ClassVar[int]
        source_engine_config: str
        source_engine_version: str

        def __init__(self, source_engine_config: _Optional[str]=..., source_engine_version: _Optional[str]=...) -> None:
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
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ENGINE_VERSION_FIELD_NUMBER: _ClassVar[int]
    TUNING_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_TARGET_FIELD_NUMBER: _ClassVar[int]
    LINE_OF_BUSINESS_FIELD_NUMBER: _ClassVar[int]
    HYPERPARAMETER_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HYPERPARAMETER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: EngineConfig.State
    engine_version: str
    tuning: EngineConfig.Tuning
    performance_target: EngineConfig.PerformanceTarget
    line_of_business: _line_of_business_pb2.LineOfBusiness
    hyperparameter_source_type: EngineConfig.HyperparameterSourceType
    hyperparameter_source: EngineConfig.HyperparameterSource

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[EngineConfig.State, str]]=..., engine_version: _Optional[str]=..., tuning: _Optional[_Union[EngineConfig.Tuning, _Mapping]]=..., performance_target: _Optional[_Union[EngineConfig.PerformanceTarget, _Mapping]]=..., line_of_business: _Optional[_Union[_line_of_business_pb2.LineOfBusiness, str]]=..., hyperparameter_source_type: _Optional[_Union[EngineConfig.HyperparameterSourceType, str]]=..., hyperparameter_source: _Optional[_Union[EngineConfig.HyperparameterSource, _Mapping]]=...) -> None:
        ...

class ListEngineConfigsRequest(_message.Message):
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

class ListEngineConfigsResponse(_message.Message):
    __slots__ = ('engine_configs', 'next_page_token', 'unreachable')
    ENGINE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    engine_configs: _containers.RepeatedCompositeFieldContainer[EngineConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, engine_configs: _Optional[_Iterable[_Union[EngineConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetEngineConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEngineConfigRequest(_message.Message):
    __slots__ = ('parent', 'engine_config_id', 'engine_config', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENGINE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    engine_config_id: str
    engine_config: EngineConfig
    request_id: str

    def __init__(self, parent: _Optional[str]=..., engine_config_id: _Optional[str]=..., engine_config: _Optional[_Union[EngineConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateEngineConfigRequest(_message.Message):
    __slots__ = ('update_mask', 'engine_config', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ENGINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    engine_config: EngineConfig
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., engine_config: _Optional[_Union[EngineConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteEngineConfigRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ExportEngineConfigMetadataRequest(_message.Message):
    __slots__ = ('engine_config', 'structured_metadata_destination')
    ENGINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_METADATA_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    engine_config: str
    structured_metadata_destination: _bigquery_destination_pb2.BigQueryDestination

    def __init__(self, engine_config: _Optional[str]=..., structured_metadata_destination: _Optional[_Union[_bigquery_destination_pb2.BigQueryDestination, _Mapping]]=...) -> None:
        ...

class ExportEngineConfigMetadataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...