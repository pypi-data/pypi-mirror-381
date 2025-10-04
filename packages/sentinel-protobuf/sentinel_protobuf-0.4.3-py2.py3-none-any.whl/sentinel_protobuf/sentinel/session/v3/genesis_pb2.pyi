from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from sentinel.session.v3 import params_pb2 as _params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ('sessions', 'params')
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    params: _params_pb2.Params

    def __init__(self, sessions: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]]=..., params: _Optional[_Union[_params_pb2.Params, _Mapping]]=...) -> None:
        ...