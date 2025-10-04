from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EnvVar(_message.Message):
    __slots__ = ('name', 'value')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str

    def __init__(self, name: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class SecretRef(_message.Message):
    __slots__ = ('secret', 'version')
    SECRET_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    secret: str
    version: str

    def __init__(self, secret: _Optional[str]=..., version: _Optional[str]=...) -> None:
        ...

class SecretEnvVar(_message.Message):
    __slots__ = ('name', 'secret_ref')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    name: str
    secret_ref: SecretRef

    def __init__(self, name: _Optional[str]=..., secret_ref: _Optional[_Union[SecretRef, _Mapping]]=...) -> None:
        ...