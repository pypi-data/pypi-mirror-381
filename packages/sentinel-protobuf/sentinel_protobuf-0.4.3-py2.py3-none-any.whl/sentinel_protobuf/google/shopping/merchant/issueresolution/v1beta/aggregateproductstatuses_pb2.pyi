from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListAggregateProductStatusesRequest(_message.Message):
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

class ListAggregateProductStatusesResponse(_message.Message):
    __slots__ = ('aggregate_product_statuses', 'next_page_token')
    AGGREGATE_PRODUCT_STATUSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    aggregate_product_statuses: _containers.RepeatedCompositeFieldContainer[AggregateProductStatus]
    next_page_token: str

    def __init__(self, aggregate_product_statuses: _Optional[_Iterable[_Union[AggregateProductStatus, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class AggregateProductStatus(_message.Message):
    __slots__ = ('name', 'reporting_context', 'country', 'stats', 'item_level_issues')

    class Stats(_message.Message):
        __slots__ = ('active_count', 'pending_count', 'disapproved_count', 'expiring_count')
        ACTIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
        PENDING_COUNT_FIELD_NUMBER: _ClassVar[int]
        DISAPPROVED_COUNT_FIELD_NUMBER: _ClassVar[int]
        EXPIRING_COUNT_FIELD_NUMBER: _ClassVar[int]
        active_count: int
        pending_count: int
        disapproved_count: int
        expiring_count: int

        def __init__(self, active_count: _Optional[int]=..., pending_count: _Optional[int]=..., disapproved_count: _Optional[int]=..., expiring_count: _Optional[int]=...) -> None:
            ...

    class ItemLevelIssue(_message.Message):
        __slots__ = ('code', 'severity', 'resolution', 'attribute', 'description', 'detail', 'documentation_uri', 'product_count')

        class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SEVERITY_UNSPECIFIED: _ClassVar[AggregateProductStatus.ItemLevelIssue.Severity]
            NOT_IMPACTED: _ClassVar[AggregateProductStatus.ItemLevelIssue.Severity]
            DEMOTED: _ClassVar[AggregateProductStatus.ItemLevelIssue.Severity]
            DISAPPROVED: _ClassVar[AggregateProductStatus.ItemLevelIssue.Severity]
        SEVERITY_UNSPECIFIED: AggregateProductStatus.ItemLevelIssue.Severity
        NOT_IMPACTED: AggregateProductStatus.ItemLevelIssue.Severity
        DEMOTED: AggregateProductStatus.ItemLevelIssue.Severity
        DISAPPROVED: AggregateProductStatus.ItemLevelIssue.Severity

        class Resolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RESOLUTION_UNSPECIFIED: _ClassVar[AggregateProductStatus.ItemLevelIssue.Resolution]
            MERCHANT_ACTION: _ClassVar[AggregateProductStatus.ItemLevelIssue.Resolution]
            PENDING_PROCESSING: _ClassVar[AggregateProductStatus.ItemLevelIssue.Resolution]
        RESOLUTION_UNSPECIFIED: AggregateProductStatus.ItemLevelIssue.Resolution
        MERCHANT_ACTION: AggregateProductStatus.ItemLevelIssue.Resolution
        PENDING_PROCESSING: AggregateProductStatus.ItemLevelIssue.Resolution
        CODE_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTATION_URI_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_COUNT_FIELD_NUMBER: _ClassVar[int]
        code: str
        severity: AggregateProductStatus.ItemLevelIssue.Severity
        resolution: AggregateProductStatus.ItemLevelIssue.Resolution
        attribute: str
        description: str
        detail: str
        documentation_uri: str
        product_count: int

        def __init__(self, code: _Optional[str]=..., severity: _Optional[_Union[AggregateProductStatus.ItemLevelIssue.Severity, str]]=..., resolution: _Optional[_Union[AggregateProductStatus.ItemLevelIssue.Resolution, str]]=..., attribute: _Optional[str]=..., description: _Optional[str]=..., detail: _Optional[str]=..., documentation_uri: _Optional[str]=..., product_count: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ITEM_LEVEL_ISSUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
    country: str
    stats: AggregateProductStatus.Stats
    item_level_issues: _containers.RepeatedCompositeFieldContainer[AggregateProductStatus.ItemLevelIssue]

    def __init__(self, name: _Optional[str]=..., reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]]=..., country: _Optional[str]=..., stats: _Optional[_Union[AggregateProductStatus.Stats, _Mapping]]=..., item_level_issues: _Optional[_Iterable[_Union[AggregateProductStatus.ItemLevelIssue, _Mapping]]]=...) -> None:
        ...