from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ('max_allocations', 'staking_share', 'status_timeout')
    MAX_ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    STAKING_SHARE_FIELD_NUMBER: _ClassVar[int]
    STATUS_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    max_allocations: int
    staking_share: str
    status_timeout: _duration_pb2.Duration

    def __init__(self, max_allocations: _Optional[int]=..., staking_share: _Optional[str]=..., status_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...