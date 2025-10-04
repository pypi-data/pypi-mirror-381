from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from sentinel.session.v1 import params_pb2 as _params_pb2
from sentinel.session.v1 import session_pb2 as _session_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QuerySessionsRequest(_message.Message):
    __slots__ = ('pagination',)
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest

    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]]=...) -> None:
        ...

class QuerySessionsForAddressRequest(_message.Message):
    __slots__ = ('address', 'status', 'pagination')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    address: str
    status: _status_pb2.Status
    pagination: _pagination_pb2.PageRequest

    def __init__(self, address: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, str]]=..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]]=...) -> None:
        ...

class QuerySessionRequest(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=...) -> None:
        ...

class QueryParamsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class QuerySessionsResponse(_message.Message):
    __slots__ = ('sessions', 'pagination')
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[_session_pb2.Session]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, sessions: _Optional[_Iterable[_Union[_session_pb2.Session, _Mapping]]]=..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]]=...) -> None:
        ...

class QuerySessionsForAddressResponse(_message.Message):
    __slots__ = ('sessions', 'pagination')
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[_session_pb2.Session]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, sessions: _Optional[_Iterable[_Union[_session_pb2.Session, _Mapping]]]=..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]]=...) -> None:
        ...

class QuerySessionResponse(_message.Message):
    __slots__ = ('session',)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: _session_pb2.Session

    def __init__(self, session: _Optional[_Union[_session_pb2.Session, _Mapping]]=...) -> None:
        ...

class QueryParamsResponse(_message.Message):
    __slots__ = ('params',)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.Params

    def __init__(self, params: _Optional[_Union[_params_pb2.Params, _Mapping]]=...) -> None:
        ...