from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AdaptMessageRequest(_message.Message):
    __slots__ = ('name', 'protocol', 'payload', 'attachments')

    class AttachmentsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    protocol: str
    payload: bytes
    attachments: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., protocol: _Optional[str]=..., payload: _Optional[bytes]=..., attachments: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class AdaptMessageResponse(_message.Message):
    __slots__ = ('payload', 'state_updates', 'last')

    class StateUpdatesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    STATE_UPDATES_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    state_updates: _containers.ScalarMap[str, str]
    last: bool

    def __init__(self, payload: _Optional[bytes]=..., state_updates: _Optional[_Mapping[str, str]]=..., last: bool=...) -> None:
        ...

class Session(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSessionRequest(_message.Message):
    __slots__ = ('parent', 'session')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    session: Session

    def __init__(self, parent: _Optional[str]=..., session: _Optional[_Union[Session, _Mapping]]=...) -> None:
        ...