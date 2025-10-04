from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.geminidataanalytics.v1alpha import data_agent_pb2 as _data_agent_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListDataAgentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., show_deleted: bool=...) -> None:
        ...

class ListDataAgentsResponse(_message.Message):
    __slots__ = ('data_agents', 'next_page_token', 'unreachable')
    DATA_AGENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    data_agents: _containers.RepeatedCompositeFieldContainer[_data_agent_pb2.DataAgent]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, data_agents: _Optional[_Iterable[_Union[_data_agent_pb2.DataAgent, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListAccessibleDataAgentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'show_deleted', 'creator_filter')

    class CreatorFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREATOR_FILTER_UNSPECIFIED: _ClassVar[ListAccessibleDataAgentsRequest.CreatorFilter]
        NONE: _ClassVar[ListAccessibleDataAgentsRequest.CreatorFilter]
        CREATOR_ONLY: _ClassVar[ListAccessibleDataAgentsRequest.CreatorFilter]
        NOT_CREATOR_ONLY: _ClassVar[ListAccessibleDataAgentsRequest.CreatorFilter]
    CREATOR_FILTER_UNSPECIFIED: ListAccessibleDataAgentsRequest.CreatorFilter
    NONE: ListAccessibleDataAgentsRequest.CreatorFilter
    CREATOR_ONLY: ListAccessibleDataAgentsRequest.CreatorFilter
    NOT_CREATOR_ONLY: ListAccessibleDataAgentsRequest.CreatorFilter
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    show_deleted: bool
    creator_filter: ListAccessibleDataAgentsRequest.CreatorFilter

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., show_deleted: bool=..., creator_filter: _Optional[_Union[ListAccessibleDataAgentsRequest.CreatorFilter, str]]=...) -> None:
        ...

class ListAccessibleDataAgentsResponse(_message.Message):
    __slots__ = ('data_agents', 'next_page_token', 'unreachable')
    DATA_AGENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    data_agents: _containers.RepeatedCompositeFieldContainer[_data_agent_pb2.DataAgent]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, data_agents: _Optional[_Iterable[_Union[_data_agent_pb2.DataAgent, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDataAgentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDataAgentRequest(_message.Message):
    __slots__ = ('parent', 'data_agent_id', 'data_agent', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_AGENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_agent_id: str
    data_agent: _data_agent_pb2.DataAgent
    request_id: str

    def __init__(self, parent: _Optional[str]=..., data_agent_id: _Optional[str]=..., data_agent: _Optional[_Union[_data_agent_pb2.DataAgent, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateDataAgentRequest(_message.Message):
    __slots__ = ('update_mask', 'data_agent', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DATA_AGENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    data_agent: _data_agent_pb2.DataAgent
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., data_agent: _Optional[_Union[_data_agent_pb2.DataAgent, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteDataAgentRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...