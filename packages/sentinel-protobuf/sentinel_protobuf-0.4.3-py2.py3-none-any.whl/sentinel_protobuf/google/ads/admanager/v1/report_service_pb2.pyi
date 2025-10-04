from google.ads.admanager.v1 import report_messages_pb2 as _report_messages_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RunReportRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RunReportMetadata(_message.Message):
    __slots__ = ('percent_complete', 'report')
    PERCENT_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    percent_complete: int
    report: str

    def __init__(self, percent_complete: _Optional[int]=..., report: _Optional[str]=...) -> None:
        ...

class RunReportResponse(_message.Message):
    __slots__ = ('report_result',)
    REPORT_RESULT_FIELD_NUMBER: _ClassVar[int]
    report_result: str

    def __init__(self, report_result: _Optional[str]=...) -> None:
        ...

class GetReportRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListReportsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'skip')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    skip: int

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., skip: _Optional[int]=...) -> None:
        ...

class ListReportsResponse(_message.Message):
    __slots__ = ('reports', 'next_page_token', 'total_size')
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[_report_messages_pb2.Report]
    next_page_token: str
    total_size: int

    def __init__(self, reports: _Optional[_Iterable[_Union[_report_messages_pb2.Report, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class CreateReportRequest(_message.Message):
    __slots__ = ('parent', 'report')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    report: _report_messages_pb2.Report

    def __init__(self, parent: _Optional[str]=..., report: _Optional[_Union[_report_messages_pb2.Report, _Mapping]]=...) -> None:
        ...

class UpdateReportRequest(_message.Message):
    __slots__ = ('report', 'update_mask')
    REPORT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    report: _report_messages_pb2.Report
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, report: _Optional[_Union[_report_messages_pb2.Report, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class FetchReportResultRowsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchReportResultRowsResponse(_message.Message):
    __slots__ = ('rows', 'run_time', 'date_ranges', 'comparison_date_ranges', 'total_row_count', 'next_page_token')
    ROWS_FIELD_NUMBER: _ClassVar[int]
    RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGES_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_DATE_RANGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[_report_messages_pb2.Report.DataTable.Row]
    run_time: _timestamp_pb2.Timestamp
    date_ranges: _containers.RepeatedCompositeFieldContainer[_report_messages_pb2.Report.DateRange.FixedDateRange]
    comparison_date_ranges: _containers.RepeatedCompositeFieldContainer[_report_messages_pb2.Report.DateRange.FixedDateRange]
    total_row_count: int
    next_page_token: str

    def __init__(self, rows: _Optional[_Iterable[_Union[_report_messages_pb2.Report.DataTable.Row, _Mapping]]]=..., run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., date_ranges: _Optional[_Iterable[_Union[_report_messages_pb2.Report.DateRange.FixedDateRange, _Mapping]]]=..., comparison_date_ranges: _Optional[_Iterable[_Union[_report_messages_pb2.Report.DateRange.FixedDateRange, _Mapping]]]=..., total_row_count: _Optional[int]=..., next_page_token: _Optional[str]=...) -> None:
        ...