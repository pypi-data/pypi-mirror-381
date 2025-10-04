from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.session.v3 import session_pb2 as _session_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ('base_session', 'subscription_id')
    BASE_SESSION_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    base_session: _session_pb2.BaseSession
    subscription_id: int

    def __init__(self, base_session: _Optional[_Union[_session_pb2.BaseSession, _Mapping]]=..., subscription_id: _Optional[int]=...) -> None:
        ...