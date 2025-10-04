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

class PredictionResult(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'state', 'dataset', 'model', 'end_time', 'prediction_periods', 'outputs', 'line_of_business')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PredictionResult.State]
        CREATING: _ClassVar[PredictionResult.State]
        ACTIVE: _ClassVar[PredictionResult.State]
        UPDATING: _ClassVar[PredictionResult.State]
        DELETING: _ClassVar[PredictionResult.State]
    STATE_UNSPECIFIED: PredictionResult.State
    CREATING: PredictionResult.State
    ACTIVE: PredictionResult.State
    UPDATING: PredictionResult.State
    DELETING: PredictionResult.State

    class Outputs(_message.Message):
        __slots__ = ('prediction_destination', 'explainability_destination')
        PREDICTION_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        EXPLAINABILITY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        prediction_destination: _bigquery_destination_pb2.BigQueryDestination
        explainability_destination: _bigquery_destination_pb2.BigQueryDestination

        def __init__(self, prediction_destination: _Optional[_Union[_bigquery_destination_pb2.BigQueryDestination, _Mapping]]=..., explainability_destination: _Optional[_Union[_bigquery_destination_pb2.BigQueryDestination, _Mapping]]=...) -> None:
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
    DATASET_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_PERIODS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    LINE_OF_BUSINESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: PredictionResult.State
    dataset: str
    model: str
    end_time: _timestamp_pb2.Timestamp
    prediction_periods: int
    outputs: PredictionResult.Outputs
    line_of_business: _line_of_business_pb2.LineOfBusiness

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[PredictionResult.State, str]]=..., dataset: _Optional[str]=..., model: _Optional[str]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., prediction_periods: _Optional[int]=..., outputs: _Optional[_Union[PredictionResult.Outputs, _Mapping]]=..., line_of_business: _Optional[_Union[_line_of_business_pb2.LineOfBusiness, str]]=...) -> None:
        ...

class ListPredictionResultsRequest(_message.Message):
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

class ListPredictionResultsResponse(_message.Message):
    __slots__ = ('prediction_results', 'next_page_token', 'unreachable')
    PREDICTION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    prediction_results: _containers.RepeatedCompositeFieldContainer[PredictionResult]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, prediction_results: _Optional[_Iterable[_Union[PredictionResult, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetPredictionResultRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreatePredictionResultRequest(_message.Message):
    __slots__ = ('parent', 'prediction_result_id', 'prediction_result', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    prediction_result_id: str
    prediction_result: PredictionResult
    request_id: str

    def __init__(self, parent: _Optional[str]=..., prediction_result_id: _Optional[str]=..., prediction_result: _Optional[_Union[PredictionResult, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdatePredictionResultRequest(_message.Message):
    __slots__ = ('update_mask', 'prediction_result', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    prediction_result: PredictionResult
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., prediction_result: _Optional[_Union[PredictionResult, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeletePredictionResultRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ExportPredictionResultMetadataRequest(_message.Message):
    __slots__ = ('prediction_result', 'structured_metadata_destination')
    PREDICTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_METADATA_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    prediction_result: str
    structured_metadata_destination: _bigquery_destination_pb2.BigQueryDestination

    def __init__(self, prediction_result: _Optional[str]=..., structured_metadata_destination: _Optional[_Union[_bigquery_destination_pb2.BigQueryDestination, _Mapping]]=...) -> None:
        ...

class ExportPredictionResultMetadataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...