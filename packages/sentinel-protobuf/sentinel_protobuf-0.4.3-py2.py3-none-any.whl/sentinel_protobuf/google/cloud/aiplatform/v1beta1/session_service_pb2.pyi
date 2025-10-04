from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1beta1 import session_pb2 as _session_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionRequest(_message.Message):
    __slots__ = ('parent', 'session')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    session: _session_pb2.Session

    def __init__(self, parent: _Optional[str]=..., session: _Optional[_Union[_session_pb2.Session, _Mapping]]=...) -> None:
        ...

class CreateSessionOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GetSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSessionsRequest(_message.Message):
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

class ListSessionsResponse(_message.Message):
    __slots__ = ('sessions', 'next_page_token')
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[_session_pb2.Session]
    next_page_token: str

    def __init__(self, sessions: _Optional[_Iterable[_Union[_session_pb2.Session, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateSessionRequest(_message.Message):
    __slots__ = ('session', 'update_mask')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    session: _session_pb2.Session
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, session: _Optional[_Union[_session_pb2.Session, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListEventsRequest(_message.Message):
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

class ListEventsResponse(_message.Message):
    __slots__ = ('session_events', 'next_page_token')
    SESSION_EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    session_events: _containers.RepeatedCompositeFieldContainer[_session_pb2.SessionEvent]
    next_page_token: str

    def __init__(self, session_events: _Optional[_Iterable[_Union[_session_pb2.SessionEvent, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class AppendEventRequest(_message.Message):
    __slots__ = ('name', 'event')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    event: _session_pb2.SessionEvent

    def __init__(self, name: _Optional[str]=..., event: _Optional[_Union[_session_pb2.SessionEvent, _Mapping]]=...) -> None:
        ...

class AppendEventResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...