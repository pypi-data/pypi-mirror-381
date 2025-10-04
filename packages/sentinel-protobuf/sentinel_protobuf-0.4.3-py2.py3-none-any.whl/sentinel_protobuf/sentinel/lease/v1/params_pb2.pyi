from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ('max_hours', 'min_hours', 'staking_share')
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    MIN_HOURS_FIELD_NUMBER: _ClassVar[int]
    STAKING_SHARE_FIELD_NUMBER: _ClassVar[int]
    max_hours: int
    min_hours: int
    staking_share: str

    def __init__(self, max_hours: _Optional[int]=..., min_hours: _Optional[int]=..., staking_share: _Optional[str]=...) -> None:
        ...