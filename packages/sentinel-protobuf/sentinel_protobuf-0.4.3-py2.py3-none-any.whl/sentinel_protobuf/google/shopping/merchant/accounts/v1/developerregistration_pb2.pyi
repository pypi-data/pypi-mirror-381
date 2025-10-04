from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DeveloperRegistration(_message.Message):
    __slots__ = ('name', 'gcp_ids')
    NAME_FIELD_NUMBER: _ClassVar[int]
    GCP_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    gcp_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., gcp_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class RegisterGcpRequest(_message.Message):
    __slots__ = ('name', 'developer_email')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    developer_email: str

    def __init__(self, name: _Optional[str]=..., developer_email: _Optional[str]=...) -> None:
        ...

class UnregisterGcpRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetDeveloperRegistrationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...