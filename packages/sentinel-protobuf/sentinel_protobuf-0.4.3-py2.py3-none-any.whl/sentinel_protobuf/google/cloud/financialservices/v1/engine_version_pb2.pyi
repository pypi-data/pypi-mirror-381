from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.financialservices.v1 import line_of_business_pb2 as _line_of_business_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EngineVersion(_message.Message):
    __slots__ = ('name', 'state', 'expected_limitation_start_time', 'expected_decommission_time', 'line_of_business')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[EngineVersion.State]
        ACTIVE: _ClassVar[EngineVersion.State]
        LIMITED: _ClassVar[EngineVersion.State]
        DECOMMISSIONED: _ClassVar[EngineVersion.State]
    STATE_UNSPECIFIED: EngineVersion.State
    ACTIVE: EngineVersion.State
    LIMITED: EngineVersion.State
    DECOMMISSIONED: EngineVersion.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_LIMITATION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DECOMMISSION_TIME_FIELD_NUMBER: _ClassVar[int]
    LINE_OF_BUSINESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: EngineVersion.State
    expected_limitation_start_time: _timestamp_pb2.Timestamp
    expected_decommission_time: _timestamp_pb2.Timestamp
    line_of_business: _line_of_business_pb2.LineOfBusiness

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[EngineVersion.State, str]]=..., expected_limitation_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expected_decommission_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., line_of_business: _Optional[_Union[_line_of_business_pb2.LineOfBusiness, str]]=...) -> None:
        ...

class ListEngineVersionsRequest(_message.Message):
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

class ListEngineVersionsResponse(_message.Message):
    __slots__ = ('engine_versions', 'next_page_token', 'unreachable')
    ENGINE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    engine_versions: _containers.RepeatedCompositeFieldContainer[EngineVersion]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, engine_versions: _Optional[_Iterable[_Union[EngineVersion, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetEngineVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...