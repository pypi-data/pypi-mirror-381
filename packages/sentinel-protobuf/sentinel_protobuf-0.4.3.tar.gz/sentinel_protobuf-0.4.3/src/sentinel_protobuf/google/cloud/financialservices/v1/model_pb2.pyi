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

class Model(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'state', 'engine_version', 'engine_config', 'primary_dataset', 'end_time', 'line_of_business')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Model.State]
        CREATING: _ClassVar[Model.State]
        ACTIVE: _ClassVar[Model.State]
        UPDATING: _ClassVar[Model.State]
        DELETING: _ClassVar[Model.State]
    STATE_UNSPECIFIED: Model.State
    CREATING: Model.State
    ACTIVE: Model.State
    UPDATING: Model.State
    DELETING: Model.State

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
    ENGINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_DATASET_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LINE_OF_BUSINESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Model.State
    engine_version: str
    engine_config: str
    primary_dataset: str
    end_time: _timestamp_pb2.Timestamp
    line_of_business: _line_of_business_pb2.LineOfBusiness

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Model.State, str]]=..., engine_version: _Optional[str]=..., engine_config: _Optional[str]=..., primary_dataset: _Optional[str]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., line_of_business: _Optional[_Union[_line_of_business_pb2.LineOfBusiness, str]]=...) -> None:
        ...

class ListModelsRequest(_message.Message):
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

class ListModelsResponse(_message.Message):
    __slots__ = ('models', 'next_page_token', 'unreachable')
    MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetModelRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateModelRequest(_message.Message):
    __slots__ = ('parent', 'model_id', 'model', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model_id: str
    model: Model
    request_id: str

    def __init__(self, parent: _Optional[str]=..., model_id: _Optional[str]=..., model: _Optional[_Union[Model, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateModelRequest(_message.Message):
    __slots__ = ('update_mask', 'model', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    model: Model
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., model: _Optional[_Union[Model, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteModelRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ExportModelMetadataRequest(_message.Message):
    __slots__ = ('model', 'structured_metadata_destination')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_METADATA_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    model: str
    structured_metadata_destination: _bigquery_destination_pb2.BigQueryDestination

    def __init__(self, model: _Optional[str]=..., structured_metadata_destination: _Optional[_Union[_bigquery_destination_pb2.BigQueryDestination, _Mapping]]=...) -> None:
        ...

class ExportModelMetadataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...