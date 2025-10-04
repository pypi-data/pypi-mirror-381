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

class BacktestResult(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'state', 'dataset', 'model', 'end_time', 'backtest_periods', 'performance_target', 'line_of_business')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BacktestResult.State]
        CREATING: _ClassVar[BacktestResult.State]
        ACTIVE: _ClassVar[BacktestResult.State]
        UPDATING: _ClassVar[BacktestResult.State]
        DELETING: _ClassVar[BacktestResult.State]
    STATE_UNSPECIFIED: BacktestResult.State
    CREATING: BacktestResult.State
    ACTIVE: BacktestResult.State
    UPDATING: BacktestResult.State
    DELETING: BacktestResult.State

    class PerformanceTarget(_message.Message):
        __slots__ = ('party_investigations_per_period_hint',)
        PARTY_INVESTIGATIONS_PER_PERIOD_HINT_FIELD_NUMBER: _ClassVar[int]
        party_investigations_per_period_hint: int

        def __init__(self, party_investigations_per_period_hint: _Optional[int]=...) -> None:
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
    BACKTEST_PERIODS_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_TARGET_FIELD_NUMBER: _ClassVar[int]
    LINE_OF_BUSINESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: BacktestResult.State
    dataset: str
    model: str
    end_time: _timestamp_pb2.Timestamp
    backtest_periods: int
    performance_target: BacktestResult.PerformanceTarget
    line_of_business: _line_of_business_pb2.LineOfBusiness

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[BacktestResult.State, str]]=..., dataset: _Optional[str]=..., model: _Optional[str]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., backtest_periods: _Optional[int]=..., performance_target: _Optional[_Union[BacktestResult.PerformanceTarget, _Mapping]]=..., line_of_business: _Optional[_Union[_line_of_business_pb2.LineOfBusiness, str]]=...) -> None:
        ...

class ListBacktestResultsRequest(_message.Message):
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

class ListBacktestResultsResponse(_message.Message):
    __slots__ = ('backtest_results', 'next_page_token', 'unreachable')
    BACKTEST_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backtest_results: _containers.RepeatedCompositeFieldContainer[BacktestResult]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, backtest_results: _Optional[_Iterable[_Union[BacktestResult, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetBacktestResultRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateBacktestResultRequest(_message.Message):
    __slots__ = ('parent', 'backtest_result_id', 'backtest_result', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKTEST_RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKTEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backtest_result_id: str
    backtest_result: BacktestResult
    request_id: str

    def __init__(self, parent: _Optional[str]=..., backtest_result_id: _Optional[str]=..., backtest_result: _Optional[_Union[BacktestResult, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateBacktestResultRequest(_message.Message):
    __slots__ = ('update_mask', 'backtest_result', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    BACKTEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    backtest_result: BacktestResult
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., backtest_result: _Optional[_Union[BacktestResult, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteBacktestResultRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ExportBacktestResultMetadataRequest(_message.Message):
    __slots__ = ('backtest_result', 'structured_metadata_destination')
    BACKTEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_METADATA_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    backtest_result: str
    structured_metadata_destination: _bigquery_destination_pb2.BigQueryDestination

    def __init__(self, backtest_result: _Optional[str]=..., structured_metadata_destination: _Optional[_Union[_bigquery_destination_pb2.BigQueryDestination, _Mapping]]=...) -> None:
        ...

class ExportBacktestResultMetadataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...